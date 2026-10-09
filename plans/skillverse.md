# skillverse

Skillverse stays `jonathanjuliani/skillverse`. It is already its own Claude Code marketplace. This release stops telling people to install it through the skilldeck hub. The npm package stays `@jonathanjuliani/skillverse`. No new `SKILL.md`. No Codex, Cursor, Copilot, or Devin manifest. Skillverse does not call skilldeck's shared workflow until a skill exists.

## Current state

A Claude Code plugin (function hooks, its own pane), a CLI (`bin/skillverse.mjs`), a localhost web app (`server/`, `web/`), and a terminal UI (`tui/`). There is no `SKILL.md`. Leave that as it is.

| File | Role today |
| --- | --- |
| `.claude-plugin/marketplace.json` | Name `skillverse`. One plugin, `source` `./`, `version` `0.2.4` |
| `.claude-plugin/plugin.json` | Name `skillverse`, `version` `0.2.4`, `repository` `https://github.com/jonathanjuliani/skillverse`. No root `plugin.json` |
| `package.json` | `@jonathanjuliani/skillverse`, `bin.skillverse`, `publishConfig.access` `public`. `version` script runs `scripts/sync-version.mjs` |
| `.github/workflows/ci.yml` | Push to `main` and pull requests: pnpm, version check, Biome, Vitest, Claude plugin validate, plugin tests, pack and `skillverse run` |
| `.github/workflows/release.yml` | Tag `v*`: check, test, `npm publish --provenance`, GitHub Release |
| `docs/how-it-works.md` | What it reads and that it stays on the machine |
| `docs/install.md`, `docs/develop.md`, `docs/use.md` | Install, dev, use |

Tags `v0.2.0` through `v0.2.4`. npm registry is `0.2.3`, so the latest tag did not publish. The release job needs `secrets.NPM_TOKEN`.

README install path 2 is `npm i -g @jonathanjuliani/skilldeck` then `skilldeck install skillverse`, which installs `skillverse@skilldeck` from the hub. `docs/install.md` repeats it. `AGENTS.md` and `.jon-skills/config.yaml` mention `jonathanjuliani/skills` as the personal defaults pack.

No Cursor, Codex, Copilot, Devin, or Gemini manifest. No `CONTRIBUTING.md`, issue templates, PR template, or `CODEOWNERS`. License: MIT.

Privacy, already written in `docs/how-it-works.md`: skill files and the session transcript are read locally; writes go to `~/.cache/skillverse/`; the server binds `127.0.0.1` and answers only `localhost` and `127.0.0.1`; live events stay in memory; hooks send skill names, a session id, and a project folder name, not prompts or file contents. The page loads graph libraries from jsDelivr.

## Gaps

- The README still offers the hub. After skilldeck phase 2 that command installs nothing useful.
- `npx skills add jonathanjuliani/skillverse` finds no `SKILL.md`. That stays true this release. The README says so instead of pretending the command works.
- Collaboration files are missing.
- The registry is one release behind the tag. The next release has to prove publish works.
- `AGENTS.md` and `.jon-skills/config.yaml` still name `jonathanjuliani/skills`.

## Not in this release

- A `SKILL.md`, a version pin inside a skill, or `disable-model-invocation`.
- Root `plugin.json`, `.agents/plugins/marketplace.json`, `.cursor-plugin/`, `.codex-plugin/`, `.devin-plugin/`, `.github/plugin/marketplace.json`, or `gemini-extension.json`.
- A job that `uses` `jonathanjuliani/skilldeck/.github/workflows/marketplace-check.yml`.
- A Cursor marketplace submission. The public listing would be a skill plugin, and there is no skill yet.

The Claude marketplace already has `source` `./`. That is the plugin install.

## Phases

### Phase 1 — Docs off the hub

Goal: install instructions use this repo and npm only. The plugin and the CLI are unchanged.

Depends on: skilldeck phase 2 (hub archived as `skilldeck-hub`)

Tasks:

- [x] `README.md`: what it does; privacy (local reads, `127.0.0.1`, no prompts leaving the machine, jsDelivr for the page) with a link to `docs/how-it-works.md`; install by marketplace (`/plugin marketplace add jonathanjuliani/skillverse`, `/plugin install skillverse@skillverse`) and by npm (`npm i -g @jonathanjuliani/skillverse`); how to run `skillverse run` and `skillverse open`; link to `docs/develop.md`; release is a tag; link back to `https://github.com/jonathanjuliani/skilldeck`. One sentence that `npx skills add jonathanjuliani/skillverse` is not available until this repo has a skill. Delete the `@jonathanjuliani/skilldeck` / `skilldeck install skillverse` block.
- [x] `docs/install.md`: the same two routes, plus the update commands that already exist (`/plugin marketplace update skillverse`, `npm update -g @jonathanjuliani/skillverse`). Remove the hub. This is the file an agent fetches from raw GitHub. Repeat the sentence that `npx skills` waits on a skill.
- [x] `docs/how-it-works.md`: keep the current privacy section. Do not add a skill row.
- [x] `docs/develop.md`: state that a release tags `main`, publishes npm, and opens a GitHub Release. Do not document a skill path or a version pin.
- [x] `AGENTS.md` and `.jon-skills/config.yaml`: `jonathanjuliani/skills` becomes `jonathanjuliani/skilldeck` after that rename. Personal defaults still live in that pack. The config parenthetical is now `plugin skilldeck`.
- [x] `CHANGELOG.md`: under `## [Unreleased]`, hub removal. Do not claim a new skill or new manifests.
- [x] Search for `skilldeck install`, `skillverse@skilldeck`, and `@jonathanjuliani/skilldeck`. Remove them. The 0.2.1 changelog bullet was reworded so it no longer names that command.

Acceptance criteria:

- `README.md` and `docs/install.md` contain no hub install.
- `README.md` states that usage data stays on the machine and links to `docs/how-it-works.md`.
- `docs/install.md` includes marketplace and npm commands, and `skillverse run`. It says `npx skills add` does not install this repo yet.
- `find . -name SKILL.md -not -path './node_modules/*'` prints nothing.
- `.claude-plugin/marketplace.json` still has one plugin, `source` `./`.

Docs to update: the files in the tasks above.

Risk / rollback: docs only. The published Claude install is unchanged. Revert the commit.

### Phase 2 — Collaboration

Goal: a pull request has a template, an owner, and a place to ask for a change. There is still no skill to template.

Depends on: phase 1

Tasks:

- [x] `CONTRIBUTING.md`: how to change the plugin, the CLI, or the docs. Run `pnpm run lint && pnpm test && pnpm run validate`. The pane code in `hooks/register.tsx` has its own rules in `AGENTS.md`. Link them. State that a new skill is out of scope until a later release, so this file does not include a `SKILL.md` template.
- [x] `.github/ISSUE_TEMPLATE/config.yml` and a bug or change template (what broke, which surface: pane, web app, or CLI).
- [x] `.github/PULL_REQUEST_TEMPLATE.md`: what changed, which commands were run, changelog line under `## [Unreleased]`.
- [x] `.github/CODEOWNERS`: `* @jonathanjuliani`.
- [x] `gh label create "good first skill" --description "A change to skillverse docs or a future skill"`. Mention it in `CONTRIBUTING.md` as a label for doc fixes. Do not file a skill issue as the example.

Acceptance criteria:

- `CODEOWNERS` and the PR template are on `main`.
- `CONTRIBUTING.md` does not tell the reader to create `skills/skillverse/SKILL.md`.
- `pnpm test` still passes. These files are not imported by the app.

Docs to update: `CONTRIBUTING.md`, and a one-line link from `README.md` if it does not already point at it.

Risk / rollback: delete the new files. No runtime change.

### Phase 3 — Release

Goal: npm and the Claude marketplace version match. No Cursor submission.

Depends on: phase 1. Phase 2 can land in the same release or the one after.

Tasks:

- [x] Confirm `NPM_TOKEN`. If `v0.2.4` never reached npm, do not retag it. Re-run the failed release run with `gh run rerun`, or cut `v0.2.5` from `main` once the doc changes are in. `gh workflow run` does not apply to a `push` tag trigger. `NPM_TOKEN` is set. `v0.2.4` was only a local tag. `git push --follow-tags` also pushed it; that release run was cancelled and the remote tag was deleted before npm showed `0.2.4`.
- [x] `pnpm version patch` (or `minor` if the changelog warrants it) on clean `main`. `scripts/sync-version.mjs` keeps `package.json`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` on one version. Push with `--follow-tags`. The unreleased section already had new commands that had never reached npm, so the bump is minor: `0.3.0`. Release: https://github.com/jonathanjuliani/skillverse/releases/tag/v0.3.0
- [x] `.github/workflows/release.yml`: no change to the trigger. It already runs `node scripts/sync-version.mjs --check`.
- [x] Do not submit this repo at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish) in the skilldeck batch. Not submitted.

Acceptance criteria:

- `npm view @jonathanjuliani/skillverse version` equals the new tag and `package.json`.
- `npx @jonathanjuliani/skillverse@<version> --help` runs.
- `/plugin marketplace update skillverse` reports that version.
- `npm view @jonathanjuliani/skilldeck` is the deprecated hub, not a publish from this repo.
- There is still no `SKILL.md`.

Docs to update: the changelog section for the release.

Risk / rollback: npm publish is not easily undone. Deprecate a bad version. Do not unpublish if anything has installed it. Marketplace rollback is a newer patch tag.

Checked on 2026-10-09, from `main`. `feat/agent-views` (pull request 2) was left as it was.

- `pnpm run lint` and `pnpm test` passed before the release (63 tests).
- `node scripts/sync-version.mjs --check v0.3.0` passed on the tag. The release workflow succeeded.
- `npm view @jonathanjuliani/skillverse version` is `0.3.0`. `npx @jonathanjuliani/skillverse@0.3.0 --help` printed the usage.
- `claude plugin marketplace update skillverse` offers plugin `skillverse` `0.3.0`, source `./`.
- `npm view @jonathanjuliani/skilldeck` is 404. Nothing from this repo published that name.
- `find . -name SKILL.md` printed nothing. Cursor was not submitted.
