#!/usr/bin/env python3
"""Tests for scripts/marketplace_check.py. Stdlib only; run from anywhere."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "marketplace_check.py"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def run(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(root)],
        check=False,
        capture_output=True,
        text=True,
    )


def skill(root: Path, name: str = "debug") -> None:
    write(
        root / "plugins" / "skilldeck" / "skills" / "engineering" / name / "SKILL.md",
        textwrap.dedent(
            f"""\
            ---
            name: {name}
            description: Find a cause.
            ---

            Body.
            """
        ),
    )


class MarketplaceCheckTest(unittest.TestCase):
    def test_this_repo_passes(self) -> None:
        result = run(ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")

    def test_missing_source_names_the_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill(root)
            write(
                root / ".claude-plugin" / "plugin.json",
                json.dumps({"name": "skilldeck"}),
            )
            write(
                root / ".claude-plugin" / "marketplace.json",
                json.dumps(
                    {
                        "name": "skilldeck",
                        "plugins": [
                            {"name": "skilldeck", "source": "./"},
                            {"name": "missing", "source": "./plugins/missing"},
                        ],
                    }
                ),
            )
            result = run(root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("./plugins/missing: not a directory", result.stdout)

    def test_name_must_match_folder(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill(root, "debug")
            write(
                root / "plugins" / "skilldeck" / "skills" / "engineering" / "debug" / "SKILL.md",
                textwrap.dedent(
                    """\
                    ---
                    name: other
                    description: Find a cause.
                    ---

                    Body.
                    """
                ),
            )
            write(root / ".claude-plugin" / "plugin.json", json.dumps({"name": "skilldeck"}))
            write(
                root / ".claude-plugin" / "marketplace.json",
                json.dumps({"name": "skilldeck", "plugins": [{"name": "skilldeck", "source": "./"}]}),
            )
            result = run(root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("name is 'other', folder is 'debug'", result.stdout)


if __name__ == "__main__":
    unittest.main()
