# jon-skills

Vendor-neutral agent skills for JavaScript, TypeScript, React and React Native, plus the design and delivery work around the code. 31 skills, installable as a plugin or as plain files.

## What makes it different

Most skill sets bake in a stack. These resolve it. Before any tool or pattern choice, a skill walks one **precedence chain** and stops at the first tier that answers:

1. **Project** what the repo already uses (lockfile, `package.json`, configs, existing layout). Detection always wins.
2. **Company** a standardization config or skill carried by the repo.
3. **Personal** your seeded tiebreakers, only where the two above are silent.
4. **Community** on greenfield, the current default offered with a reason and confirmed before it is applied.

So the same skills work on a legacy npm/Jest service, a pnpm/Vitest monorepo and a fresh Expo app without special-casing.

Every skill also carries the guardrails that earn their place in it: **When this does not apply** (all of them, so a skill is not applied to a one-line change), **Excuses that do not hold** (the sentence an agent tells itself to skip the discipline, and the rebuttal), **Before you hand it over** (what actually goes wrong in that skill's output), and **Persistence** on the two that set a session-long posture. A guardrail shapes how a skill is applied and never reduces what the agent may analyze, search or consider. Authoring rules are in [`.agents/conventions.md`](.agents/conventions.md).

## Install

There are two ways in, and they behave differently. **Pick one**: installing both leaves you with every skill twice.

| | **Plugin** | **Files** (`npx skills`) |
| --- | --- | --- |
| What you get | A managed bundle of all 30, updating when the repo ships | Editable copies of the skills you choose |
| Invocation | Namespaced: `/jon:setup-skills` | Bare: `/setup-skills` |
| Install everything | yes | yes |
| Install one skill | no | yes |
| Install one category | no | no, list the names |
| Remove one skill | no | yes |
| Remove everything | yes | yes |
| Disable without removing | yes | no |
| Harnesses | Claude Code, Codex, Cursor, Gemini | Dozens, including all of those |

### Files, any agent

The [open skills CLI](https://github.com/vercel-labs/skills) handles this repo's layout, since it walks a skill directory three levels deep and supports `skills/<category>/<name>/SKILL.md`.

```bash
npx skills add jonathanjuliani/skills --list          # see what is in here first
npx skills add jonathanjuliani/skills                 # pick interactively
npx skills add jonathanjuliani/skills --all           # take everything
npx skills add jonathanjuliani/skills --skill design-review --skill forms
```

There is no category flag, so a whole category means listing its names. Add `-g` for your user directory instead of the project, and `-a cursor` or `-a claude-code` to target one agent.

### Claude Code

```bash
/plugin marketplace add jonathanjuliani/skills
/plugin install jon@skills
```

Skills arrive namespaced, so setup is `/jon:setup-skills`. Choose a scope when prompted: **user** (all your projects), **project** (committed to `.claude/settings.json`, shared with collaborators) or **local** (this repo, just you).

### Codex

Reads `.codex-plugin/plugin.json`, which points at `skills/`. Skills are invoked with `@`, so setup is `@setup-skills`.

```bash
codex plugin marketplace add jonathanjuliani/skills
codex plugin add jon@skills
```

### Cursor

Reads `plugins/jon/.cursor-plugin/plugin.json`, which lists every skill path (Cursor plugins do not recurse into bucket folders). These are workflows, so they belong in the skills layer rather than pasted into `.cursor/rules/*.mdc`. GitHub import needs the plugin in a subdirectory: `.cursor-plugin/marketplace.json` points at `plugins/jon` with a bare `source` name. A repo-root `"source": "./"` is silently rejected.

**Local copy (plugin development / offline).** Does not go through GitHub import. Cursor skips a symlink that points at a clone elsewhere on disk, so copy the plugin into `~/.cursor/plugins/local` instead:

```bash
./scripts/install-cursor.sh
```

Then fully quit Cursor (`Cmd+Q`) and reopen, or run Developer: Reload Window. Enable **Include third-party Plugins, Skills, and other configs**. On Teams or Enterprise, an admin also needs **Allow Local Plugin Imports**. Confirm all 31 skills under Customize → Skills, then run `/setup-skills` (or `/jon:setup-skills` if the plugin is namespaced). Re-run the script after you change the plugin locally.

**GitHub import (any plan).** Customize → Plugins → From GitHub Repository → `https://github.com/jonathanjuliani/skills`. Cursor reads `.cursor-plugin/marketplace.json` and installs `jon` from `plugins/jon`. Choose user or project scope. Setup is `/jon:setup-skills` (or `/setup-skills` if Cursor does not namespace). If the import dialog closes with no plugin and no cache folder, use the local copy instead.

**Team Marketplace.** On Teams or Enterprise, an admin can import the GitHub repo: Dashboard → Plugins → Add Marketplace → Import from Repo → `https://github.com/jonathanjuliani/skills`. Cursor reads `.cursor-plugin/marketplace.json`.

**Official Marketplace.** Once listed, install from Customize → Marketplace. Until then, submit the public repo at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish).

### Gemini CLI

```bash
gemini extensions install https://github.com/jonathanjuliani/skills
```

Reads `gemini-extension.json`, which loads `GEMINI.md` as context. That file tells the agent to open the routing block before a non-trivial task. The Coverage section is the human map of the same pack, not a second catalog for the agent.

### Then, once per repo

```bash
/jon:setup-skills     # plugin install
/setup-skills         # installed as files
```

Confirms your personal defaults, detects the project, writes `.jon-skills/config.yaml`, and offers to add a verification rule to the repo's `AGENTS.md` or `CLAUDE.md`. Everything it writes outside its own config needs an explicit yes.

> Developing locally? Point the marketplace at your clone: `/plugin marketplace add ~/development/jon/skills`

## Remove

### Files

```bash
npx skills list                      # what is installed, and from where
npx skills remove design-review      # one skill
npx skills remove forms design-brief # several
npx skills remove --all              # everything
```

`remove --all` removes **every installed skill from every source**, not only this pack. To clear just this one, name its skills, or use `npx skills remove --skill '*' -a <agent>` to clear one agent.

### Claude Code

```bash
/plugin disable jon@skills     # keep it installed, stop loading it
/plugin enable jon@skills      # put it back
/plugin uninstall jon@skills   # remove it
```

Disable is the one to reach for first: it costs nothing to undo and it is how you find out whether a pack is earning its context. Use `/plugin list` to see what is installed.

Removing the marketplace also uninstalls anything installed from it:

```bash
/plugin marketplace remove skills
```

For scripting, the `claude plugin` shell commands do the same without opening the panel, and take `--scope`.

## Skills

### Foundation

- **resolve-conventions** (model-invoked): the precedence engine. Detects a project's conventions and resolves anything unresolved against personal then community defaults.
- **setup-skills** (user-invoked): one-time setup. Confirm personal defaults, detect the project, write `.jon-skills/config.yaml`, and **optionally** add two blocks to the repo's `AGENTS.md` or `CLAUDE.md`: a verification rule, and a routing table mapping the moments of a task to the skill that owns each. Each is asked separately and written only between its own markers.
- **agent-instructions** (model-invoked): write or repair a repo's `AGENTS.md` or `CLAUDE.md` so its rules actually bind, on the budget of being read every turn.

### Engineering

- **project-shape** (model-invoked): detect single-repo, monorepo, or modular, and recommend folder and structure best practices per surface (backend, frontend, mobile).
- **ts-standards** (model-invoked): JS/TS conventions reference (naming, types, error handling, module boundaries, validation at boundaries). Principles, not vendors.
- **create** (model-invoked): scaffold a new component, module, package, service, or screen to the resolved conventions and shape. Walks a YAGNI ladder first, since the cheapest unit of code is the one nobody writes.
- **refactor** (model-invoked): behavior-preserving refactor toward the project's conventions, tests green throughout, and no fence removed before it is understood.
- **api-design** (model-invoked): choose REST, tRPC, or GraphQL by consumer, with typed, validated contracts.
- **security-hardening** (model-invoked): find where the system extends trust (untrusted input, access control, secrets, supply chain) and put the right control there.
- **state-management** (model-invoked): separate server state from client state and pick the right tool for each.
- **forms** (model-invoked): forms people can finish. Labels that persist, validation that fires at the right moment, errors that never destroy typed input, and submit that happens once.
- **frontend-craft** (model-invoked): compose React and React Native components well and treat accessibility as part of the build, reaching for the platform before a dependency. Takes its direction from `design-brief`.
- **testing-strategy** (model-invoked): choose seams and test kinds, concentrate effort on critical paths, and run the red-green loop.
- **verify-before-done** (model-invoked): set the observable criterion before starting, then prove it with fresh command output before claiming anything is done, fixed, or passing.
- **dependency-choice** (model-invoked): decide whether to add a dependency and which, judged on current community adoption, fit, and exposure.
- **perf-audit** (model-invoked): measure, fix the dominant cost, re-measure; guidance per surface.
- **observability** (model-invoked): instrument for the questions production will ask, and alert on symptoms a user can feel.
- **ship-flow** (model-invoked): move a change to production in small steps, with CI as a gate, flags, staged rollout, and an undo path.
- **migration** (model-invoked): retire an old dependency, API, or pattern with expand, migrate, contract, and treat deleting the old thing as the actual finish line.
- **release-flow** (model-invoked): versioning, changelog, and publishing, matching the project's existing process.

### Design

These skills are the decide half of System at Designs. The folder stays so that decision stays separate from the build in `frontend-craft`. See [Coverage](#coverage).

- **design-brief** (model-invoked): establish the surface kind, the audience and what they are doing, the references, the dials, and the constraints that override taste. One sentence that the rest of the work is checked against.
- **information-architecture** (model-invoked): content, hierarchy, navigation, screen and URL structure, naming and flows, decided before anything is styled.
- **design-inspiration** (model-invoked): take a reference apart and reuse the reasoning rather than the pixels, including extracting a token set from a live page and knowing a convention from a signature.
- **curate-design-inspiration** (model-invoked): after user confirmation, discover categories and live examples from curated galleries, dedupe against the store, and write new capture entries to the personal store.
- **design-tokens** (model-invoked): name decisions by role rather than by value, define both themes together, and adopt a token system in a codebase that hardcodes values today.
- **design-review** (model-invoked): scored usability critique ranked by user impact, so a finding is a row a team can prioritise instead of an opinion.

They run in that order on a new surface: a read, then the structure, then the direction and its tokens, then the build in `engineering/`, then the score. On an existing product most of it is already answered and the job is to inherit rather than decide.

`design-inspiration` ships a seed of captured references under `skills/design/design-inspiration/references/`, and accumulates further reads in a personal store at `~/.jon-skills/design/references/` by default. One file per reference, recording what was taken, what was rejected, and the audience it came from. New captures go to the personal store unless asked to ship. When a task needs the store (not only a named live URL or paste), `design-inspiration` confirms a session working set via `store-selection.md` before opening captures: seed, then default personal, then an alternate folder only if the user names the path. Merge and override apply to that task only and do not change files on disk. Both stores sit above the conventions in `patterns.md`. When the accepted set is thin or needs a gallery-driven refresh, `curate-design-inspiration` confirms scope, deduplicates against authorized locations, and writes new personal entries.

Accessibility splits three ways rather than being one pass: a linter catches the static mistakes, `axe` in CI catches the computed ones, and only what neither can see reaches a human review. `frontend-craft` carries that split, and `design-review` refuses to spend attention on anything the first two tiers should have gated.

### Process

These skills sit on the Process axis. `align-first` is model-invoked and runs once per non-trivial task through the routing block. `investigate-product`, `plan-delivery`, `retro`, and `diagram` are the Defines level. See [Coverage](#coverage).

- **align-first** (model-invoked): restate the ask, name the assumptions you would otherwise make silently, surface only the branches whose answers change the work, then continue under stated defaults rather than blocking. Escalates into a bounded interview when that pass does not land, with the declared branch list as its budget.
- **investigate-product** (user-invoked): investigate the product and user problem before any solution is designed. Output is a short problem brief.
- **plan-delivery** (user-invoked): sequence a set of asks into phases by value versus effort, with a thin first slice and clear cut lines.
- **diagram** (model-invoked): choose the right diagram for what is being explained and render it.
- **retro** (user-invoked): turn a finished delivery into durable, owned changes that feed the next plan.

Some things are deliberately left out:

- a `bug-hunting` and a `quality` review skill, because Claude Code ships `/code-review` and `/simplify`. On another harness you may want an equivalent; this can change later
- an `item estimation` skill lives inside the `plan-delivery` one

## Coverage

Folders are how the pack is authored. `foundation/`, `engineering/`, `design/`, and `process/` stay. The map below is how those skills cover an engineering job. It follows the five axes in [Engineering Ladders](https://github.com/jorgef/engineeringladders): Technology, System, People, Process, and Influence. A level on an axis is cumulative. This pack does not ship one skill per Developer, Tech Lead, or manager level. A ladder is which axes a role leans on. Developer leans Technology and System. Tech Lead leans System at Owns, Evolves, and Leads. A technical program manager leans Process. Engineering management is out of scope.

`align-first` stays model-invoked. It is the Challenges move on Process, and it runs on tasks that never touch code. The routing block's first row is the delivery channel: once per non-trivial task, then proceed under the stated assumption. It is not a session-long output style. A persistent mode would apply it to a typo, which the skill tells you to skip.

| Axis | Covered | Not in this pack |
| --- | --- | --- |
| Technology | Adopts to Masters: `resolve-conventions`, `ts-standards`, `create`, `project-shape`, `frontend-craft`, `forms`, `state-management`, `api-design`, `design-tokens`, `dependency-choice`, `perf-audit`, `security-hardening` | Creates: a new technology used by other teams |
| System | Enhances to Evolves: `create`, `refactor`, `forms`, `frontend-craft`, `api-design`, `project-shape`, `design-brief`, `information-architecture`, `design-inspiration`, `curate-design-inspiration`, `design-review`, `observability`, `ship-flow`, `verify-before-done`, `migration`, `release-flow` | Leads. `project-shape` classifies a repo that exists. `create` scaffolds a unit inside one. An empty-repo bootstrap, a skill that records an architecture decision, and an incident or mitigation skill are not shipped. |
| Process | Follows to Defines: `testing-strategy`, `verify-before-done`, `ship-flow`, `align-first`, `agent-instructions`, `investigate-product`, `plan-delivery`, `retro`, `diagram` | A deeper team-process design than `plan-delivery` and `retro` |
| People | | Mentoring, career conversations, and engineering management. A review skill is omitted because Claude Code ships `/code-review`. |
| Influence | `release-flow`, an artifact other teams can consume | Community reach, which is personal content rather than this pack |

The three System gaps worth a later skill are an empty-repo bootstrap, an architecture-decision record, and incident mitigation. This change does not add them, and it does not add People skills or one skill per ladder level.

The routing block stays a short moment table, read every turn once a repo opts in. The rows name recurring moments only. A new or changed surface reaches `design-brief` before components. `investigate-product`, `plan-delivery`, and `retro` stay off that table: they are user-invoked, so a line there would ask for a slash command on every coding task.

## Optional companions

This pack is self-contained: nothing here requires another plugin to work. A few skills are better with company, and where that is true they name the companion rather than assuming it is installed.

| Want | Where it lives |
| --- | --- |
| A standalone session that grills a plan you already have | `grill-me` and `grill-with-docs` in [mattpocock/skills](https://github.com/mattpocock/skills). `align-first` here runs one cheap pass every time and escalates into a bounded interview when that pass does not land, which covers the same ground from the other end |
| A deeper test-driven discipline | `obra/superpowers` and `mattpocock/skills` both ship one. `testing-strategy` here carries the loop well enough to work alone |
| Extracting a token set from a live site | [arvindrk/extract-design-system](https://github.com/arvindrk/extract-design-system), which `design-inspiration` points at rather than reimplementing |
| Building and stress-testing a domain model | `domain-modeling` in [mattpocock/skills](https://github.com/mattpocock/skills). `agent-instructions` here covers what a `CONTEXT.md` should contain |

Claude Code's own `/code-review`, `/simplify`, `/run` and `dataviz` are referenced in a few places and ship with that harness. On Codex, Cursor or Gemini you will want an equivalent, and the skills that mention them say so rather than depending on them.

## What is verified where

Only Claude Code has been measured, and `evals/RESULTS.md` records what was tested, what was not, and what failed. Three things carry over:

- **A model-invoked skill was never reached for on its own** across eleven runs, on two models. The pack works around this three ways: wiring the important gates into skills that do fire, offering to write a verification rule into the repo's `AGENTS.md`, and offering a routing block in the same file that maps the recurring moments of a task to the skill that owns each. The first has eval evidence behind it. The second and third rest on the same reasoning (a file read every turn reaches the model, a description does not) and neither has been measured yet.
- **Cross-skill chaining** (`Call the Skill tool with "..."`) is Claude Code phrasing. Whether another harness acts on it is untested, so elsewhere treat each skill as self-contained.
- **Nothing in `design/`, and no frontend skill, has an eval.** Eight skills now cover that territory on reasoning alone. `design-review` is the only one whose output is structured enough to score objectively, so it is the one to measure first.

User-invoked skills (`setup-skills`, `align-first` aside, plus `investigate-product`, `plan-delivery`, `retro`) rely on `disable-model-invocation`, a Claude Code key, plus `policy.allow_implicit_invocation: false` for OpenAI-style hosts. A harness honouring neither may reach for them on its own, which matters most for `investigate-product`, since it is forbidden from proposing a solution and would derail a coding task.

## Prior art

What this pack learned from. Each is worth reaching for directly when you want something narrower, more opinionated or more complete: this one is deliberately small and vendor-neutral, and that is a trade rather than a claim to be better.

| Repo | What it is | Why you would reach for it |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | A full methodology as composable skills: brainstorm, plan, worktree, subagent execution, TDD, review | You want the process to own the whole loop. Its `verification-before-completion` is the ancestor of `verify-before-done` |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 25 engineering skills mapped to a lifecycle, with personas and reference checklists | You want breadth. `security-hardening`, `observability` and `ship-flow` all go deeper there |
| [mattpocock/skills](https://github.com/mattpocock/skills) | A senior TypeScript workflow built around grilling the user until the ask is understood | You want a full interview. `align-first` here is the light version, not a replacement |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's own: document formats, artifacts, MCP builder, skill-creator | You need a document or an artifact. This pack does not go near those |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Forces the laziest solution that works, with intensity levels and a published benchmark | You want the anti-over-engineering stance always on. The YAGNI ladder in `create` is a narrow version of its ladder |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Karpathy's notes on LLM coding pitfalls as behavioral rules | You want one short file rather than a skill set. Its ideas are spread across `create`, `refactor` and `verify-before-done` |
| [educlopez/ui-craft](https://github.com/educlopez/ui-craft) | A design engineering system: one skill over 34 references covering heuristics, inspiration, motion, forms, recipes | You want depth on a specific surface. Its scored critique is the ancestor of `design-review`, its pattern analysis of `design-inspiration` |
| [julianoczkowski/designer-skills](https://github.com/julianoczkowski/designer-skills) | A nine-skill design pipeline: brief, IA, tokens, build, review, tasks | You want the design process driven end to end. The phase split in `design/` follows its shape |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design intelligence as searchable data: styles, palettes, font pairings, UX guidelines | You are doing real visual design. `frontend-craft` sets a direction; this has the reference library |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Anti-slop frontend for landing pages and portfolios, driven by a design read and three dials | You are building marketing surfaces. The read and dials in `design-brief` come from here |
| [arvindrk/extract-design-system](https://github.com/arvindrk/extract-design-system) | Extracts colours, type, spacing, radii and shadows from any public site into `tokens.json` and `tokens.css` | You want a real starting token set. `design-inspiration` points here rather than reimplementing it |
| [feature-sliced/skills](https://github.com/feature-sliced/skills) | Official Feature-Sliced Design v2.1: layers, slices, public API boundaries, import rules | You want one prescriptive frontend architecture. Note it carries no licence |
| [humanlayer/skills](https://github.com/humanlayer/skills) | A small set including `improve-claude-md` and agentic control-loop builders | You want an agentic loop. `agent-instructions` owes its conditional-rule idea to `improve-claude-md` |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Cuts token use hard by stripping the agent's prose | Long sessions where output volume is the cost |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Shapes output for action: next step first, state restated, no preamble | You want answers you can act on. Pick one of this and caveman, not both |
| [blader/humanizer](https://github.com/blader/humanizer) | Removes the structural tells of AI writing | You are shipping prose: docs, posts, release notes |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | A curated list of skills and tools | You are looking for something specific and want to search before building it |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | An agent harness performance system: skills, instincts, memory, security | You want to change the harness itself, not just add skills |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | An agent framework built to grow with its user | You are building a custom agent rather than extending one |

Links verified 2026-09. Star counts are omitted, since they are stale the day they are written.

## Philosophy

Detect before you decide. Recommend before you impose. Ask before you assume. Prove before you claim.

Small, composable skills that defer to the project in front of them, so they stay useful across personal and company codebases instead of fighting whatever is already there.

## Repo layout

- `skills/` grouped into `foundation/`, `engineering/`, `design/` and `process/`. `docs/` holds human-facing pages for user-invoked skills only.
- `evals/` the test harness and its findings. `RESULTS.md` records what has and has not been measured, including what failed.
- `scripts/validate.py` the checks: frontmatter parses, names match folders, guardrails present, cross-references and relative links resolve, manifests in sync, no undeclared external skill, and markdown style holds. `.githooks/pre-commit` runs it before a commit; `.github/workflows/validate.yml` runs it on push and pull request plus a weekly link check.
- `.agents/conventions.md` how to write and extend a skill here. `AGENTS.md` instructions for an agent working on this repo, not for consumers.
- `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/` (marketplace) plus `plugins/jon/` (Cursor plugin), `gemini-extension.json` one manifest per harness, kept in sync by the validator. `GEMINI.md` is the context file the Gemini extension loads.

```bash
pip install pyyaml
git config core.hooksPath .githooks   # once per clone
python3 scripts/validate.py           # offline, fast
python3 scripts/validate.py --links   # also resolves external URLs
```

Skip the hook for one commit with `git commit --no-verify`. Without pyyaml the validator still runs, reports that frontmatter is only partially checked, and CI covers the rest.

No Node toolchain here on purpose, and no markdown formatter: the repo is markdown, YAML and two scripts, so there is no JavaScript to lint, and a formatter was measured against it and rejected (384 lines changed across 24 files while every measurable axis was already uniform). The style is checked instead of rewritten; the reasoning is in [`.agents/conventions.md`](.agents/conventions.md).
