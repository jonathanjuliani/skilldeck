#!/usr/bin/env python3
"""Validate Manus .skill archives without changing the canonical skills or the OpenAI package."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import subprocess
import sys
import tempfile
import zipfile

import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILDER = ROOT / "scripts" / "build-manus-skills.py"
OPENAI_BUILDER = ROOT / "scripts" / "build-openai-plugin.py"
OPENAI_TEST = ROOT / "scripts" / "test-openai-package.py"
SOURCE_SKILLS = ROOT / "plugins" / "skilldeck" / "skills"
BUNDLE_NAME = "skilldeck-manus.zip"
FORBIDDEN_ARCHIVE_NAMES = {".DS_Store", "__pycache__"}
USER_INVOKED = {
    "setup-skills",
    "survey-structure",
    "retro",
    "plan-delivery",
    "investigate-product",
}
VERIFY_FROM = (
    'Call the Skill tool with "resolve-conventions" to learn the project\'s '
    "test runner, type checker, linter, and build"
)
VERIFY_TO = (
    'Apply the installed skill "resolve-conventions" now: read its instructions and '
    "follow them. If it is not installed, say so in one line and continue. Use it to "
    "learn the project's test runner, type checker, linter, and build"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Manus skill archives.")
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument(
        "--skip-determinism",
        action="store_true",
        help="Skip rebuilding twice and comparing the resulting archives.",
    )
    return parser.parse_args()


def load_frontmatter(text: str, label: str) -> dict:
    if not text.startswith("---\n"):
        raise AssertionError(f"{label} has no YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise AssertionError(f"{label} has unclosed YAML frontmatter")
    payload = yaml.safe_load(parts[1])
    if not isinstance(payload, dict):
        raise AssertionError(f"{label} frontmatter must be a mapping")
    return payload


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(SOURCE_SKILLS.rglob("*")):
        if path.is_file():
            hashes[str(path.relative_to(SOURCE_SKILLS))] = sha256(path)
    if not hashes:
        raise AssertionError("no canonical skill files found")
    return hashes


def source_skill_names() -> set[str]:
    names: set[str] = set()
    for path in SOURCE_SKILLS.glob("*/*/SKILL.md"):
        name = load_frontmatter(path.read_text(encoding="utf-8"), str(path)).get("name")
        if name in names:
            raise AssertionError(f"duplicate source skill name: {name}")
        names.add(name)
    return names


def read_skill(archive: pathlib.Path) -> tuple[str, str]:
    with zipfile.ZipFile(archive) as bundle:
        members = bundle.namelist()
        roots = {pathlib.PurePosixPath(member).parts[0] for member in members}
        if roots != {archive.stem}:
            raise AssertionError(f"{archive.name} must contain one {archive.stem!r} root")
        for member in members:
            parts = pathlib.PurePosixPath(member).parts
            if any(part in FORBIDDEN_ARCHIVE_NAMES or part.endswith(".pyc") for part in parts):
                raise AssertionError(f"{archive.name} contains forbidden file: {member}")
            if "openai.yaml" in parts or "agents" in parts:
                raise AssertionError(f"{archive.name} still contains harness metadata: {member}")
        skill_md = f"{archive.stem}/SKILL.md"
        if skill_md not in members:
            raise AssertionError(f"{archive.name} lacks {skill_md}")
        text = bundle.read(skill_md).decode("utf-8")
    return text, "\n".join(members)


def validate_output(output: pathlib.Path) -> None:
    output = output.resolve()
    archives = sorted(output.glob("*.skill"))
    expected = source_skill_names()
    found = {archive.stem for archive in archives}
    if found != expected:
        missing = sorted(expected - found)
        extra = sorted(found - expected)
        raise AssertionError(f"skill inventory mismatch, missing={missing}, extra={extra}")

    bundle = output / BUNDLE_NAME
    if not bundle.is_file():
        raise AssertionError(f"missing download bundle {BUNDLE_NAME}")
    with zipfile.ZipFile(bundle) as packed:
        packed_names = set(packed.namelist())
    if packed_names != {archive.name for archive in archives}:
        raise AssertionError("download bundle is not exactly the .skill files")

    for archive in archives:
        text, members = read_skill(archive)
        frontmatter = load_frontmatter(text, archive.name)
        if frontmatter.get("name") != archive.stem:
            raise AssertionError(f"{archive.name} names itself {frontmatter.get('name')!r}")
        if "Call the Skill tool with" in text:
            raise AssertionError(f"{archive.name} still tells Manus to call the Skill tool")
        if archive.stem in USER_INVOKED:
            if "disable-model-invocation: true" not in text.split("---\n", 2)[1]:
                raise AssertionError(f"{archive.name} dropped disable-model-invocation")
            if f"Run only after the user typed `/{archive.stem}`." not in text:
                raise AssertionError(f"{archive.name} lacks the user-invoked gate")
        if archive.stem in {"design-inspiration", "curate-design-inspiration"}:
            if "A missing `~/.skilldeck-skills` directory is expected." not in text:
                raise AssertionError(f"{archive.name} lacks the design-store note")

    verify = (output / "verify-before-done.skill")
    verify_text, _members = read_skill(verify)
    if VERIFY_TO not in verify_text:
        raise AssertionError("verify-before-done was not rewritten as specified")
    if "## On Manus" in verify_text:
        raise AssertionError("verify-before-done gained a host block it does not need")

    setup_text, _members = read_skill(output / "setup-skills.skill")
    if "skills/foundation/resolve-conventions/defaults.yaml" in setup_text:
        raise AssertionError("setup-skills still points at the plugin-relative defaults path")
    if 'Read `defaults.yaml` from the installed skill "resolve-conventions".' not in setup_text:
        raise AssertionError("setup-skills defaults read was not rewritten")
    if "Writing `AGENTS.md` or `CLAUDE.md` does not install skills on Manus." not in setup_text:
        raise AssertionError("setup-skills lacks the Manus install note")

    with zipfile.ZipFile(output / "design-inspiration.skill") as bundle:
        if "design-inspiration/store-selection.md" not in bundle.namelist():
            raise AssertionError("design-inspiration dropped a companion")
    with zipfile.ZipFile(output / "record-decision.skill") as bundle:
        record = bundle.read("record-decision/SKILL.md").decode("utf-8")
    if 'and with "project-shape"' in record:
        raise AssertionError("record-decision left the second skill call untranslated")
    if 'Then apply the installed skill "project-shape" now:' not in record:
        raise AssertionError("record-decision did not split the second skill into its own step")

    print(f"Manus package validation passed: {len(archives)} skills")


def assert_sources_unchanged(before: dict[str, str]) -> None:
    after = source_hashes()
    if after != before:
        changed = sorted(set(before) ^ set(after) | {key for key in before if before.get(key) != after.get(key)})
        raise AssertionError(f"canonical skill files changed: {changed}")
    verify = (SOURCE_SKILLS / "engineering" / "verify-before-done" / "SKILL.md").read_text(encoding="utf-8")
    if VERIFY_FROM not in verify:
        raise AssertionError("canonical verify-before-done lost the Skill tool phrase")
    setup = (SOURCE_SKILLS / "foundation" / "setup-skills" / "SKILL.md").read_text(encoding="utf-8")
    if "disable-model-invocation: true" not in setup:
        raise AssertionError("canonical setup-skills lost disable-model-invocation")
    if "Call the Skill tool with" not in setup:
        raise AssertionError("canonical setup-skills lost the Skill tool phrase")


def assert_openai_package_still_differs() -> None:
    if "retains Claude-only frontmatter" not in OPENAI_TEST.read_text(encoding="utf-8"):
        raise AssertionError("OpenAI package test no longer rejects disable-model-invocation")
    with tempfile.TemporaryDirectory(prefix="skilldeck-openai-untouched-") as temporary:
        output = pathlib.Path(temporary) / "skilldeck"
        subprocess.run(
            [
                sys.executable,
                str(OPENAI_BUILDER),
                "--output",
                str(output),
                "--no-archive",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        generated = (output / "skills" / "setup-skills" / "SKILL.md").read_text(encoding="utf-8")
        verify = (output / "skills" / "verify-before-done" / "SKILL.md").read_text(encoding="utf-8")
    if "disable-model-invocation: true" in generated:
        raise AssertionError("OpenAI package kept disable-model-invocation on setup-skills")
    if VERIFY_FROM not in verify:
        raise AssertionError("OpenAI package rewrote the Skill tool phrase")


def validate_determinism() -> None:
    with tempfile.TemporaryDirectory(prefix="skilldeck-manus-determinism-") as temporary:
        temporary_root = pathlib.Path(temporary)
        hashes = []
        for label in ("first", "second"):
            output = temporary_root / label
            subprocess.run(
                [sys.executable, str(BUILDER), "--output", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            digest = hashlib.sha256()
            for path in sorted(output.iterdir()):
                digest.update(path.name.encode())
                digest.update(path.read_bytes())
            hashes.append(digest.hexdigest())
        if hashes[0] != hashes[1]:
            raise AssertionError("two clean builds produced different Manus archives")
    print("Deterministic Manus build validation passed")


def main() -> None:
    args = parse_args()
    before = source_hashes()
    validate_output(args.output)
    assert_sources_unchanged(before)
    assert_openai_package_still_differs()
    assert_sources_unchanged(before)
    if not args.skip_determinism:
        validate_determinism()
        assert_sources_unchanged(before)


if __name__ == "__main__":
    main()
