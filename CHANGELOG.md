# Changelog

All notable changes to skilldeck skills are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Add each change under **Unreleased** as you make it; `python3 scripts/version.py` moves them under the new version when you release (see [Releasing](docs/pack/resources.md#releasing)).

## [Unreleased]

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

[Unreleased]: https://github.com/jonathanjuliani/skills/compare/v0.1.3...HEAD
[0.1.3]: https://github.com/jonathanjuliani/skills/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/jonathanjuliani/skills/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/jonathanjuliani/skills/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/jonathanjuliani/skills/releases/tag/v0.1.0
