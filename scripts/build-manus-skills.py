#!/usr/bin/env python3
"""Build one Manus .skill archive per skilldeck skill.

Reads the canonical skill folders and writes archives under dist/manus/.
Does not edit those folders, the plugin manifests, or the OpenAI package.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import tempfile
import zipfile

import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_SKILLS = ROOT / "skills"
DEFAULT_OUTPUT = ROOT / "dist" / "manus"
BUNDLE_NAME = "skilldeck-manus.zip"
IGNORED_NAMES = {".DS_Store", "__pycache__", "agents"}
USER_INVOKED = {
    "setup-skills",
    "survey-structure",
    "retro",
    "plan-delivery",
    "investigate-product",
}
DESIGN_STORE = {"design-inspiration", "curate-design-inspiration"}
SKILL_CALL = re.compile(r'Call the Skill tool with "([^"]+)"')
AND_WITH = re.compile(r',? and with "([^"]+)"')
SETUP_READ = (
    "Read the personal defaults file at "
    "`skills/foundation/resolve-conventions/defaults.yaml`."
)
SETUP_READ_TO = (
    'Read `defaults.yaml` from the installed skill "resolve-conventions". '
    "If that skill is not installed, say so and stop this step."
)
SETUP_LIVE = (
    "personal defaults live in "
    "`skills/foundation/resolve-conventions/defaults.yaml`."
)
SETUP_LIVE_TO = (
    'personal defaults live in `defaults.yaml` inside the installed skill '
    '"resolve-conventions".'
)
APPLY = (
    'Apply the installed skill "{name}" now: read its instructions and follow them. '
    "If it is not installed, say so in one line and continue."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build one Manus .skill archive per skilldeck skill."
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=DEFAULT_OUTPUT,
        help="Directory for the .skill archives and the download bundle.",
    )
    parser.add_argument(
        "--bundle",
        type=pathlib.Path,
        help="Download bundle of the .skill files. Defaults inside --output.",
    )
    parser.add_argument(
        "--no-bundle",
        action="store_true",
        help="Write the .skill archives without the download bundle.",
    )
    return parser.parse_args()


def load_frontmatter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.relative_to(ROOT)} has no YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError(f"{path.relative_to(ROOT)} has unclosed YAML frontmatter")
    payload = yaml.safe_load(parts[1])
    if not isinstance(payload, dict):
        raise ValueError(f"{path.relative_to(ROOT)} frontmatter must be a mapping")
    return payload


def discover_skills() -> list[tuple[str, pathlib.Path]]:
    discovered: list[tuple[str, pathlib.Path]] = []
    seen: dict[str, pathlib.Path] = {}
    for manifest_path in sorted(SOURCE_SKILLS.glob("*/*/SKILL.md")):
        frontmatter = load_frontmatter(manifest_path)
        name = frontmatter.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"{manifest_path.relative_to(ROOT)} has no skill name")
        if name != manifest_path.parent.name:
            raise ValueError(
                f"{manifest_path.relative_to(ROOT)} names skill {name!r}, "
                f"but its directory is {manifest_path.parent.name!r}"
            )
        if name in seen:
            first = seen[name].relative_to(ROOT)
            second = manifest_path.parent.relative_to(ROOT)
            raise ValueError(f"duplicate skill name {name!r}: {first} and {second}")
        seen[name] = manifest_path.parent
        discovered.append((name, manifest_path.parent))
    if not discovered:
        raise ValueError("no skills found under skills/<category>/<name>/SKILL.md")
    return discovered


def apply_phrase(name: str) -> str:
    return APPLY.format(name=name)


def rewrite_skill_calls(text: str) -> str:
    def replace_call(match: re.Match[str]) -> str:
        following = text[match.end() :]
        bridge = "It" if following.startswith(" has ") else "Use it"
        return f"{apply_phrase(match.group(1))} {bridge}"

    rewritten = SKILL_CALL.sub(replace_call, text)

    def replace_and_with(match: re.Match[str]) -> str:
        phrase = apply_phrase(match.group(1))
        lowered = phrase[0].lower() + phrase[1:]
        return f". Then {lowered} Use it"

    return AND_WITH.sub(replace_and_with, rewritten)


def rewrite_setup_paths(text: str, *, require_both: bool) -> str:
    if require_both and (SETUP_READ not in text or SETUP_LIVE not in text):
        raise ValueError("setup-skills no longer contains the defaults.yaml path sentences")
    rewritten = text.replace(SETUP_READ, SETUP_READ_TO).replace(SETUP_LIVE, SETUP_LIVE_TO)
    if "skills/foundation/resolve-conventions/defaults.yaml" in rewritten:
        raise ValueError("setup-skills still points at the plugin-relative defaults path")
    return rewritten


def host_block(name: str) -> str:
    parts: list[str] = []
    if name in USER_INVOKED:
        parts.append(
            f"Run only after the user typed `/{name}`. "
            "Do not start this skill from a matching description."
        )
    if name == "setup-skills":
        parts.append(
            "Writing `AGENTS.md` or `CLAUDE.md` does not install skills on Manus. "
            "Add skills with Skills, then + Add, then Upload."
        )
    if name in DESIGN_STORE:
        parts.append(
            "A missing `~/.skilldeck-skills` directory is expected. "
            "Use the public `jonathanjuliani/design-references` fallback this skill "
            "already describes. Do not stop to look for a local checkout."
        )
    if not parts:
        return ""
    return "## On Manus\n\n" + "\n\n".join(parts) + "\n"


def insert_host_block(text: str, block: str) -> str:
    if not block:
        return text
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md has no YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError("SKILL.md has unclosed YAML frontmatter")
    body = parts[2][1:] if parts[2].startswith("\n") else parts[2]
    return f"---\n{parts[1]}---\n\n{block.strip()}\n\n{body}"


def transform_tree(skill_root: pathlib.Path, name: str) -> None:
    for path in sorted(skill_root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        rewritten = rewrite_skill_calls(text)
        if name == "setup-skills" and (
            path.name == "SKILL.md"
            or "skills/foundation/resolve-conventions/defaults.yaml" in rewritten
        ):
            rewritten = rewrite_setup_paths(rewritten, require_both=path.name == "SKILL.md")
        if path.name == "SKILL.md":
            rewritten = insert_host_block(rewritten, host_block(name))
        if "Call the Skill tool with" in rewritten:
            raise ValueError(f"{path.name} still tells Manus to call the Skill tool")
        path.write_text(rewritten, encoding="utf-8")


def ignored_copy_entry(_directory: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORED_NAMES or name.endswith(".pyc")}


def safe_rebuild_directory(output: pathlib.Path) -> None:
    output = output.resolve()
    if output == ROOT or output in ROOT.parents:
        raise ValueError(f"refusing to replace unsafe output directory: {output}")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)


def write_deterministic_zip(source: pathlib.Path, archive: pathlib.Path, root_name: str) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(
        archive,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as bundle:
        files = [source] if source.is_file() else sorted(path for path in source.rglob("*") if path.is_file())
        for path in files:
            if source.is_file():
                relative = pathlib.PurePosixPath(path.name)
            else:
                relative = pathlib.PurePosixPath(root_name) / path.relative_to(source)
            info = zipfile.ZipInfo(str(relative), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            bundle.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)


def build_archives(output: pathlib.Path) -> list[pathlib.Path]:
    skills = discover_skills()
    safe_rebuild_directory(output)
    archives: list[pathlib.Path] = []
    with tempfile.TemporaryDirectory(prefix="skilldeck-manus-") as temporary:
        temporary_root = pathlib.Path(temporary)
        for name, source in skills:
            destination = temporary_root / name
            shutil.copytree(source, destination, ignore=ignored_copy_entry)
            transform_tree(destination, name)
            archive = output / f"{name}.skill"
            write_deterministic_zip(destination, archive, name)
            archives.append(archive)
    return archives


def write_bundle(archives: list[pathlib.Path], bundle: pathlib.Path) -> pathlib.Path:
    bundle = bundle.resolve()
    if bundle.parent == ROOT or bundle.parent in ROOT.parents:
        raise ValueError(f"refusing to write the bundle inside the repository root: {bundle}")
    if bundle in {archive.resolve() for archive in archives}:
        raise ValueError("bundle path collides with a .skill archive")
    staging = pathlib.Path(tempfile.mkdtemp(prefix="skilldeck-manus-bundle-"))
    try:
        for archive in archives:
            shutil.copyfile(archive, staging / archive.name)
        write_deterministic_zip(staging, bundle, "")
    finally:
        shutil.rmtree(staging)
    return bundle


def main() -> None:
    args = parse_args()
    output = args.output.resolve()
    archives = build_archives(output)
    print(f"Built Manus skills: {output}")
    print(f"Skills: {len(archives)}")
    if not args.no_bundle:
        bundle = args.bundle or output / BUNDLE_NAME
        write_bundle(archives, bundle)
        print(f"Bundle: {bundle.resolve()}")


if __name__ == "__main__":
    main()
