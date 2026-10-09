#!/usr/bin/env python3
"""Structural checks for skilldeck skills. Run before committing.

Catches what silently breaks a skill pack: frontmatter that is not valid YAML
(an unquoted colon in a description is the recurring one), a name that does not
match its folder, a missing cross-tool manifest, a skill on disk that nobody
registered, a cross-reference to a skill that does not exist, and a relative
link to a reference file that has been renamed or removed.

Pass --links to also resolve external URLs. That is off by default because it
needs the network and can flake; the rest of the run is offline and fast.

Pass --inventory to print a per-skill word-count table (SKILL.md body vs
companions). The table is additive; validation still runs.
"""
import json, pathlib, re, sys

LINK = re.compile(r"\[[^\]]*\]\((?!https?://|#)([^)]+)\)")
# Progressive disclosure budget on the SKILL.md body (frontmatter excluded).
# A warning is noise, a failure is a split that did not happen. See
# .agents/conventions.md. Names in SIZE_ALLOWLIST may exceed FAIL_WORDS.
WARN_WORDS = 1200
FAIL_WORDS = 2000
SIZE_ALLOWLIST = set()

try:
    import yaml
except ImportError:
    yaml = None  # degraded mode, reported at the end

ROOT = pathlib.Path(__file__).resolve().parent.parent
# Skills that ship with a harness rather than with this pack. Referencing one is
# allowed only where the text says whose it is, which the check below enforces:
# the repo is installable standalone and must not imply a dependency it has not
# declared. Anything else belongs in docs/pack/inspirations.md under
# "Optional companions", named with its source, never as a bare /slash reference.
HARNESS_BUILTINS = {"code-review", "simplify", "run", "dataviz", "security-review"}
OPENAI_AGENT_FIELDS = {"interface", "policy", "dependencies"}
OPENAI_POLICY_FIELDS = {"products", "allow_implicit_invocation"}
OPENAI_PRODUCTS = {"CHAT", "CODEX"}
errors, warnings, skills, inventory = [], [], {}, []
skill_sources = {}


def skill_body(text):
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def word_count(text):
    return len(text.split())

for f in sorted(ROOT.glob("skills/*/*/SKILL.md")):
    rel = f.relative_to(ROOT)
    text = f.read_text()
    if not text.startswith("---\n"):
        errors.append(f"{rel}: no frontmatter"); continue
    block = text.split("---\n", 2)[1]
    if yaml is None:
        # Without a YAML parser, check the one failure that actually recurs here:
        # an unquoted colon in a value, which silently turns it into a mapping.
        fm = {}
        for raw in block.splitlines():
            if not raw or raw.startswith((" ", "\t", "#")):
                continue
            key, sep, value = raw.partition(":")
            if not sep:
                continue
            value = value.strip()
            if ": " in value and value[:1] not in "\"'>|":
                errors.append(f"{rel}: frontmatter value for '{key}' contains an unquoted ':', "
                              f"which is not valid YAML. Quote it or reword.")
            fm[key.strip()] = value
    else:
        try:
            fm = yaml.safe_load(block)
        except yaml.YAMLError as e:
            line = str(e).split("\n")[-2].strip() if "\n" in str(e) else e
            errors.append(f"{rel}: frontmatter is not valid YAML. An unquoted ':' in "
                          f"description is the usual cause. {line}")
            continue
    for key in ("name", "description"):
        if not fm.get(key):
            errors.append(f"{rel}: missing '{key}'")
    if fm.get("name") != f.parent.name:
        errors.append(f"{rel}: name '{fm.get('name')}' does not match folder '{f.parent.name}'")
    if not (f.parent / "agents" / "openai.yaml").exists():
        errors.append(f"{rel}: missing agents/openai.yaml")
    if "—" in text:
        errors.append(f"{rel}: contains an em-dash, which the authoring conventions ban")
    if "## When this does not apply" not in text:
        errors.append(f"{rel}: missing the 'When this does not apply' guardrail")

    # A model-invoked skill is reached only through its description, so the
    # description carries triggers. A user-invoked one is human-facing by
    # convention and is exempt from both checks below.
    user_invoked = fm.get("disable-model-invocation") in (True, "true")
    desc = fm.get("description") or ""
    if not user_invoked and "Use when" not in desc:
        errors.append(f"{rel}: description has no 'Use when' clause. A model-invoked "
                      f"skill is routed on its description; see .agents/conventions.md.")

    # policy.allow_implicit_invocation is the OpenAI-side half of the same
    # decision as disable-model-invocation. One without the other means a skill
    # is user-invoked on one harness and model-invoked on another.
    oai = f.parent / "agents" / "openai.yaml"
    if oai.exists() and yaml is not None:
        try:
            meta = yaml.safe_load(oai.read_text()) or {}
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: agents/openai.yaml is not valid YAML. {exc}")
            meta = None
        if meta is not None:
            unknown = set(meta) - OPENAI_AGENT_FIELDS
            if unknown:
                errors.append(f"{rel}: agents/openai.yaml has unsupported top-level fields "
                              f"{sorted(unknown)}")
            iface = meta.get("interface") or {}
            for key in ("display_name", "short_description"):
                if not iface.get(key):
                    errors.append(f"{rel}: agents/openai.yaml missing interface.{key}")
            policy = meta.get("policy") or {}
            if not isinstance(policy, dict):
                errors.append(f"{rel}: agents/openai.yaml policy must be a mapping")
                policy = {}
            unknown_policy = set(policy) - OPENAI_POLICY_FIELDS
            if unknown_policy:
                errors.append(f"{rel}: agents/openai.yaml policy has unsupported fields "
                              f"{sorted(unknown_policy)}")
            products = policy.get("products")
            if products is not None and (
                not isinstance(products, list)
                or not products
                or any(product not in OPENAI_PRODUCTS for product in products)
            ):
                errors.append(f"{rel}: agents/openai.yaml policy.products must contain "
                              "CHAT, CODEX, or both")
            implicit = policy.get("allow_implicit_invocation")
            if implicit is not None and not isinstance(implicit, bool):
                errors.append(f"{rel}: agents/openai.yaml "
                              "policy.allow_implicit_invocation must be true or false")
            if user_invoked and implicit is not False:
                errors.append(f"{rel}: has disable-model-invocation but its openai.yaml "
                              f"does not set policy.allow_implicit_invocation: false.")
            if not user_invoked and implicit is False:
                errors.append(f"{rel}: openai.yaml forbids implicit invocation but the "
                              f"frontmatter has no disable-model-invocation. Set both or neither.")

    if fm.get("name"):
        if fm["name"] in skills:
            errors.append(f"{rel}: duplicate skill name '{fm['name']}', first declared in "
                          f"{skill_sources[fm['name']]}")
        skill_sources[fm["name"]] = rel
        skills[fm["name"]] = text
        if len(f"skilldeck:{fm['name']}") > 64:
            errors.append(f"{rel}: OpenAI plugin and skill identity exceeds 64 characters")
        body = skill_body(text)
        body_words = word_count(body)
        name = fm["name"]
        if name not in SIZE_ALLOWLIST:
            if body_words > FAIL_WORDS:
                errors.append(f"{rel}: SKILL.md body is {body_words} words; the budget is "
                              f"{FAIL_WORDS} (see .agents/conventions.md). Split a lookup "
                              f"or surface page into a companion.")
            elif body_words > WARN_WORDS:
                warnings.append(f"{rel}: SKILL.md body is {body_words} words (warn above "
                                f"{WARN_WORDS}). Consider splitting a lookup into a companion.")
        companions, companion_words, linked = [], 0, []
        for p in sorted(f.parent.rglob("*")):
            if not p.is_file() or p == f or p.suffix not in {".md", ".yaml", ".yml"}:
                continue
            if p.parent.name == "agents" and p.name == "openai.yaml":
                continue
            companions.append(str(p.relative_to(f.parent)))
            companion_words += word_count(p.read_text())
        for target in LINK.findall(text):
            dest = (f.parent / target.split("#")[0]).resolve()
            try:
                dest.relative_to(f.parent.resolve())
            except ValueError:
                continue
            if dest != f.resolve() and dest.exists() and target.split("#")[0] not in linked:
                linked.append(target.split("#")[0])
        inventory.append({
            "name": name,
            "rel": str(rel),
            "user_invoked": user_invoked,
            "body_words": body_words,
            "companion_words": companion_words,
            "companions": companions,
            "linked": linked,
        })

graph = {}
for name, text in skills.items():
    refs = re.findall(r'call the Skill tool with "([^"]+)"', text, re.IGNORECASE)
    for ref in refs:
        if ref not in skills:
            errors.append(f"{name}: calls '{ref}', which is not a skill in this pack. "
                          f"The Skill tool cannot reach another plugin's skill.")
    graph[name] = [r for r in dict.fromkeys(refs) if r in skills]

# A cycle in the call graph is an agent that can be handed back to a skill it is
# already inside. The "applies once per task" rule in .agents/conventions.md is
# what makes the surviving ones safe, but a NEW one is a real loop risk, so the
# known set is allowlisted by the single edge that closes it and anything else
# fails. Fix a new cycle by reversing an edge (see "Chains run one direction"),
# never by extending this list.
KNOWN_BACK_EDGES = {
    ("design-inspiration", "curate-design-inspiration"),
    ("design-inspiration", "design-brief"),
    ("security-hardening", "dependency-choice"),
    ("security-hardening", "api-design"),
    ("release-flow", "ship-flow"),
}

def find_cycles():
    found, seen = [], set()
    def walk(node, stack):
        for nxt in graph.get(node, []):
            if nxt in stack:
                cycle = stack[stack.index(nxt):]
                rotate = cycle.index(min(cycle))
                found.append(tuple(cycle[rotate:] + cycle[:rotate]))
            elif nxt not in seen:
                seen.add(nxt)
                walk(nxt, stack + [nxt])
    for start in sorted(graph):
        seen.add(start)
        walk(start, [start])
    return sorted(set(found), key=lambda c: (len(c), c))

for cycle in find_cycles():
    edges = list(zip(cycle, cycle[1:] + cycle[:1]))
    if any(e in KNOWN_BACK_EDGES for e in edges):
        continue
    path = " -> ".join(cycle + cycle[:1])
    errors.append(f"cross-skill call cycle: {path}. Reverse one edge so the chain "
                  f"runs one direction, per .agents/conventions.md.")

# Skills that emit code must end at the completion gate. The list is explicit
# rather than inferred so that a new code-changing skill has to be added here
# deliberately, instead of shipping ungated because nothing noticed.
MUST_REACH_GATE = {
    "create", "debug", "bootstrap-repo", "refactor", "migration", "forms", "frontend-craft", "api-design",
    "state-management", "security-hardening", "observability", "design-tokens",
    "perf-audit", "ship-flow", "release-flow", "testing-strategy", "mitigate-incident",
}
for name in sorted(MUST_REACH_GATE):
    if name not in skills:
        errors.append(f"{name}: listed as code-changing in validate.py but is not a skill")
    elif "verify-before-done" not in graph.get(name, []):
        errors.append(f"{name}: changes code but never calls the Skill tool with "
                      f"'verify-before-done'. Every skill that writes code ends at the gate.")

# The gate is a sink. Anything it calls could route back into it, which the
# cycle check would catch, but naming the rule here makes the failure legible.
gate_calls = set(graph.get("verify-before-done", [])) - {"resolve-conventions"}
if gate_calls:
    errors.append(f"verify-before-done calls {sorted(gate_calls)}. It is the terminal gate "
                  f"and must stay a sink; state the guidance inline instead.")

# Payload blocks are spliced into a file the user owns, between markers. An
# unbalanced pair means the splice has no end and would swallow their content.
for payload in sorted((ROOT / "skills/foundation/setup-skills").glob("*-block.md")):
    text = payload.read_text()
    for marker in set(re.findall(r"skilldeck-skills:([a-z-]+):(?:begin|end)", text)):
        begins = text.count(f"skilldeck-skills:{marker}:begin")
        ends = text.count(f"skilldeck-skills:{marker}:end")
        if begins != 1 or ends != 1:
            errors.append(f"{payload.relative_to(ROOT)}: marker '{marker}' appears "
                          f"{begins} begin / {ends} end, expected exactly one of each.")

# Design-inspiration seed captures: closed-list domains/principles from taxonomy.md.
# Keeps the progressive-disclosure indexes honest without inventing a second catalog.
TAXONOMY = ROOT / "skills/design/design-inspiration/taxonomy.md"
SEED_REFS = ROOT / "skills/design/design-inspiration/references"
if TAXONOMY.exists() and yaml is not None:
    tax_text = TAXONOMY.read_text()
    # Principles share the same table-row shape; split by section headers.
    domain_section = re.search(
        r"## Domains\n(.*?)(?=\n## Principles\n)", tax_text, re.S)
    principle_section = re.search(
        r"## Principles\n(.*?)(?=\n## )", tax_text, re.S)
    allowed_domains = set()
    if domain_section:
        allowed_domains = set(re.findall(r"^\| `([a-z0-9-]+)` \|", domain_section.group(1), re.M))
    allowed_principles = set()
    if principle_section:
        allowed_principles = set(re.findall(r"^\| `([a-z0-9-]+)` \|", principle_section.group(1), re.M))
    if not allowed_domains or not allowed_principles:
        errors.append("skills/design/design-inspiration/taxonomy.md: could not parse "
                      "domain or principle closed lists from the tables")
    else:
        for path in sorted(SEED_REFS.glob("*.md")):
            if path.name == "README.md":
                continue
            rel = path.relative_to(ROOT)
            text = path.read_text()
            if not text.startswith("---\n"):
                errors.append(f"{rel}: seed capture missing frontmatter")
                continue
            parts = text.split("---\n", 2)
            if len(parts) != 3:
                errors.append(f"{rel}: seed capture frontmatter is malformed")
                continue
            try:
                fm = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError as exc:
                errors.append(f"{rel}: seed capture frontmatter is not valid YAML. {exc}")
                continue
            domains = fm.get("domains")
            if not isinstance(domains, list) or not domains:
                errors.append(f"{rel}: seed capture requires a non-empty 'domains' list")
            else:
                if len(domains) > 3:
                    errors.append(f"{rel}: 'domains' has {len(domains)} values, max is 3")
                for tag in domains:
                    if tag not in allowed_domains:
                        errors.append(f"{rel}: unknown domain '{tag}' "
                                      f"(not in taxonomy.md Domains)")
            principles = fm.get("principles")
            if principles is not None:
                if not isinstance(principles, list):
                    errors.append(f"{rel}: 'principles' must be a YAML list when present")
                else:
                    if len(principles) > 4:
                        errors.append(f"{rel}: 'principles' has {len(principles)} values, max is 4")
                    for tag in principles:
                        if tag not in allowed_principles:
                            errors.append(f"{rel}: unknown principle '{tag}' "
                                          f"(not in taxonomy.md Principles)")
elif TAXONOMY.exists() and yaml is None:
    warnings.append("design-inspiration seed taxonomy check skipped (pyyaml missing)")

# No silent external dependency. A bare `/name` for something this pack does not
# ship reads as though the reader has it, which breaks the moment they do not.
for f in sorted([*ROOT.glob("skills/**/*.md"), *ROOT.glob("docs/**/*.md"), ROOT / "README.md"]):
    rel, text = f.relative_to(ROOT), f.read_text()
    for i, line in enumerate(text.splitlines(), 1):
        # With a slash it reads as invocable; without one it still reads as ours.
        # Bare names are only checked against known-external ones, since an
        # unrestricted check would fire on every npm package and CSS token.
        refs = re.findall(r"`/([a-z][a-z0-9-]+)`", line)
        refs += [m for m in re.findall(r"`([a-z][a-z0-9-]+)`", line)
                 if m in HARNESS_BUILTINS and m not in skills]
        for ref in refs:
            if ref in skills or ref == "setup-skills":
                continue
            if ref in HARNESS_BUILTINS and re.search(r"Claude Code|harness|ships", line):
                continue
            errors.append(f"{rel}:{i}: `/{ref}` is not in this pack. Say whose it is on the "
                          f"same line, or list it under Optional companions in docs/pack/inspirations.md.")

# Relative links: a renamed reference file breaks these with no other symptom.
for f in sorted([*ROOT.glob("skills/**/*.md"), *ROOT.glob("docs/**/*.md"), ROOT / "README.md"]):
    rel = f.relative_to(ROOT)
    for target in LINK.findall(f.read_text()):
        path = (f.parent / target.split("#")[0]).resolve()
        if not path.exists():
            errors.append(f"{rel}: link to '{target}' does not resolve")

# Markdown style. The repo is already uniform on every axis below, so these
# lock it in rather than fixing anything. A formatter was measured against this
# repo and rejected: it churned 384 lines for no consistency gain, and without
# the frontmatter plugin it collapses every SKILL.md's frontmatter into a heading.
for f in sorted([*ROOT.glob("skills/**/*.md"), *ROOT.glob("docs/**/*.md"),
                 ROOT / "README.md", ROOT / "CONTEXT.md", ROOT / ".agents/conventions.md"]):
    rel, text = f.relative_to(ROOT), f.read_text()
    fenced = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            if not fenced and line.strip() == "```":
                errors.append(f"{rel}:{i}: opening code fence has no language (use ```text if none fits)")
            fenced = not fenced
            continue
        if fenced:
            continue
        # Inline code is quoted material, so a rule may name the syntax it bans.
        line = re.sub(r"`[^`]*`", "``", line)
        if re.match(r"^\s*[*+] ", line):
            errors.append(f"{rel}:{i}: list marker is '{line.lstrip()[0]}', this repo uses '-'")
        if re.search(r"(?<!_)__(?!_)\S", line):
            errors.append(f"{rel}:{i}: strong emphasis uses '__', this repo uses '**'")
        if line.startswith("|") and line.count("|") > 2 and not line.startswith("| "):
            errors.append(f"{rel}:{i}: table row needs a space after the leading pipe")
    if "\n\n\n\n" in text:
        errors.append(f"{rel}: three or more consecutive blank lines")

# Hygiene, cheap and keeps diffs from carrying noise.
for f in sorted([*ROOT.glob("skills/**/*"), *ROOT.glob("docs/**/*"), ROOT / "README.md",
                 ROOT / "CONTEXT.md", ROOT / ".agents/conventions.md"]):
    if not f.is_file() or f.suffix not in {".md", ".yaml", ".yml"}:
        continue
    rel, text = f.relative_to(ROOT), f.read_text()
    if text and not text.endswith("\n"):
        errors.append(f"{rel}: no newline at end of file")
    for i, line in enumerate(text.splitlines(), 1):
        if line != line.rstrip():
            errors.append(f"{rel}:{i}: trailing whitespace")
            break

on_disk = {str(p.parent.relative_to(ROOT)) for p in ROOT.glob("skills/*/*/SKILL.md")}

# Harness manifests. They drift the moment one is edited alone, so the shared
# fields are compared rather than trusted. Claude Code and Cursor list every
# leaf path because their plugin loaders do not recurse into bucket folders.
# Codex walks ./skills/ from the plugin directory. Cursor's plugin.json lives under
# plugins/skilldeck so GitHub import can resolve a subdirectory source. The skill
# files live in that directory too: Cursor refuses a symlink whose target leaves
# the plugin directory.
MANIFESTS = {
    ".claude-plugin/plugin.json": "list",
    "plugins/skilldeck/.cursor-plugin/plugin.json": "list",
    "plugins/skilldeck/.codex-plugin/plugin.json": "dir",
}
loaded = {}
for path, kind in MANIFESTS.items():
    p = ROOT / path
    if not p.exists():
        errors.append(f"{path}: missing harness manifest"); continue
    try:
        loaded[path] = json.loads(p.read_text())
    except Exception as e:
        errors.append(f"{path}: {e}"); continue
    if kind == "dir":
        target = loaded[path].get("skills")
        plugin_root = (ROOT / path).parent.parent
        skills_dir = plugin_root / "skills"
        if target != "./skills/":
            errors.append(f"{path}: 'skills' should be './skills/', found {target!r}")
        elif skills_dir.is_symlink() or not skills_dir.is_dir():
            errors.append(f"{path}: ./skills/ must be a real directory under {plugin_root.relative_to(ROOT)}")
    elif kind == "list":
        listed = loaded[path].get("skills")
        if not isinstance(listed, list):
            errors.append(f"{path}: 'skills' should be a list of leaf paths, found {listed!r}")
        else:
            names = {r.lstrip("./") for r in listed}
            for missing in sorted(on_disk - names):
                errors.append(f"{path}: {missing} on disk but not registered")
            for stale in sorted(names - on_disk):
                errors.append(f"{path}: {stale} registered but not on disk")

try:
    json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
except Exception as e:
    errors.append(f".claude-plugin/marketplace.json: {e}")

try:
    mkt = json.loads((ROOT / ".cursor-plugin/marketplace.json").read_text())
    plugins = mkt.get("plugins") or []
    if not plugins:
        errors.append(".cursor-plugin/marketplace.json: no plugins listed")
    else:
        entry = plugins[0]
        for banned in ("keywords", "category", "tags"):
            if banned in entry:
                errors.append(f".cursor-plugin/marketplace.json: '{banned}' belongs on plugin.json, not the marketplace entry")
        expected_name = loaded.get("plugins/skilldeck/.cursor-plugin/plugin.json", {}).get("name")
        if expected_name and entry.get("name") != expected_name:
            errors.append(f".cursor-plugin/marketplace.json: plugin name {entry.get('name')!r} does not match plugin.json {expected_name!r}")
        if (mkt.get("metadata") or {}).get("pluginRoot") != "plugins":
            errors.append(".cursor-plugin/marketplace.json: metadata.pluginRoot should be 'plugins'")
        if entry.get("source") != "skilldeck":
            errors.append(f".cursor-plugin/marketplace.json: source should be 'skilldeck', found {entry.get('source')!r}")
        if mkt.get("name") != "skilldeck":
            errors.append(f".cursor-plugin/marketplace.json: name should be 'skilldeck', found {mkt.get('name')!r}")
    cursor_skills = ROOT / "plugins/skilldeck/skills"
    root_skills = ROOT / "skills"
    if cursor_skills.is_symlink() or not cursor_skills.is_dir():
        errors.append("plugins/skilldeck/skills: must be a real directory, not a symlink")
    if not root_skills.is_symlink():
        errors.append("skills: must be a symlink to plugins/skilldeck/skills")
    else:
        link = root_skills.readlink()
        if str(link) != "plugins/skilldeck/skills":
            errors.append(f"skills: symlink should be plugins/skilldeck/skills, found {str(link)!r}")
except FileNotFoundError:
    errors.append(".cursor-plugin/marketplace.json: missing")
except Exception as e:
    errors.append(f".cursor-plugin/marketplace.json: {e}")

try:
    codex_mkt = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    if codex_mkt.get("name") != "skilldeck":
        errors.append(
            ".agents/plugins/marketplace.json: name should be 'skilldeck', "
            f"found {codex_mkt.get('name')!r}"
        )
    codex_plugins = codex_mkt.get("plugins") or []
    if len(codex_plugins) != 1:
        errors.append(".agents/plugins/marketplace.json: expected exactly one plugin")
    else:
        source = codex_plugins[0].get("source") or {}
        if codex_plugins[0].get("name") != "skilldeck":
            errors.append(
                ".agents/plugins/marketplace.json: plugin name should be 'skilldeck', "
                f"found {codex_plugins[0].get('name')!r}"
            )
        if source.get("path") != "./plugins/skilldeck":
            errors.append(
                ".agents/plugins/marketplace.json: source.path should be './plugins/skilldeck', "
                f"found {source.get('path')!r}"
            )
except FileNotFoundError:
    errors.append(".agents/plugins/marketplace.json: missing")
except Exception as e:
    errors.append(f".agents/plugins/marketplace.json: {e}")

if len(loaded) > 1:
    ref_path, ref = next(iter(loaded.items()))
    for field in ("name", "version", "license", "homepage", "repository"):
        values = {p: m.get(field) for p, m in loaded.items()}
        if len(set(values.values())) > 1:
            errors.append(f"manifests disagree on '{field}': {values}")

canonical_version = loaded.get(".claude-plugin/plugin.json", {}).get("version")

gem = ROOT / "gemini-extension.json"
if not gem.exists():
    errors.append("gemini-extension.json: missing harness manifest")
else:
    try:
        gemini = json.loads(gem.read_text())
        ctx = gemini.get("contextFileName")
        if not ctx:
            errors.append("gemini-extension.json: no contextFileName")
        elif not (ROOT / ctx).exists():
            errors.append(f"gemini-extension.json: contextFileName '{ctx}' does not exist")
        if gemini.get("name") != "skilldeck":
            errors.append(f"gemini-extension.json: name should be 'skilldeck', found {gemini.get('name')!r}")
        if canonical_version and gemini.get("version") != canonical_version:
            errors.append(
                f"gemini-extension.json: version {gemini.get('version')!r} does not match "
                f".claude-plugin/plugin.json {canonical_version!r}"
            )
    except Exception as e:
        errors.append(f"gemini-extension.json: {e}")

if canonical_version:
    try:
        claude_mkt = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    except Exception:
        claude_mkt = None
    if isinstance(claude_mkt, dict):
        entry = next(
            (item for item in claude_mkt.get("plugins") or []
             if isinstance(item, dict) and item.get("name") == "skilldeck"),
            None,
        )
        if claude_mkt.get("name") != "skilldeck":
            errors.append(
                ".claude-plugin/marketplace.json: name should be 'skilldeck', "
                f"found {claude_mkt.get('name')!r}"
            )
        if claude_mkt.get("renames") != {"skills": "skilldeck", "skillverse": None}:
            errors.append(
                ".claude-plugin/marketplace.json: renames should map 'skills' to "
                "'skilldeck' and 'skillverse' to null, "
                f"found {claude_mkt.get('renames')!r}"
            )
        if entry is None:
            errors.append(".claude-plugin/marketplace.json: no plugin named 'skilldeck'")
        elif entry.get("version") != canonical_version:
            errors.append(
                ".claude-plugin/marketplace.json: version "
                f"{entry.get('version')!r} does not match .claude-plugin/plugin.json {canonical_version!r}"
            )

for required in ("AGENTS.md",):
    if not (ROOT / required).exists():
        errors.append(f"{required}: missing")

if "--links" in sys.argv:
    import urllib.request, urllib.error
    # URLs inside a code fence are illustrative, and RFC 2606 reserves the
    # example domains for exactly that, so neither is a link to resolve.
    RESERVED = ("example.com", "example.org", "example.net", "localhost")
    urls = set()
    for f in [*ROOT.glob("**/*.md")]:
        if ".git" in f.parts: continue
        fenced = False
        for line in f.read_text().splitlines():
            if line.startswith("```"):
                fenced = not fenced
                continue
            if fenced:
                continue
            # Trailing backtick, sentence period, and similar prose marks are
            # not part of the URL. Inline code like `https://host/path`. would
            # otherwise be requested with the closer attached and 404.
            for u in re.findall(r"https://[^\s)\]]+", line):
                u = u.rstrip("`.,;:!?\"'*")
                if not any(d in u for d in RESERVED):
                    urls.add(u)
    for url in sorted(urls):
        try:
            req = urllib.request.Request(url, method="HEAD",
                                         headers={"User-Agent": "skilldeck-skills-validate"})
            urllib.request.urlopen(req, timeout=10)
        except urllib.error.HTTPError as e:
            # 403/405: host refuses HEAD or this user agent. 429: rate limit.
            # The host answered, so the link is not dead.
            if e.code not in (403, 405, 429):
                errors.append(f"dead link: {url} ({e.code})")
        except Exception as e:
            errors.append(f"unreachable link: {url} ({type(e).__name__})")

if yaml is None:
    print("WARNING: pyyaml not found, so frontmatter is only partially checked.")
    print(f"  This interpreter is {sys.executable}. On macOS the system python3 cannot")
    print("  pip install; use a different interpreter, a venv, or pipx.")
    print("  CI runs the full check either way.\n")

if "--inventory" in sys.argv:
    print("skill                           invoke   skill.md  companions  linked")
    total_body = total_comp = 0
    for row in inventory:
        invoke = "user" if row["user_invoked"] else "model"
        linked = ", ".join(row["linked"]) if row["linked"] else "-"
        print(f"{row['name']:<30} {invoke:<7} {row['body_words']:>8} {row['companion_words']:>11}  {linked}")
        total_body += row["body_words"]
        total_comp += row["companion_words"]
    print(f"{'TOTAL':<30} {'':<7} {total_body:>8} {total_comp:>11}")
    print()

if warnings:
    print(f"WARN ({len(warnings)})")
    for w in warnings:
        print("  -", w)
    print()

if errors:
    print(f"FAIL ({len(errors)})")
    for e in errors: print("  -", e)
    sys.exit(1)
print(f"OK: {len(skills)} skills")
