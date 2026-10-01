# Install

How to install and remove jon-skills, per agent.
Open this when you are installing, updating, or taking the pack back out.
Back to [jon-skills](../../README.md).

## Install

There are two ways in, and they behave differently. **Pick one**: installing both leaves you with every skill twice.

| | **Plugin** | **Files** (`npx skills`) |
| --- | --- | --- |
| What you get | A managed bundle of all 30, updating when the repo ships | Editable copies of the skills you choose |
| Invocation | Namespaced: `/jon:setup-skills` | Bare: `/setup-skills` |
| Install everything | yes | yes |
| Install one skill | no | yes |
| Install one category | no | no, list the names |
| Remove one skill | no | yes |
| Remove everything | yes | yes |
| Disable without removing | yes | no |
| Harnesses | Claude Code, Codex, Cursor, Gemini | Dozens, including all of those |

### Files, any agent

The [open skills CLI](https://github.com/vercel-labs/skills) handles this repo's layout, since it walks a skill directory three levels deep and supports `skills/<category>/<name>/SKILL.md`.

```bash
npx skills add jonathanjuliani/skills --list          # see what is in here first
npx skills add jonathanjuliani/skills                 # pick interactively
npx skills add jonathanjuliani/skills --all           # take everything
npx skills add jonathanjuliani/skills --skill design-review --skill forms
```

There is no category flag, so a whole category means listing its names. Add `-g` for your user directory instead of the project, and `-a cursor` or `-a claude-code` to target one agent.

### Claude Code

```bash
/plugin marketplace add jonathanjuliani/skills
/plugin install jon@skills
```

Skills arrive namespaced, so setup is `/jon:setup-skills`. Choose a scope when prompted: **user** (all your projects), **project** (committed to `.claude/settings.json`, shared with collaborators) or **local** (this repo, just you).

### Codex

Reads `.codex-plugin/plugin.json`, which points at `skills/`. Skills are invoked with `@`, so setup is `@setup-skills`.

```bash
codex plugin marketplace add jonathanjuliani/skills
codex plugin add jon@skills
```

### Cursor

Reads `plugins/jon/.cursor-plugin/plugin.json`, which lists every skill path (Cursor plugins do not recurse into bucket folders). These are workflows, so they belong in the skills layer rather than pasted into `.cursor/rules/*.mdc`. GitHub import needs the plugin in a subdirectory: `.cursor-plugin/marketplace.json` points at `plugins/jon` with a bare `source` name. A repo-root `"source": "./"` is silently rejected.

**Local copy (plugin development / offline).** Does not go through GitHub import. Cursor skips a symlink that points at a clone elsewhere on disk, so copy the plugin into `~/.cursor/plugins/local` instead:

```bash
./scripts/install-cursor.sh
```

Then fully quit Cursor (`Cmd+Q`) and reopen, or run Developer: Reload Window. Enable **Include third-party Plugins, Skills, and other configs**. On Teams or Enterprise, an admin also needs **Allow Local Plugin Imports**. Confirm all 31 skills under Customize → Skills, then run `/setup-skills` (or `/jon:setup-skills` if the plugin is namespaced). Re-run the script after you change the plugin locally.

**GitHub import (any plan).** Customize → Plugins → From GitHub Repository → `https://github.com/jonathanjuliani/skills`. Cursor reads `.cursor-plugin/marketplace.json` and installs `jon` from `plugins/jon`. Choose user or project scope. Setup is `/jon:setup-skills` (or `/setup-skills` if Cursor does not namespace). If the import dialog closes with no plugin and no cache folder, use the local copy instead.

**Team Marketplace.** On Teams or Enterprise, an admin can import the GitHub repo: Dashboard → Plugins → Add Marketplace → Import from Repo → `https://github.com/jonathanjuliani/skills`. Cursor reads `.cursor-plugin/marketplace.json`.

**Official Marketplace.** Once listed, install from Customize → Marketplace. Until then, submit the public repo at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish).

### Gemini CLI

```bash
gemini extensions install https://github.com/jonathanjuliani/skills
```

Reads `gemini-extension.json`, which loads `GEMINI.md` as context. That file tells the agent to open the routing block before a non-trivial task. The [Coverage](coverage.md) page is the human map of the same pack, not a second catalog for the agent.

### Then, once per repo

```bash
/jon:setup-skills     # plugin install
/setup-skills         # installed as files
```

Confirms your personal defaults, detects the project, writes `.jon-skills/config.yaml`, and offers to add a verification rule to the repo's `AGENTS.md` or `CLAUDE.md`. Everything it writes outside its own config needs an explicit yes.

> Developing locally? Point the marketplace at your clone: `/plugin marketplace add ~/development/jon/skills`

## Remove

### Files

```bash
npx skills list                      # what is installed, and from where
npx skills remove design-review      # one skill
npx skills remove forms design-brief # several
npx skills remove --all              # everything
```

`remove --all` removes **every installed skill from every source**, not only this pack. To clear just this one, name its skills, or use `npx skills remove --skill '*' -a <agent>` to clear one agent.

### Claude Code

```bash
/plugin disable jon@skills     # keep it installed, stop loading it
/plugin enable jon@skills      # put it back
/plugin uninstall jon@skills   # remove it
```

Disable is the one to reach for first: it costs nothing to undo and it is how you find out whether a pack is earning its context. Use `/plugin list` to see what is installed.

Removing the marketplace also uninstalls anything installed from it:

```bash
/plugin marketplace remove skills
```

For scripting, the `claude plugin` shell commands do the same without opening the panel, and take `--scope`.
