#!/usr/bin/env python3
"""Export the README skill map to docs/pack/skill-map.svg.

The mermaid block between the skill-map markers in README.md is the only
source. This renders it with mermaid-cli through npx, which is the one place
the repo reaches for Node, and only when you run this. The SVG starts with a
hash of the source and theme so validate.py can tell when it is stale without
Node.

Usage: python3 scripts/skill_map.py
"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SVG = ROOT / "docs/pack/skill-map.svg"
BLOCK = re.compile(r"<!-- skill-map:begin -->\n```mermaid\n(.*?)```\n<!-- skill-map:end -->", re.S)
HASH = re.compile(r"<!-- skill-map-source: ([0-9a-f]{64}) -->")
MERMAID_CLI = "@mermaid-js/mermaid-cli@11"

# Tokyo Night, matching Skillverse's web app. The root takes the first slot,
# then the buckets in README order: foundation, design, engineering, process.
BACKGROUND = "#04060c"
ON_ACCENT = "#0b1020"
SECTIONS = ["#c0caf5", "#e0af68", "#bb9af7", "#7aa2f7", "#9ece6a"]
CONFIG = {
    "theme": "base",
    "themeVariables": {
        "darkMode": True,
        "background": BACKGROUND,
        "primaryColor": "#c0caf5",
        "primaryTextColor": ON_ACCENT,
        "lineColor": "#7a83a6",
        **{f"cScale{i}": c for i, c in enumerate(SECTIONS)},
        **{f"cScaleLabel{i}": ON_ACCENT for i in range(len(SECTIONS))},
    },
}


def source(text):
    match = BLOCK.search(text)
    return match.group(1) if match else None


def digest(src):
    return hashlib.sha256((src + json.dumps(CONFIG, sort_keys=True)).encode()).hexdigest()


def main():
    src = source(README.read_text())
    if src is None:
        sys.exit("README.md: no mermaid block between skill-map markers")
    with tempfile.TemporaryDirectory() as tmp:
        mmd, out, cfg = (pathlib.Path(tmp, n) for n in ("map.mmd", "map.svg", "config.json"))
        mmd.write_text(src)
        cfg.write_text(json.dumps(CONFIG))
        subprocess.run(["npx", "-y", MERMAID_CLI, "-i", str(mmd), "-o", str(out),
                        "-c", str(cfg), "-b", BACKGROUND], check=True)
        svg = out.read_text()
    SVG.write_text(f"<!-- skill-map-source: {digest(src)} -->\n{svg.rstrip()}\n")
    print(f"wrote {SVG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
