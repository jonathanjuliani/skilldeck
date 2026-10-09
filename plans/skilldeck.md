# skilldeck (rename of `jonathanjuliani/skills`)

The engineering skills repo becomes the `skilldeck` marketplace. One plugin, the one that already exists at `plugins/skilldeck/`. The hub at `jonathanjuliani/skilldeck` is renamed to `skilldeck-hub` and archived in phase 2, after these manifest edits are on `main`. Do not copy this tree into the hub, and do not delete the hub.

## Current state

36 skills under `plugins/skilldeck/skills/<bucket>/<name>/SKILL.md`. Root `skills` is a symlink to that directory. Frontmatter is valid today: `scripts/validate.py` requires `name` and `description`, and `name` must match the folder. CI is `.github/workflows/validate.yml` (push, pull request, Monday link check) and `.github/workflows/release.yml` (tag `v*` creates a GitHub Release). Tags `v0.1.0` through `v0.1.4`. Version `0.1.4` is copied by `scripts/version.py` into:

- `.claude-plugin/plugin.json`
- `plugins/skilldeck/.cursor-plugin/plugin.json`
- `.codex-plugin/plugin.json`
- `gemini-extension.json`
- the `skilldeck` entry in `.claude-plugin/marketplace.json`

| File | Role today |
| --- | --- |
| `.claude-plugin/marketplace.json` | Marketplace name `skills`. One plugin `skilldeck`, `source` `./` |
| `.claude-plugin/plugin.json` | Plugin name `skilldeck`. Explicit `skills` array of 36 paths. `homepage` and `repository` are `github.com/jonathanjuliani/skills` |
| `.cursor-plugin/marketplace.json` | Name `skilldeck-skills`, `pluginRoot` `plugins`, plugin source `skilldeck` |
| `plugins/skilldeck/.cursor-plugin/plugin.json` | Same skill list as Claude. Real files, because Cursor rejects a symlink that leaves the plugin directory |
| `.codex-plugin/plugin.json` | Name `skilldeck`, `skills` `./skills/`, `interface` block. No `.agents/plugins/marketplace.json` |
| `gemini-extension.json` | Name `skilldeck-skills`, `contextFileName` `GEMINI.md` |
| `scripts/install-cursor.sh` | Copies the one plugin into `~/.cursor/plugins/local` |
| `scripts/build-openai-plugin.py` | Flattens `skills/<bucket>/<name>` into `dist/openai/jon` for a ChatGPT import zip |

No `.github/plugin/`, no root `plugin.json`, no `CONTRIBUTING.md`, no issue or PR templates, no `CODEOWNERS`. No `.devin-plugin/` in this release.

README and `docs/pack/install.md` tell people to install `skills@skilldeck` from the hub, or `npx skills add jonathanjuliani/skills`. Codex commands point at the hub. Cursor GitHub import points at `jonathanjuliani/skills`.

License: MIT (`LICENSE`). Changelog: `CHANGELOG.md`.

User-facing strings that stay: `.skilldeck-skills/`, `skilldeck-skills:` markers in the setup blocks, `~/.skilldeck-skills/design/references/`, and the slash prefix `/skilldeck:`.

## Gaps

- Marketplace `name` is `skills` (Claude) and `skilldeck-skills` (Cursor). The target name is `skilldeck`, which the hub already uses. The plugin name stays `skilldeck`, so the install id becomes `skilldeck@skilldeck`.
- Claude `source` `./` is legal for Claude and rejected by Cursor. Cursor already uses `plugins/skilldeck`. Keep that split.
- Codex has a plugin manifest at the repo root and no repo marketplace file, so `codex plugin marketplace add` cannot point at this repo.
- Copilot, VS Code, and Antigravity have no confirmed install against this repo. Devin is skills-only: `npx skills add … -a devin`. Do not add `.devin-plugin/plugin.json`.
- Gemini is one extension for the whole repo. Set its `name` to `skilldeck`. Do not expand it.
- `npx skills add` already walks `skills/<bucket>/<name>/SKILL.md` through the root symlink. Leave that symlink. Do not move skill folders.
- Install docs, badges, and `homepage` fields say `jonathanjuliani/skills` or the hub.
- No contribution surface: template, issue forms, PR template, `CODEOWNERS`, `good first skill` label.
- `scripts/validate.py` hard-codes the Cursor marketplace name `skilldeck-skills`.

## Phases

### Phase 1 — One marketplace name, same GitHub repo

Goal: this repo is a marketplace named `skilldeck` with the existing plugin and relative sources. Claude, Codex, Cursor, and Gemini still install. Skill folders do not move. GitHub is still `jonathanjuliani/skills`.

Depends on: none

Tasks:

- [x] `.claude-plugin/marketplace.json`: set `name` to `skilldeck`. Keep one plugin, `name` `skilldeck`, `source` `./`. Add `renames` so the hub's plugin name `skills` points at `skilldeck`. Confirm the field against [Host a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace) while editing. If the doc's shape does not match, leave `renames` out and record that in the phase note. Do not guess a second field.
- [x] `.cursor-plugin/marketplace.json`: set `name` to `skilldeck`. Keep `metadata.pluginRoot` `plugins` and the one bare `source` `skilldeck`. No `./` prefix.
- [x] `plugins/skilldeck/.codex-plugin/plugin.json`: move the root `.codex-plugin/plugin.json` here. `name` stays `skilldeck`. `skills` stays `./skills/` (that directory is `plugins/skilldeck/skills`). Keep a short `interface.displayName`. Delete the root file.
- [x] `.agents/plugins/marketplace.json`: `name` `skilldeck`, one plugin, `source.path` `./plugins/skilldeck`.
- [x] `gemini-extension.json`: set `name` to `skilldeck`. Leave `contextFileName` `GEMINI.md`.
- [x] `scripts/validate.py`: require marketplace `name` `skilldeck` in the Claude, Cursor, and Codex marketplace files; require Cursor `source` `skilldeck`; require the root `skills` symlink to `plugins/skilldeck/skills`; require `plugins/skilldeck/skills` to be a real directory. Error text includes the file path. Do not require extra plugin directories.
- [x] `scripts/version.py` and `scripts/test_version.py`: the Codex manifest path is now `plugins/skilldeck/.codex-plugin/plugin.json`. Still one version across the files the script already owns.
- [x] `scripts/install-cursor.sh`: still copies the one plugin into `~/.cursor/plugins/local/skilldeck`. Copy, do not symlink.
- [x] Do not add `plugins/foundation/`, `plugins/engineering/`, `plugins/design/`, or `plugins/process/`. Do not delete `plugins/skilldeck/` or the root symlink. Do not add `.devin-plugin/plugin.json`.

Acceptance criteria:

- `python3 scripts/validate.py` passes.
- `claude plugin marketplace add ./` then `claude plugin install skilldeck@skilldeck` installs the pack. A new session exposes `/skilldeck:setup-skills`. There is no second plugin.
- `codex plugin marketplace add ./` lists one plugin whose `source.path` is `./plugins/skilldeck`.
- `./scripts/install-cursor.sh` leaves a real directory at `~/.cursor/plugins/local/skilldeck`, and Cursor shows the 36 skills after a reload.
- `npx skills add ./ --list` prints all 36 skills.
- `gemini extensions install <path-to-clone>` still loads `GEMINI.md`. The extension name is `skilldeck`.

Docs to update: `docs/pack/resources.md` if it names the Cursor marketplace `skilldeck-skills` or the root Codex path. Install commands wait for phase 4. Both are done. `docs/pack/install.md` only had its Codex path corrected. Install commands are unchanged.

Checked on 2026-10-09, still on GitHub `jonathanjuliani/skills`:

- `python3 scripts/validate.py`, `python3 scripts/test_version.py`, and `python3 scripts/version.py --check` passed. `claude plugin validate .` passed, including `renames`.
- The host doc's `renames` example maps a removed plugin to `null`. This marketplace maps `skills` to `skilldeck` and `skillverse` to `null`.
- `claude plugin marketplace add ./ --scope local` then `claude plugin install skilldeck@skilldeck` installed one plugin. That add retargeted the existing marketplace named `skilldeck` (the hub). The install was removed and the marketplace was pointed back at `jonathanjuliani/skilldeck`. A new session was not left open, so `/skilldeck:setup-skills` was not observed.
- `npx skills add ./ --list` printed 36 skills.
- `codex` and `gemini` are not on PATH. Those two acceptance commands were skipped.
- The OpenAI package build requires the output directory to be named `skilldeck`. CI and `scripts/test-openai-package.py` were still using `jon`.

Risk / rollback: revert the branch. `main` is untouched until merge, so current users are unaffected. Do not tag.

### Phase 2 — Rename the GitHub repo and archive the hub

Goal: `github.com/jonathanjuliani/skilldeck` is this repo. The hub lives on as `skilldeck-hub`, archived. Old `skills` URLs redirect. Users are told once.

Depends on: phase 1 merged to `main`

Tasks:

- [x] Working tree clean on `main`, including the local edits already in this clone, so the rename is not mixed with unrelated diffs.
- [x] `npm deprecate @jonathanjuliani/skilldeck`. The owner deleted the package. `npm view` returns 404.
- [x] Hub repo: rename `jonathanjuliani/skilldeck` to `jonathanjuliani/skilldeck-hub`. Archive it. Replace `README.md` with the same migration paragraph. Do not delete the repo.
- [x] This repo: GitHub Settings → rename `skills` to `skilldeck`. Do not create a repository named `skills` afterwards.
- [x] Local clone: `git remote set-url origin git@github.com:jonathanjuliani/skilldeck.git`.
- [x] Every `https://github.com/jonathanjuliani/skills` in manifests, `CHANGELOG.md` link definitions, `docs/`, `README.md`, and `GEMINI.md`: change to `https://github.com/jonathanjuliani/skilldeck`. `GEMINI.md` had no such URL. `scripts/version.py` writes the changelog links, so its `REPO` constant moved too.
- [x] `private-skills` blob link in `plugins/jon/skills/personal-design-refs/references/README.md`: update after the redirect responds. That edit is in the other repo; it is not a skilldeck release. The old blob redirects to `skills/design/...`, which is a symlink and returns 404. The link now targets `plugins/skilldeck/skills/design/design-inspiration/references/duolingo.md`.

Acceptance criteria:

- `https://github.com/jonathanjuliani/skills` redirects to `https://github.com/jonathanjuliani/skilldeck` and the page is this repo (36 skills, one plugin).
- `https://github.com/jonathanjuliani/skilldeck-hub` is archived and its README does not offer `skills@skilldeck` as a current install.
- `npm view @jonathanjuliani/skilldeck` shows the deprecation message.
- `claude plugin marketplace add jonathanjuliani/skilldeck` registers a marketplace whose `name` is `skilldeck` and whose plugin is `skilldeck`.
- `npx skills add jonathanjuliani/skills --list` still lists the skills, through the redirect.

Docs to update: a short "Moved from `skills`" note at the top of `README.md` only. Full install page is phase 4. `CHANGELOG.md` `## [Unreleased]` records the rename.

Risk / rollback: GitHub can rename this repo back to `skills` only if nothing else has claimed `skilldeck`. Do not archive `skilldeck-hub` until `jonathanjuliani/skilldeck` answers as this repo. If the rename of `skills` fails because the name is still taken, the hub rename did not finish. Stop. Do not create a second repo, and do not delete the hub.

### Phase 3 — Other platforms and the shared check

Goal: Copilot, VS Code, Antigravity, and Gemini are tried against the one plugin. The reusable workflow exists on `main`. Devin is not given a plugin manifest.

Depends on: phase 2

Tasks:

- [x] Antigravity: do not add a second `plugin.json`. Run `agy plugin install ./plugins/skilldeck`. If `agy` rejects the manifest, record the error in `docs/install.md` and keep `npx skills add` as the path. Do not fork the schema to guess. `agy` is not on PATH (2026-10-09). The note is in `docs/pack/install.md`, which is the install page until phase 4 moves it to `docs/install.md`.
- [x] Copilot: from a clone, `copilot plugin marketplace add ./`. If the Claude marketplace is picked up, do not add `.github/plugin/marketplace.json`. If it is not, add that file with one entry, `source` `./`, and make `scripts/validate.py` fail when the two marketplace files differ. `copilot` is not on PATH. The extra marketplace file was not added.
- [x] VS Code: do not flatten `skills/<bucket>/<name>`. If `chat.plugins.marketplaces` lists the repo and the skills do not appear, record which file VS Code read and that nested folders were not discovered. The Claude and Cursor skill lists stay the supported install. User settings do not list the repo, so the skill list was not observed.
- [x] `.github/workflows/marketplace-check.yml`: `on: workflow_call`. Checkout the caller into `caller/`, checkout `jonathanjuliani/skilldeck` at the tag being released into `skilldeck/`, run a new `scripts/marketplace_check.py` against `caller/`. The script checks frontmatter `name` and `description`, manifest JSON, and that each relative `source` is a real plugin directory. Print `path: reason` on failure.
- [x] `.github/workflows/validate.yml`: run `scripts/marketplace_check.py` on this repo so the shared check and the full validator both run.
- [x] `scripts/version.py`: include any new manifest that has `version`. No new versioned manifest. `.github/plugin/marketplace.json` was not added.
- [x] Do not add `.devin-plugin/plugin.json`. The install doc tells Devin users to run `npx skills add jonathanjuliani/skilldeck -a devin`.

Acceptance criteria:

- `copilot plugin marketplace browse skilldeck` lists one plugin named `skilldeck`, or the verification note explains which extra file was required.
- `agy plugin install ./plugins/skilldeck` either installs or the rejection is written down. No invented fields.
- A pull request with a marketplace `source` of `./plugins/missing` fails the check with that path in the log.
- The workflow file is on `main` before `v1.0.0`. Skillverse does not reference it in this release.
- No `.devin-plugin/` directory exists.

Docs to update: `docs/pack/resources.md` lists the new workflow. Install commands wait for phase 4.

Risk / rollback: delete the workflow file. Platform files that fail validation are reverted. Already-supported installs use the phase 1 files and keep working.

### Phase 4 — Front door, migration, contribution

Goal: a person or an agent can install from the README and from `docs/install.md`, and can add a skill without reading the validator source.

Depends on: phase 2. Can be written against phase 1 on the branch and published in the same tag as phase 5.

Tasks:

- [x] `README.md`: what skilldeck is; one plugin row (name `skilldeck`, one-line description, version); install commands grouped as native plugin, Team, and skills-only fallback; how to update; how a release is cut; link to `CONTRIBUTING.md`; "Moved from `skills`" with the old id `skills@skilldeck` and the new id `skilldeck@skilldeck`; "Also from skilldeck: skillverse" linking to `https://github.com/jonathanjuliani/skillverse`. No hub command and no `@jonathanjuliani/skilldeck`. Devin's line is `npx skills add jonathanjuliani/skilldeck -a devin`. The version in the table is `0.1.4`. Phase 5 has to change that row when it bumps the manifests. `version.py` does not edit the README.
- [x] `docs/install.md`: the agent page. State the tool, then the commands. An agent fetches `https://raw.githubusercontent.com/jonathanjuliani/skilldeck/main/docs/install.md`. Move the long per-harness detail out of `docs/pack/install.md` into this file, and leave `docs/pack/install.md` as a pointer, or replace it in place if the pack index should stay at `docs/pack/`. Pick one URL and use it in the README. Do not keep two install pages that can drift. Slash commands in that page stay `/skilldeck:…`. `npx skills` stays `/setup-skills`.
- [x] `docs/pack/skills.md`, `docs/pack/coverage.md`, `docs/pack/inspirations.md`, `docs/foundation/setup-skills.md`, `docs/process/*.md`: keep `/skilldeck:` for a plugin install. Say that `npx skills` stays unscoped. There is no `docs/process/align-first.md` or `diagram.md`.
- [x] `skills/foundation/setup-skills/routing-block.md` and `verification-block.md`: marker prefix `skilldeck-skills:` stays.
- [x] `CONTRIBUTING.md`: the shape is `plugins/skilldeck/skills/<bucket>/<name>/SKILL.md`, with `plugins/skilldeck/skills/engineering/debug/` as the example. Required frontmatter. Run `python3 scripts/validate.py`. Link `.agents/conventions.md`. The four bucket folders stay; they are not four plugins.
- [x] `.github/ISSUE_TEMPLATE/skill.yml`: name, bucket (`foundation`, `engineering`, `design`, `process`), when it should run.
- [x] `.github/PULL_REQUEST_TEMPLATE.md`: which bucket, validator run, changelog line under `## [Unreleased]`.
- [x] `.github/CODEOWNERS`: `* @jonathanjuliani`.
- [x] Label `good first skill`: `gh label create "good first skill" --description "A new skill inside the skilldeck plugin"`. Mention it in `CONTRIBUTING.md`.
- [x] `CHANGELOG.md`: under `## [Unreleased]`, the id change from `skills@skilldeck` to `skilldeck@skilldeck`, the rename, and the removed hub install.
- [x] Search the repo for `jonathanjuliani/skills`, `skilldeck-skills`, `npx skills add jonathanjuliani/skills`, and `@jonathanjuliani/skilldeck`. Each hit is updated or listed as an intentional keep (`.skilldeck-skills` is a keep). `skills@skilldeck` remains only in the migration note. Keeps: past changelog sections, `plans/`, `CONTEXT.md`, skill files that name `.skilldeck-skills/` or `skilldeck-skills:` markers, and `evals/RESULTS.md`.

Acceptance criteria:

- The install commands in `README.md` use `skilldeck@skilldeck` and do not use `@jonathanjuliani/skilldeck`. The migration section is the only place that shows `skills@skilldeck`.
- `README.md` does not contain `jonathanjuliani/skills` except inside the "Moved from `skills`" note, which states the redirect.
- Fetching `docs/install.md` is enough to install on Claude Code without opening another file.
- A new skill folder that is not in the plugin's skill list fails `python3 scripts/validate.py` with the folder path in the message.
- `CODEOWNERS` and both templates are on `main`.

Docs to update: the files in the tasks above.

Risk / rollback: docs only, plus templates. Revert the commit. Install behavior does not change.

### Phase 5 — Release 1.0.0 and the Cursor listing

Goal: one breaking release. The install id changes. Marketplace clients see a new version. Cursor is submitted once, for this one plugin.

Depends on: phases 2, 3, and 4

Tasks:

- [x] `python3 scripts/version.py major` on clean `main`. Version becomes `1.0.0` in every manifest the script owns. Tag `v1.0.0`. The README version row was set to `1.0.0` in the parent commit, because `version.py` does not edit the README.
- [x] `git push --follow-tags`. `.github/workflows/release.yml` opens the GitHub Release from the changelog section. The body includes the migration commands: remove marketplace `skilldeck` if it was the hub, add `jonathanjuliani/skilldeck`, install `skilldeck@skilldeck`. Also give `skillverse@skillverse` for anyone who had installed Skillverse from the hub. Release: https://github.com/jonathanjuliani/skilldeck/releases/tag/v1.0.0
- [x] Pin a GitHub issue "Moved from skills" with those same commands for Claude, Codex, and Cursor. https://github.com/jonathanjuliani/skilldeck/issues/2
- [x] Submit `https://github.com/jonathanjuliani/skilldeck` at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish). One plugin. Further re-index requests only on minor or major tags. Do not submit skillverse in this batch. On 2026-10-09 the page said "Sign in to apply" and had no form. The submission was not filed. That note is on the GitHub Release.
- [x] After the tag exists, confirm `https://www.skills.sh/jonathanjuliani/skilldeck` (and the old `/skills` path). If the old path 404s and the new path is empty, the listing is populated by the skills CLI's own index, not by a file in this repo. Record the URL in `docs/install.md`. Do not add a skills.sh config file; none is documented. Both URLs returned 404 on 2026-10-09. The URL is recorded in `docs/install.md`.

Acceptance criteria:

- `python3 scripts/version.py --check v1.0.0` passes on the tag.
- The GitHub Release body tells a hub user to install `skilldeck@skilldeck`, not four plugins, and not `skills@skilldeck`.
- `claude plugin marketplace update skilldeck` on a machine that had the hub offers `1.0.0`. If the old plugin `skills` is still what update offers, remove and add, then install `skilldeck@skilldeck`.
- `/skilldeck:setup-skills` still runs.
- The Cursor submission is filed, or a dated note in the release says the form was unavailable.

Docs to update: release notes are the changelog section. `docs/pack/resources.md` already describes `version.py`; adjust the Codex manifest path if phase 1 moved it. The Codex path was already updated in phase 1.

Risk / rollback: tags are not moved. A bad release is a `v1.0.1` fix. Yanking `v1.0.0` on GitHub does not roll back clones that already updated. Cursor listing can be pulled by the publisher if a review finds a problem.

Checked on 2026-10-09:

- `python3 scripts/version.py --check v1.0.0` passed on the tag. Validate and release workflows on `v1.0.0` succeeded.
- The GitHub Release body tells a hub user to install one plugin, `skilldeck@skilldeck`, and `skillverse@skillverse` from `jonathanjuliani/skillverse`. It records that `skills@skilldeck` is retired.
- `claude plugin marketplace update skilldeck` recloned this repo. The marketplace entry is plugin `skilldeck` version `1.0.0`. This machine still has marketplace `skills` at `jonathanjuliani/skills.git` and `jon@skills` 0.1.0 enabled, so `skilldeck@skilldeck` was not installed here.
- `/skilldeck:setup-skills` was not started in a new session.
- The Cursor publish page required sign-in. The dated note is on the release.
