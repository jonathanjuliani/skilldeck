# Changelog

All notable changes to skilldeck skills are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Add each change under **Unreleased** as you make it; `python3 scripts/version.py` moves them under the new version when you release (see [Releasing](docs/pack/resources.md#releasing)).

## [Unreleased]

## [1.0.3] - 2026-10-30

### Added

- Companions for the failures that show up on any JS/TS product, not a payments or kiosk skill: idempotency on `api-design`, money and transactions on `data-model`, a resilient client and unattended surfaces on `frontend-craft`, and failure-path tests on `testing-strategy`. The case spec is `evals/gap-cases.jsonl`. `evals/run.sh` does not load it.

### Changed

- `ts-standards` states that money is an integer in minor units with a currency.
- `state-management` keeps in-flight work that must survive a reload in session storage, with its idempotency key.
- `security-hardening` names what card data may be stored, and that the full number and the security code may not.
- `design-brief` names an unattended or shared device as a surface kind, with dials. `design-review` asks whether a stranger on that surface can recover alone.
- `bootstrap-repo` states the readme contract for a stranger cloning an app. `verify-before-done` requires a clean-environment run only when the claim is that they can.

## [1.0.2] - 2026-10-21

### Added

- Each GitHub Release includes `skilldeck-openai.zip`, the flat package ChatGPT and OpenAI web import. Codex still reads the bucketed tree.

## [1.0.1] - 2026-10-16

### Added

- The README points at `jonathanjuliani/adhd-focus`, a separate public plugin. It is not part of this pack.
- The README has a Mermaid mind map of every skill, with engineering split into Shape, Build, Quality, and Ship and operate. `scripts/skill_map.py` exports it to `docs/pack/skill-map.svg` for sharing. `validate.py` fails when a skill is missing from the map, filed under the wrong bucket, or the SVG is missing or stale. CI and the pre-commit hook run it.

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

[Unreleased]: https://github.com/jonathanjuliani/skilldeck/compare/v1.0.3...HEAD
[1.0.3]: https://github.com/jonathanjuliani/skilldeck/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/jonathanjuliani/skilldeck/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/jonathanjuliani/skilldeck/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.4...v1.0.0
[0.1.4]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/jonathanjuliani/skilldeck/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/jonathanjuliani/skilldeck/releases/tag/v0.1.0
