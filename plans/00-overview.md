# Self-contained marketplaces: skilldeck and skillverse

Planning date: 2026-10-09. Revised the same day. This is a plan only. No repo was renamed, and no package was published.

Two public repos, each its own marketplace. No hub, no vendored copy of one repo inside the other, and no file sync between them. The only cross-repo link is a sentence in the skilldeck README.

| Repo | Role | Marketplace `name` | Install id |
| --- | --- | --- | --- |
| `jonathanjuliani/skilldeck` (rename of `jonathanjuliani/skills`) | 36 engineering skills, one plugin | `skilldeck` | `skilldeck@skilldeck` |
| `jonathanjuliani/skillverse` | Token and skill usage: Claude Code plugin, CLI, local web app. npm package `@jonathanjuliani/skillverse` | `skillverse` | `skillverse@skillverse` |

The published npm package is `@jonathanjuliani/skillverse` (registry 0.2.3; local tag `v0.2.4`).

## Decisions

- One plugin, named `skilldeck`, holding all 36 skills in the current buckets. No split into `foundation`, `engineering`, `design`, or `process` plugins.
- No domain. Install URLs are `github.com/jonathanjuliani/…`.
- Rename path: archive the hub as `jonathanjuliani/skilldeck-hub`, deprecate `@jonathanjuliani/skilldeck`, then rename `jonathanjuliani/skills` to `jonathanjuliani/skilldeck`. Do not copy the skills tree into the hub, and do not delete the hub.
- Unscoped npm name `skilldeck` stays unpublished.
- Skillverse gets no new `SKILL.md` in this release. The Claude plugin and the CLI stay as they are. `npx skills add jonathanjuliani/skillverse` waits until a skill exists.
- Devin, this release: `npx skills add jonathanjuliani/skilldeck -a devin` only. No `.devin-plugin/plugin.json`.

Slash commands stay `/skilldeck:setup-skills`. The config directory stays `.skilldeck-skills/`. The old hub id `skills@skilldeck` is the migration note, not the new install command.

## Target state

```text
skilldeck/                              skillverse/
  .claude-plugin/marketplace.json         .claude-plugin/marketplace.json
  .cursor-plugin/marketplace.json         .claude-plugin/plugin.json
  .agents/plugins/marketplace.json        bin/ cli/ server/ web/ hooks/
  plugins/skilldeck/
    .cursor-plugin/plugin.json
    .codex-plugin/plugin.json
    skills/<bucket>/<name>/SKILL.md
  skills -> plugins/skilldeck/skills
```

Every marketplace `source` is a path inside that same repo. Claude keeps `source` `./` (the root `.claude-plugin/plugin.json`). Cursor keeps a bare `source` of `skilldeck` under `metadata.pluginRoot` `plugins`. Codex uses `source.path` `./plugins/skilldeck`. No `github` source object.

Skill folders stay nested: `plugins/skilldeck/skills/<bucket>/<name>/SKILL.md`. Do not flatten them. Agent Plugins 1.0 discovers `skills/<name>/SKILL.md` one level down ([specification](https://agent-plugins.org/specification)). Whether a client also sees `<bucket>/<name>` is checked in [verification](verification.md). Claude and Cursor keep the explicit skill lists that already work.

## What exists today

Three repos, one of them a hub:

| Repo | What it is | Marketplace | Plugins |
| --- | --- | --- | --- |
| [`jonathanjuliani/skills`](https://github.com/jonathanjuliani/skills) | The 36 skills. 29 commits. Tags `v0.1.0` through `v0.1.4`. Default branch `main` | `.claude-plugin/marketplace.json` name `skills`. Cursor marketplace name `skilldeck-skills` | One plugin, `skilldeck`, source `./` (Claude) and `plugins/skilldeck` (Cursor). Root `skills` is a symlink to `plugins/skilldeck/skills` |
| [`jonathanjuliani/skilldeck`](https://github.com/jonathanjuliani/skilldeck) | Hub plus npm `@jonathanjuliani/skilldeck` (registry 0.1.3, local tag `v0.1.4`). 9 commits, 0 stars | Claude marketplace name `skilldeck` | External sources: `jonathanjuliani/skills` as plugin `skills`, `jonathanjuliani/skillverse` as plugin `skillverse`. Cursor marketplace is an empty list |
| [`jonathanjuliani/skillverse`](https://github.com/jonathanjuliani/skillverse) | Plugin, CLI, web app, terminal app. Tag `v0.2.4`. No `SKILL.md` | Claude marketplace name `skillverse`, source `./` | One Claude plugin. No Cursor, Codex, Copilot, or Devin manifest |

Published install lines point at the hub: `/plugin install skills@skilldeck` and `skilldeck install skills`. Cursor is documented against `jonathanjuliani/skills`, with a warning not to also add the hub.

`skills.sh` has no listing: `https://www.skills.sh/jonathanjuliani/skills` returns 404. Re-check after the rename; there is nothing to move.

Copying the skills tree into the hub is the harder path. GitHub redirects `jonathanjuliani/skills` only when that repo is renamed, and the rename is blocked while the hub owns `skilldeck`. A copy either squashes blame into one commit or force-pushes over the hub, and still leaves `jonathanjuliani/skills` with no redirect. The skills history is the one worth keeping.

## Platform matrix

Checked 2026-10-09. "Manifest" is the file to plan. Required fields are only those the linked doc states.

| Platform | Surface | Manifest | Required fields | Doc | Notes |
| --- | --- | --- | --- | --- | --- |
| Claude Code | CLI, desktop, VS Code extension | `.claude-plugin/marketplace.json` plus `.claude-plugin/plugin.json` | Marketplace: `name`, `owner`, `plugins[]` with `name` and `source`. Relative `source` starts with `./`, or a bare directory name when `metadata.pluginRoot` is set. `"."` is the repo root | [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace), [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference) | Add with `/plugin marketplace add jonathanjuliani/skilldeck` or `claude plugin marketplace add ./path`. Host docs describe a top-level `renames` map: [Host a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace). Use it so hub plugin `skills` points at `skilldeck`, after confirming the field shape |
| Codex and ChatGPT desktop | CLI and desktop | Repo marketplace `.agents/plugins/marketplace.json`. Compatibility manifest `.codex-plugin/plugin.json` | Marketplace entry `source.path` is a `./` path relative to the repo root. Plugin scaffold sets `skills` to `./skills/` | [Package your plugin](https://developers.openai.com/plugins/build/plugins) | `codex plugin marketplace add owner/repo` and `codex plugin marketplace add ./path`. The skills repo has a root `.codex-plugin/plugin.json` and no `.agents/plugins/marketplace.json`. Move the manifest to `plugins/skilldeck/.codex-plugin/plugin.json` so `source.path` `./plugins/skilldeck` finds it |
| Cursor | Desktop and CLI | `.cursor-plugin/marketplace.json` and `plugins/skilldeck/.cursor-plugin/plugin.json` | Marketplace: `name`, `plugins[]` with `name` and `source`. `source` is a path from the repo root or a URL. `owner.name` when `owner` is present | [Plugins](https://cursor.com/docs/plugins), [marketplace schema](https://raw.githubusercontent.com/cursor/plugins/main/schemas/marketplace.schema.json) | This repo already uses `metadata.pluginRoot: "plugins"` and a bare `source` (`"skilldeck"`). A root `source` of `"."` or `"./"` was reported as silently rejected after Cursor 2.6 ([forum](https://forum.cursor.com/t/team-marketplace-refresh-failing-since-mar-7-worked-fine-until-mar-6-public-repo-no-github-app-connected/154643/9)). Keep the bare name. Local load is a copy into `~/.cursor/plugins/local/skilldeck`, not a symlink. Public listing: [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish), open source, permissive license, every update re-reviewed ([publisher terms](https://cursor.com/marketplace-publisher-terms)) |
| GitHub Copilot | CLI, VS Code, Copilot app | `.github/plugin/marketplace.json`, and Copilot also looks in `.claude-plugin/marketplace.json` | Marketplace: `name`, `owner`, `plugins[]` with `name` and `source` (repo-relative path or URL) | [Creating a marketplace](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace), [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) | `copilot plugin marketplace add jonathanjuliani/skilldeck`. Do not add a second marketplace file until a local add misses the Claude file |
| VS Code | Desktop | Root `plugin.json` with the Agent Plugins `$schema`, if a client needs it. Marketplace via `chat.plugins.marketplaces` | `$schema` `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`, `name`. Skills come from `skills/` | [Agent plugins in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-plugins) | `"chat.plugins.enabled": true` (default true). **UNVERIFIED:** which marketplace filename VS Code reads when several exist, and whether it sees `skills/<bucket>/<name>/SKILL.md`. Confirm in [verification](verification.md). Do not flatten the tree to satisfy this |
| Agent Plugins 1.0 | Portable layer | `plugin.json` at the plugin root. Closed schema | `$schema` as above, `name`. Optional: `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, `extensions` | [Specification](https://agent-plugins.org/specification), [Manifest](https://agent-plugins.org/plugin-authors/manifest) | Claude-only keys stay in `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. Add a root `plugin.json` only where a platform will not read the Claude manifest. Nested skill folders stay |
| Antigravity | `agy` CLI and desktop | `plugin.json` in the plugin directory, or skills via `.agents/skills` | `name` (required for the CLI). Optional `description`. Documented `$schema`: `https://antigravity.google/schemas/v1/plugin.json`. The published schema sets `additionalProperties: false` | [Plugins](https://antigravity.google/docs/plugins/), [Skills](https://antigravity.google/docs/skills/) | Try `agy plugin install ./plugins/skilldeck`. The named marketplace only accepts `antigravity-plugins-official`. **UNVERIFIED:** whether the existing Claude `plugin.json` (or an Agent Plugins file) is accepted. If it is rejected, the install doc says so and points at `npx skills`. Do not invent a second schema |
| Gemini CLI | CLI, legacy | `gemini-extension.json` at the repo root | The skills repo already ships `name`, `description`, `version`, `contextFileName` | [Gemini CLI shutdown for individual accounts](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), [agy migration](https://antigravity.google/docs/cli/gcli-migration/) | Individuals stopped being served on 2026-06-18. Enterprise and paid API keys still work. Keep one extension file. Set `name` to `skilldeck`. Do not build a new Gemini surface |
| Windsurf | Desktop | Skills only | `SKILL.md` with `name` and `description` | [vercel-labs/skills](https://github.com/vercel-labs/skills) | `npx skills add jonathanjuliani/skilldeck -a windsurf` |
| OpenCode | CLI, desktop beta | Skills only | same | same | `-a opencode` |
| Devin | CLI, Desktop, cloud | None this release | — | [vercel-labs/skills](https://github.com/vercel-labs/skills) | `npx skills add jonathanjuliani/skilldeck -a devin` writes `.devin/skills/` or `~/.config/devin/skills/`. No `.devin-plugin/plugin.json` |

## Rename checklist

| Check | Result | Consequence |
| --- | --- | --- |
| GitHub `jonathanjuliani/skills` | Public, `main`, 29 commits, the skills repo | Rename this to `skilldeck` after the hub has moved. GitHub redirects the old URL. Do not create a new repo named `skills` afterwards ([Renaming a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)) |
| GitHub `jonathanjuliani/skilldeck` | Public, the hub, 9 commits, 0 stars | Rename it to `skilldeck-hub` and archive it. Do not delete it. Deleting drops the GitHub releases and does not redirect `jonathanjuliani/skills` |
| GitHub `jonathanjuliani/skillverse` | Public, stays | No rename |
| npm `skilldeck` (unscoped) | 404, name is free | Leave it unpublished |
| npm `@jonathanjuliani/skilldeck` | Published 0.1.3. Local tag `v0.1.4` is ahead of the registry | `npm deprecate` with a migration message. Do not reuse the name for a new CLI |
| npm `@jonathanjuliani/skillverse` | Published. Local tag `v0.2.4`, registry 0.2.3 | Keep. Next release should confirm `NPM_TOKEN` actually publishes |
| Domain | Out of scope | No domain is registered or linked from these repos |

Cutover order, so users migrate once:

1. Land the marketplace name change and the Codex marketplace file on `main` of `skills` while the GitHub name is still `skills`. One plugin. Skill folders stay put.
2. `npm deprecate @jonathanjuliani/skilldeck`.
3. Rename `jonathanjuliani/skilldeck` to `jonathanjuliani/skilldeck-hub`. Archive it. README: one paragraph pointing at the two real repos.
4. Rename `jonathanjuliani/skills` to `jonathanjuliani/skilldeck`. That claims the name and replaces the temporary redirect to `skilldeck-hub`.
5. Leave `jonathanjuliani/skills` unused forever.

After step 4, `https://github.com/jonathanjuliani/skills` redirects to skilldeck. `https://github.com/jonathanjuliani/skilldeck` is this repo. Update the local remote: `git remote set-url origin git@github.com:jonathanjuliani/skilldeck.git`. The directory name on disk can stay `skills`.

Breaking ids:

| Before | After |
| --- | --- |
| `skills@skilldeck` from the hub | `skilldeck@skilldeck`. `renames.skills` set to `skilldeck` if the host doc confirms the field |
| `skillverse@skilldeck` from the hub | Removed. Install `skillverse@skillverse` |
| `skilldeck@skills` if anyone added this repo's marketplace under its old name | Marketplace name changes from `skills` to `skilldeck`. Remove and add again |
| Cursor marketplace `skilldeck-skills`, plugin `skilldeck` | Marketplace `skilldeck`, same one plugin |
| `/skilldeck:setup-skills` | Unchanged |
| `.skilldeck-skills/` | Unchanged |
| `npx skills add jonathanjuliani/skills` | Still works via the redirect. Docs say `jonathanjuliani/skilldeck` |

Migration text goes in the skilldeck README, the `1.0.0` GitHub Release, and a pinned GitHub issue. Users who already have marketplace `skilldeck` from the hub should remove it and add `jonathanjuliani/skilldeck` again, because Claude identifies a marketplace by `name` and will not hold two checkouts with that name. Update does not rename an installed marketplace.

One link outside these repos: `private-skills` points at a blob on `jonathanjuliani/skills` (`plugins/jon/skills/personal-design-refs/references/README.md`). Update that URL after the redirect exists. It is not part of either marketplace.

## Shared CI

A reusable workflow lives in skilldeck and is pinned to a tag, not `@main`. Skillverse does not call it in this release. It has no `SKILL.md`, and this release does not add one. Call the workflow from skillverse only after a skill exists.

```yaml
# later, in skillverse/.github/workflows/ci.yml, not in this release
marketplace:
  uses: jonathanjuliani/skilldeck/.github/workflows/marketplace-check.yml@v1.0.0
```

The workflow checks out the caller, checks out the pinned skilldeck script beside it, and runs three checks:

- every `SKILL.md` has `name` and `description`, and `name` matches the folder
- each marketplace and plugin manifest parses and contains the required fields for that file
- every `plugins[]` entry's `source` is a relative path to a real directory that contains a plugin manifest

Skilldeck's existing `scripts/validate.py` stays the full check (guardrails, links, word budget, OpenAI package, version sync). The reusable workflow is the small shared slice, in Python, so skilldeck does not grow a Node toolchain. Skilldeck's own `validate.yml` runs the script. Skillverse keeps Biome, Vitest, and `claude plugin test` and does not gain a copy of the script.

Why a called workflow and not a copied template: a template is a second copy. Pin the tag so a bad edit on skilldeck `main` cannot fail a future caller. Skilldeck must stay public.

## Manifest generator

Do not add one.

One plugin and a handful of platform files are small enough to write by hand. The formats disagree on purpose: Cursor wants a bare `source` and `pluginRoot`, Claude wants `./`, Codex wants `source.path`. A generator would encode those exceptions and still need the validator. `scripts/validate.py` already fails when a manifest and a folder disagree. Extend that check. CI fails with the file path and the missing field or folder.

## Releases

A release is a git tag on that repo's `main`. No workflow in one repo tags the other.

| Repo | Bump | Publish |
| --- | --- | --- |
| skilldeck | `python3 scripts/version.py major` writes the same `version` into every manifest that has one, moves `CHANGELOG.md` `## [Unreleased]`, commits, tags `v1.0.0` | `.github/workflows/release.yml` on `v*`: `version.py --check`, `validate.py`, GitHub Release from the changelog section. No npm |
| skillverse | `pnpm version` already syncs `package.json`, `.claude-plugin/plugin.json`, and the marketplace entry via `scripts/sync-version.mjs` | `.github/workflows/release.yml` on `v*`: check, test, `npm publish --provenance --access public`, GitHub Release |

`v1.0.0` on skilldeck is the breaking tag because the install id changes from `skills@skilldeck` to `skilldeck@skilldeck`. Slash commands and `.skilldeck-skills/` do not change. Cursor and Claude only offer an update when `version` changes.

Cursor public listing: submit the one skilldeck plugin once, after `1.0.0`. Do not submit skillverse in that batch. This release does not add a skillverse skill plugin. Re-index skilldeck on minor and major tags, not on every patch. Publisher terms require a re-index request per update, and each update is reviewed again.

Changelogs stay hand-written (`CHANGELOG.md`, Keep a Changelog). The release workflow already turns the matching section into the GitHub Release notes.

When a skillverse skill is added later, pin the CLI it calls to the same version as `package.json` (`npx @jonathanjuliani/skillverse@<version>`). Do not use `@latest`. That pin is not part of this release.

## Overall timeline

| Order | Work | Repo still installs |
| --- | --- | --- |
| 1 | skilldeck phase 1: marketplace name `skilldeck`, Codex marketplace file, one plugin, local installs only | Current `main` unchanged until merge |
| 2 | Merge skilldeck phase 1 to `main`. Tag nothing yet | `npx skills add jonathanjuliani/skills` and `/skilldeck:setup-skills` |
| 3 | skilldeck phase 2: deprecate npm, rename hub to `skilldeck-hub` and archive it, rename this repo | `skilldeck@skilldeck`. Redirect covers `npx skills add jonathanjuliani/skills` |
| 4 | skilldeck phase 3: Copilot, VS Code, Antigravity, Gemini, `marketplace-check.yml` | Claude, Codex, Cursor, Gemini as before |
| 5 | skillverse docs: drop hub install lines. No new skill, no extra manifests, no shared-workflow job | `skillverse@skillverse` and npm |
| 6 | Docs, templates, pinned issue | |
| 7 | skilldeck `v1.0.0` and one Cursor submission | |

## When to upgrade to a central hub

Do not build one now.

Triggers, any one of them:

- a fourth installable repo (these two, plus two more)
- a community listing that must show plugins from several owners
- the same plugin shipped from more than one repo
- a real need to install skilldeck as several plugins instead of one

Migration when that happens: leave each repo's marketplace as it is. Add a new repo whose marketplace entries vendor a copy, or point at a git subtree, of each plugin. Existing `skilldeck@skilldeck` installs keep working. The hub is an extra catalog, not a rename.

The retired `skilldeck-hub` is the counterexample. Its entries used `source.repo` of another GitHub repo. Cursor cannot follow that, which is why the skills pack and the hub drifted apart. A future hub copies bytes. It does not reference the other repo.

## Risks

1. The GitHub name swap is easy to do in the wrong order. Renaming `skills` first fails because `skilldeck` exists. Creating any new repo named `skills` later deletes the redirect.
2. Users who added the hub lose `skillverse@skilldeck` in the same step as `skills@skilldeck`. The pinned issue has to give both new commands. Claude will not install skillverse from the skilldeck marketplace.
3. Cursor public review is manual and per update. A rename that is not yet listed is fine. After listing, a bad patch sits in review.
4. Antigravity and Agent Plugins both want `plugin.json` at the plugin root, with different closed schemas. One file may be rejected by `agy`. Nested `skills/<bucket>/<name>` may be invisible to a client that only reads `skills/<name>/SKILL.md`. The explicit Claude and Cursor lists stay until a check proves otherwise.
5. skillverse tag `v0.2.4` is ahead of npm (0.2.3). The next skillverse release can fail the same way if `NPM_TOKEN` is missing or stale. Skilldeck does not publish npm.
