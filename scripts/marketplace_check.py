#!/usr/bin/env python3
"""Shared marketplace check. Prints `path: reason` and exits 1 on failure.

    python3 scripts/marketplace_check.py <repo>

Checks every SKILL.md for `name` and `description`, parses marketplace and
plugin manifests, and requires each plugins[].source to be a relative directory
that contains a plugin manifest. Another repo runs this through
.github/workflows/marketplace-check.yml. This repo runs it from validate.yml.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml


SKIP_DIRS = {".git", "node_modules", "dist", "__pycache__"}
PLUGIN_MANIFESTS = (
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "plugin.json",
)
MARKETPLACES = (
    ".claude-plugin/marketplace.json",
    ".cursor-plugin/marketplace.json",
    ".github/plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
)


def fail(errors: list[str], path: str, reason: str) -> None:
    errors.append(f"{path}: {reason}")


def load_json(path: Path, errors: list[str]) -> dict | None:
    rel = str(path)
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        fail(errors, rel, f"invalid JSON ({exc.msg})")
        return None
    if not isinstance(data, dict):
        fail(errors, rel, "manifest must be a JSON object")
        return None
    return data


def skill_files(root: Path) -> list[Path]:
    seen: set[Path] = set()
    found: list[Path] = []
    for path in sorted(root.rglob("SKILL.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        found.append(path)
    return found


def check_skills(root: Path, errors: list[str]) -> None:
    for path in skill_files(root):
        rel = str(path.relative_to(root))
        text = path.read_text()
        if not text.startswith("---\n"):
            fail(errors, rel, "no frontmatter")
            continue
        parts = text.split("---\n", 2)
        if len(parts) < 3:
            fail(errors, rel, "frontmatter is not closed")
            continue
        try:
            frontmatter = yaml.safe_load(parts[1])
        except yaml.YAMLError as exc:
            fail(errors, rel, f"frontmatter is not YAML ({exc})")
            continue
        if not isinstance(frontmatter, dict):
            fail(errors, rel, "frontmatter must be a mapping")
            continue
        name = frontmatter.get("name")
        description = frontmatter.get("description")
        if not isinstance(name, str) or not name.strip():
            fail(errors, rel, "missing name")
        elif name != path.parent.name:
            fail(errors, rel, f"name is {name!r}, folder is {path.parent.name!r}")
        if not isinstance(description, str) or not description.strip():
            fail(errors, rel, "missing description")


def plugin_manifest_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for rel in (
        ".claude-plugin/plugin.json",
        ".cursor-plugin/plugin.json",
        ".codex-plugin/plugin.json",
        "plugin.json",
    ):
        path = root / rel
        if path.is_file():
            paths.append(path)
    for pattern in (
        "plugins/*/plugin.json",
        "plugins/*/.claude-plugin/plugin.json",
        "plugins/*/.cursor-plugin/plugin.json",
        "plugins/*/.codex-plugin/plugin.json",
    ):
        paths.extend(sorted(root.glob(pattern)))
    return paths


def check_plugin_manifests(root: Path, errors: list[str]) -> None:
    for path in plugin_manifest_paths(root):
        rel = str(path.relative_to(root))
        data = load_json(path, errors)
        if data is None:
            continue
        name = data.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(errors, rel, "missing name")


def authored_source(source: object) -> str | None:
    if isinstance(source, str) and source.strip():
        return source
    if isinstance(source, dict):
        path = source.get("path")
        if isinstance(path, str) and path.strip():
            return path
    return None


def has_plugin_manifest(directory: Path) -> bool:
    return any((directory / rel).is_file() for rel in PLUGIN_MANIFESTS)


def check_source(root: Path, source: object, plugin_root: str, errors: list[str]) -> None:
    authored = authored_source(source)
    if authored is None:
        fail(errors, "<source>", "missing relative path")
        return
    if authored.startswith(("/", "\\")) or "://" in authored or authored.startswith("git@"):
        fail(errors, authored, "source is not a relative path")
        return
    if ".." in Path(authored).parts:
        fail(errors, authored, "source leaves the repository")
        return
    if authored in (".", "./"):
        relative = Path()
    elif authored.startswith("./"):
        relative = Path(authored[2:])
    elif plugin_root:
        relative = Path(plugin_root) / authored
    else:
        relative = Path(authored)
    directory = (root / relative).resolve()
    try:
        directory.relative_to(root.resolve())
    except ValueError:
        fail(errors, authored, "source leaves the repository")
        return
    if not directory.is_dir():
        fail(errors, authored, "not a directory")
        return
    if not has_plugin_manifest(directory):
        fail(errors, authored, "no plugin manifest")


def check_marketplaces(root: Path, errors: list[str]) -> None:
    found = [root / rel for rel in MARKETPLACES if (root / rel).is_file()]
    if not found:
        fail(errors, str(root), "no marketplace.json")
        return
    for path in found:
        rel = str(path.relative_to(root))
        data = load_json(path, errors)
        if data is None:
            continue
        name = data.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(errors, rel, "missing name")
        plugins = data.get("plugins")
        if not isinstance(plugins, list):
            fail(errors, rel, "missing plugins")
            continue
        plugin_root = ""
        metadata = data.get("metadata")
        if isinstance(metadata, dict) and isinstance(metadata.get("pluginRoot"), str):
            plugin_root = metadata["pluginRoot"]
        for index, entry in enumerate(plugins):
            if not isinstance(entry, dict):
                fail(errors, rel, f"plugins[{index}] must be an object")
                continue
            plugin_name = entry.get("name")
            if not isinstance(plugin_name, str) or not plugin_name.strip():
                fail(errors, rel, f"plugins[{index}] missing name")
            if "source" not in entry:
                label = plugin_name if isinstance(plugin_name, str) else str(index)
                fail(errors, rel, f"plugin {label!r} has no source")
                continue
            check_source(root, entry.get("source"), plugin_root, errors)


def check(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        fail(errors, str(root), "not a directory")
        return errors
    check_skills(root, errors)
    check_plugin_manifests(root, errors)
    check_marketplaces(root, errors)
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python3 scripts/marketplace_check.py <repo>", file=sys.stderr)
        return 2
    root = Path(argv[1]).resolve()
    errors = check(root)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
