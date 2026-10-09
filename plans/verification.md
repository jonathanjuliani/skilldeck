# Verification

Run these after the phase that claims the platform, on a machine that does not already have the old hub marketplace registered. Where a tool is missing, record the skip in the phase note. Do not treat a skip as a pass.

Local checks come before any GitHub rename or Cursor submission.

## skilldeck

Clone path below is the local checkout. After phase 2, `jonathanjuliani/skilldeck` is this repo. Before phase 2, use the local path or `jonathanjuliani/skills`.

### Claude Code

Doc: [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace).

```text
claude plugin marketplace add /path/to/skilldeck
claude plugin install skilldeck@skilldeck
```

Expected: `/plugin` lists marketplace `skilldeck` and one plugin, `skilldeck`. A new session exposes `/skilldeck:setup-skills`. There is no plugin named `skills`, and no second plugin. All 36 skills load from this one install.

Update, after `v1.0.0`:

```text
claude plugin marketplace update skilldeck
```

Expected: the installed version matches the tag. A machine that previously had the hub no longer offers `skills@skilldeck`. If update keeps the old plugin, remove and add:

```text
/plugin marketplace remove skilldeck
/plugin marketplace add jonathanjuliani/skilldeck
/plugin install skilldeck@skilldeck
```

### Codex

Doc: [Package your plugin](https://developers.openai.com/plugins/build/plugins).

```text
codex plugin marketplace add /path/to/skilldeck
```

Expected: the marketplace file read is `.agents/plugins/marketplace.json`. One plugin, `source.path` `./plugins/skilldeck`. Restart Codex, open the plugin directory, install `skilldeck`. The pack's skills are invocable.

ChatGPT desktop: add the same local marketplace, restart, install that plugin from the Plugins Directory. Expected: the plugin name matches `interface.displayName` or the manifest `name`.

### Cursor

Doc: [Plugins](https://cursor.com/docs/plugins).

Local, before any publish:

```text
./scripts/install-cursor.sh
```

Expected: `~/.cursor/plugins/local/skilldeck` is a real directory, not a symlink. Quit Cursor (`Cmd+Q`) or Developer: Reload Window. Customize → Skills lists the 36 skills. Enable third-party plugins. On a Team or Enterprise account, an admin has allowed local plugin imports.

GitHub import, after phase 2: Customize → Plugins → From GitHub Repository → `https://github.com/jonathanjuliani/skilldeck`.

Expected: one plugin from `.cursor-plugin/marketplace.json`. Marketplace `name` is `skilldeck`. `source` is the bare name `skilldeck` with `pluginRoot` `plugins`. A `source` of `./plugins/skilldeck` is a failure. Do not also import `skilldeck-hub`.

Team: Dashboard → Plugins → Add Marketplace → Import from Repo → the same URL. Expected: the same one plugin. Refresh after a version bump shows the new version without a reinstall only if Cursor's refresh works. If it does not, reinstall and note it. That bug is upstream ([forum](https://forum.cursor.com/t/team-marketplace-auto-refresh-does-not-pick-up-plugin-changes-manual-refresh-cache-clear-reinstall-required/154675)).

Public listing, after phase 5: install from Customize → Marketplace. Expected: the reviewed version, not a local copy. Remove the local copy first so skills are not doubled.

### GitHub Copilot

Doc: [Creating a marketplace](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace).

```text
copilot plugin marketplace add /path/to/skilldeck
copilot plugin marketplace browse skilldeck
copilot plugin install skilldeck@skilldeck
```

Expected: browse lists one plugin named `skilldeck`. If add reports no marketplace, add `.github/plugin/marketplace.json` (skilldeck phase 3) and repeat. VS Code and the Copilot app use the same repo once it is in `chat.plugins.marketplaces` or installed via the CLI.

### VS Code

Doc: [Agent plugins in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-plugins).

User `settings.json`:

```json
{
  "chat.plugins.enabled": true,
  "chat.plugins.marketplaces": ["jonathanjuliani/skilldeck"]
}
```

Expected: Chat → Agent Customizations → Plugins lists `skilldeck`. Skills in this repo live at `plugins/skilldeck/skills/<bucket>/<name>/SKILL.md`. If the skill list is empty, record which marketplace file VS Code fetched and that nested folders were not walked. Do not flatten the tree in response. The Claude and Cursor installs remain the pass for those clients.

Local, before the rename: a `file:///` marketplace path, if the setting accepts one, against the clone. The doc says GitHub shorthand, HTTPS, SSH, and `file:///` paths work.

### Antigravity

Doc: [Plugins](https://antigravity.google/docs/plugins/).

```text
agy plugin install /path/to/skilldeck/plugins/skilldeck
agy plugin list
```

Expected: either the plugin is installed and its skills are listed, or `agy` rejects `plugin.json`. Write the rejection into `docs/install.md`. Do not add a second manifest to make this pass.

There is no documented `-a antigravity` target in the skills CLI. If `agy` rejects the folder, the install doc points at `npx skills add jonathanjuliani/skilldeck` and says Antigravity's workspace skills live in `.agents/skills/`.

### Gemini CLI

Doc: [migration to agy](https://antigravity.google/docs/cli/gcli-migration/). Individual accounts are already shut down.

```text
gemini extensions install /path/to/skilldeck
```

Expected, on an account that can still call Gemini CLI: the extension name is `skilldeck` and `GEMINI.md` is loaded. On an individual account: a request failure is a pass for "we did not invest in this" only if the extension file itself validates. Do not spend time debugging Gemini CLI auth.

### Windsurf and OpenCode

Doc: [vercel-labs/skills](https://github.com/vercel-labs/skills).

```text
npx skills add /path/to/skilldeck --list
npx skills add /path/to/skilldeck --all -a windsurf
npx skills add /path/to/skilldeck --all -a opencode
```

Expected: `--list` prints 36 skills. Windsurf writes under `.windsurf/skills/` or `~/.codeium/windsurf/skills/`. OpenCode writes under `.agents/skills/` or `~/.config/opencode/skills/`. Installing the repo twice with different agents does not duplicate inside one agent.

### Devin

This release does not install a Devin plugin. Do not run `devin plugins install`, and do not add `.devin-plugin/plugin.json`.

```text
npx skills add /path/to/skilldeck --all -a devin
```

Expected: the 36 skills under `.devin/skills/` or `~/.config/devin/skills/`.

### skills CLI, any agent

```text
npx skills add jonathanjuliani/skilldeck --skill debug --skill design-review
```

Expected: those two skills, and not the other 34. After the rename, `npx skills add jonathanjuliani/skills --list` still works and hits the redirected repo.

## skillverse

### Claude Code

```text
claude plugin marketplace add /path/to/skillverse
claude plugin install skillverse@skillverse
```

Expected: one Skillverse button in a new session. `claude plugin validate .` and `pnpm run test:plugin` pass. A second install from a folder (`claude --plugin-dir /path/to/skillverse`) plus the marketplace shows two buttons. The install doc says to pick one.

```text
claude --plugin-dir /path/to/skillverse
```

Expected: the pane still loads from `.claude-plugin/plugin.json`. There is no root `plugin.json`.

### npm and the local web app

```text
npm i -g @jonathanjuliani/skillverse@<released-version>
skillverse run
skillverse status
curl -fsS http://127.0.0.1:4317/health
skillverse open
skillverse stop
```

Port may be 4317–4320 or `SKILLVERSE_PORT`. Expected: `/health` succeeds, the browser opens the page, `stop` makes a second curl fail. From another machine, the port does not answer. A page on another origin does not read `/data.js` (covered by `tests/unit/server.spec.ts`; re-run `pnpm test`).

```text
npx skills add /path/to/skillverse --list
```

Expected: no skills. The README says this command is not the install path yet.

### Privacy spot check

With the web app running:

- `lsof` or `ss` shows the listen address as `127.0.0.1`, not `0.0.0.0`.
- The response to a request with `Origin: https://example.com` has no `Access-Control-Allow-Origin`.
- A hook payload fixture in `pnpm test` still asserts that a prompt and a command are not forwarded.

No new privacy test is required if `tests/unit/server.spec.ts` already covers the first two. Read it before adding one.

## Shared CI

On a throwaway branch of skilldeck, set one marketplace `source` to `./plugins/no-such-plugin` and open a pull request.

Expected: the check fails, and the log contains `./plugins/no-such-plugin`. skilldeck runs `scripts/marketplace_check.py` from `validate.yml`.

Do not open that pull request on skillverse. This release does not call the shared workflow from there.

Revert the skilldeck branch. Do not merge it.

## Rename

After skilldeck phase 2:

| URL or command | Expected |
| --- | --- |
| `https://github.com/jonathanjuliani/skills` | Redirects to `jonathanjuliani/skilldeck`, this repo |
| `https://github.com/jonathanjuliani/skilldeck` | One plugin, `skilldeck`, not the hub |
| `https://github.com/jonathanjuliani/skilldeck-hub` | Archived, migration paragraph only |
| `npm view @jonathanjuliani/skilldeck` | Deprecation message, no new feature release |
| `npx skills add jonathanjuliani/skills --list` | 36 skills |
| A new repo named `skills` under the account | Not created |

## Not a pass

- A screenshot of a marketplace page without installing.
- `claude plugin marketplace add` against the hub URL after the rename.
- Cursor listing "submitted" without a local `~/.cursor/plugins/local/skilldeck` install first.
- Antigravity marked done because a JSON file exists, when `agy` was never run and the rejection was not written down.
- Devin marked done because a `.devin-plugin/plugin.json` exists. The pass is `npx skills add … -a devin`.
