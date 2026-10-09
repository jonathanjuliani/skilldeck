# Changelog

All notable changes to skilldeck skills are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Add each change under **Unreleased** as you make it; `python3 scripts/version.py` moves them under the new version when you release (see [Releasing](docs/pack/resources.md#releasing)).

## [Unreleased]

## [1.0.0] - 2026-10-09

### Added

- `scripts/marketplace_check.py` checks skill `name` and `description`, marketplace JSON, and that each `source` is a relative plugin directory. CI runs it. Another repo calls `.github/workflows/marketplace-check.yml` pinned to a tag.

### Changed

- The install id is `skilldeck@skilldeck`. The hub install `skills@skilldeck` is retired. The hub repository is archived as `jonathanjuliani/skilldeck-hub`.
- Hub users who still have marketplace `skilldeck` pointed at the archived hub remove it, add this repository, and install one plugin. Claude Code: `/plugin marketplace remove skilldeck`, `/plugin marketplace add jonathanjuliani/skilldeck`, `/plugin install skilldeck@skilldeck`. Codex: `codex plugin marketplace remove skilldeck`, `codex plugin marketplace add jonathanjuliani/skilldeck`, `codex plugin add skilldeck@skilldeck`. Cursor: remove the marketplace that pointed at the hub, then import `https://github.com/jonathanjuliani/skilldeck`.
- Skillverse is a separate repository. Anyone who installed it from the hub adds `jonathanjuliani/skillverse` and installs `skillverse@skillverse`. Codex: `codex plugin marketplace add jonathanjuliani/skillverse`, then `codex plugin add skillverse@skillverse`.
- The GitHub repository is `jonathanjuliani/skilldeck`. `jonathanjuliani/skills` redirects here.
- Claude, Cursor, Codex, and Gemini marketplaces are named `skilldeck`. The install id on this repo is `skilldeck@skilldeck`. The plugin is still the one pack.
- Codex reads `plugins/skilldeck/.codex-plugin/plugin.json` via `.agents/plugins/marketplace.json`.
- Claude `renames` maps the hub plugin `skills` to `skilldeck`, and records that `skillverse` is no longer in this marketplace.

### Fixed

- The OpenAI package build names its output directory `skilldeck`, matching the plugin name. CI was still writing `jon`.
- Cursor GitHub import found no skills. The pack was a symlink out of `plugins/skilldeck`, which Cursor refuses. The files now live in that directory, and `skills/` at the repo root points there.

## [0.1.4] - 2026-10-09

### Changed

- Cursor installs this pack from this repo. The skilldeck marketplace is Claude Code and Codex.

## [0.1.3] - 2026-10-09

### Changed

- Cursor can install this pack from the skilldeck marketplace as well as from this repo.

## [0.1.2] - 2026-10-09

### Changed

- The pack is named skilldeck skills. Config ids, setup markers, and the personal design store use `skilldeck-skills`.
- Claude Code and Codex install this pack from skilldeck as `skills@skilldeck`.
- The README is titled skills and shows the skilldeck marketplace and npm install.
- Setup asks before writing `.skilldeck-skills/config.yaml`. The plugin command is `/skilldeck:setup-skills`.

## [0.1.1] - 2026-10-08

### Added

- Claude Code can install this pack from skilldeck as `skills@skilldeck` (`skilldeck install skills`). It is the same pack as `jon@skills`; pick one.
- One version across the harness manifests, kept in step by `python3 scripts/version.py`, with this changelog and a GitHub Release on the tag.

### Fixed

- The install page says the plugin is all 36 skills, matching the README.

## [0.1.0] - 2026-10-07

Baseline. The manifests already said 0.1.0. History before this file is in git.

[Unreleased]: https://github.com/jonathanjuliani/skilldeck/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.4...v1.0.0
[0.1.4]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/jonathanjuliani/skilldeck/releases/tag/v0.1.0
