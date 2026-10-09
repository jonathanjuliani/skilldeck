# Install

How to install, update, and remove skilldeck.
An agent can install on Claude Code from this file alone.
Back to [skilldeck](../README.md).

Pick one route. A plugin install and `npx skills` together load every skill twice.

A plugin install namespaces commands as `/skilldeck:`. `npx skills` stays unscoped, so setup is `/setup-skills`.

The plugin name is `skilldeck`. The install id is `skilldeck@skilldeck`.

## Claude Code

```text
/plugin marketplace add jonathanjuliani/skilldeck
/plugin install skilldeck@skilldeck
```

Start a new session. Setup is `/skilldeck:setup-skills`. It asks before writing `.skilldeck-skills/config.yaml`, and asks again before it edits anything else.

Scope is **user** (all your projects), **project** (committed, shared), or **local** (this repo, just you).

Update, then start a new session:

```text
/plugin marketplace update skilldeck
/plugin update skilldeck@skilldeck
```

Remove:

```text
/plugin uninstall skilldeck@skilldeck
```

`/plugin disable skilldeck@skilldeck` keeps it installed and stops loading it. `/plugin enable skilldeck@skilldeck` puts it back. The `claude plugin` shell commands do the same and take `--scope`.

## Codex

```bash
codex plugin marketplace add jonathanjuliani/skilldeck
codex plugin add skilldeck@skilldeck
```

The marketplace file is `.agents/plugins/marketplace.json`. The plugin manifest is `plugins/skilldeck/.codex-plugin/plugin.json`, and its skills path is `./skills/` inside that plugin. Codex invokes skills with `@`, so setup is `@setup-skills`.

Update the marketplace from Codex, then start a new session.

## Cursor

GitHub import: Customize → Plugins → From GitHub Repository → `https://github.com/jonathanjuliani/skilldeck`.

Cursor reads `.cursor-plugin/marketplace.json`. The plugin source is the bare name `skilldeck` with `pluginRoot` `plugins`. The skill list is `plugins/skilldeck/.cursor-plugin/plugin.json`, because Cursor does not recurse into bucket folders. The skill files live in that directory. A symlink out of the plugin is refused.

Setup is `/skilldeck:setup-skills`, or `/setup-skills` if Cursor does not namespace.

Local copy, for plugin development: Cursor skips a symlink whose target is outside `~/.cursor/plugins/local`.

```bash
./scripts/install-cursor.sh
```

Quit Cursor and reopen. Enable **Include third-party Plugins, Skills, and other configs**. On Teams or Enterprise, an admin also enables **Allow Local Plugin Imports**.

Team: Dashboard → Plugins → Add Marketplace → Import from Repo → `https://github.com/jonathanjuliani/skilldeck`.

Official listing, after it is published: Customize → Marketplace.

Update by installing again after a version bump. A refresh does not always pick up a new version.

## GitHub Copilot

```bash
copilot plugin marketplace add jonathanjuliani/skilldeck
copilot plugin marketplace browse skilldeck
copilot plugin install skilldeck@skilldeck
```

Copilot looks for `marketplace.json` in `.github/plugin/`, then in `.claude-plugin/`. This repo ships only `.claude-plugin/marketplace.json`, so the two catalogs cannot drift. The plugin source is `./`, and the manifest Copilot loads is `.claude-plugin/plugin.json`. That file lists every skill path. Do not add a root `plugin.json`: Copilot would prefer it over the Claude manifest.

Update:

```bash
copilot plugin marketplace update skilldeck
```

## VS Code

```json
{
  "chat.plugins.enabled": true,
  "chat.plugins.marketplaces": ["jonathanjuliani/skilldeck"]
}
```

Skills stay at `plugins/skilldeck/skills/<bucket>/<name>/SKILL.md`. If the skill list is empty, nested folders were not walked. Claude and Cursor keep their explicit lists. Do not flatten the tree.

## Antigravity

From a clone:

```bash
agy plugin install ./plugins/skilldeck
agy plugin list
```

`plugins/skilldeck/plugin.json` is the Antigravity manifest (`name` and `description` only). Skills in that directory are `skills/<bucket>/<name>/SKILL.md`. Antigravity documents `skills/<name>/SKILL.md`, one level. If `agy plugin list` shows no skills, use `npx skills add jonathanjuliani/skilldeck`. Workspace copies live in `.agents/skills/`.

Do not install the GitHub URL of the repository root. A `plugin.json` there would hide `.claude-plugin/plugin.json` from Copilot.

## Gemini CLI

```bash
gemini extensions install https://github.com/jonathanjuliani/skilldeck
```

The extension name in `gemini-extension.json` is `skilldeck`. It loads `GEMINI.md`.

## Devin

This release has no Devin plugin.

```bash
npx skills add jonathanjuliani/skilldeck -a devin
```

The files land in `.devin/skills/` or `~/.config/devin/skills/`. Setup stays `/setup-skills`.

## Windsurf and OpenCode

```bash
npx skills add jonathanjuliani/skilldeck -a windsurf
npx skills add jonathanjuliani/skilldeck -a opencode
```

Same unscoped commands as any `npx skills` install.

## Skills only, any agent

```bash
npx skills add jonathanjuliani/skilldeck --list
npx skills add jonathanjuliani/skilldeck
npx skills add jonathanjuliani/skilldeck --skill design-review --skill forms
```

There is no category flag. A whole bucket means listing its names. `-g` installs for your user instead of the project. `-a` targets one agent.

Setup is `/setup-skills`. It is not `/skilldeck:setup-skills`.

Remove:

```bash
npx skills list
npx skills remove design-review
npx skills remove --all
```

`remove --all` removes every installed skill from every source, not only this pack.

## skills.sh

The listing URL is [skills.sh/jonathanjuliani/skilldeck](https://www.skills.sh/jonathanjuliani/skilldeck).
On 2026-10-09 that path and [skills.sh/jonathanjuliani/skills](https://www.skills.sh/jonathanjuliani/skills) both returned 404.
The index is filled by the skills CLI. This repo has no skills.sh config file.
