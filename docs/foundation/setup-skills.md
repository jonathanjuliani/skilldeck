## What it does

Sets up jon-skills for a machine and a repo. It confirms your personal defaults, detects what the current project already uses, resolves any greenfield gaps with you, and writes a per-repo config cache the other skills read.

It also offers three opt-in additions to the repo: a starter `CONTEXT.md` if there is none, a short verification rule in the repo's `AGENTS.md` or `CLAUDE.md`, and a routing table in the same file listing which skill belongs to which moment in a task. Each is asked separately and takes its own yes.

It never changes a project's tooling: no installs, no build config edits, no refactors. Everything it writes outside its own config needs an explicit yes.

## When to reach for it

You invoke this by typing `/setup-skills`, and the agent will not reach for it on its own. Reach for it once per machine to review your personal defaults, and once per repo you work in to cache the resolved conventions so skills like `create` do not re-detect every time. Skipping it is fine; the skills will detect on the fly, just without the cache.

## Prerequisites

None to run. It writes `.jon-skills/config.yaml` in the current repo, and with your agreement can seed a `CONTEXT.md` and add a verification block and a routing block to `AGENTS.md` or `CLAUDE.md`. It reads your personal defaults from `skills/foundation/resolve-conventions/defaults.yaml`.

## The two scopes

Setup touches two levels. **Per machine**: your personal defaults (package manager, lint/format, test runner, validation, naming, framework leanings) live in one file and apply everywhere as tiebreakers. **Per repo**: the resolved conventions and project shape for the current repository are cached locally. Keeping them separate is what lets the same defaults ride along while each repo keeps its own truth.

## Common questions

**Will it change my project's setup?**
Not your tooling. It records what is true and what you chose; it does not install anything or edit build config. The two files it can add to, `CONTEXT.md` and your agent instructions file, are both offered rather than assumed, and it writes each block only between that block's own markers so the rest of the file is untouched.

**Why does it want to edit my AGENTS.md?**
Because a completion gate has to already be in context when a claim is being written. The `verify-before-done` skill holds the full reasoning, but it is model-invoked, and measurement on this repo found it never got invoked on its own: zero invocations across eleven runs where it was available and relevant. An agent instructions file is read every turn without being reached for, so a short version of the rule lives there and the skill stays as the detail behind it. Say no and nothing is written; the skill still works when invoked.

**What is the routing block for?**
The same finding, applied to the other end of a task. If no skill gets reached for on its own, a list of which skill belongs to which moment is worth more in a file read every turn than in thirty-six descriptions read only when something goes looking. It routes and nothing more: each line names a moment and a skill, the skill still carries the method, and each entry fires once per task rather than once per message. Take it or leave it independently of the verification block.

**What if the repo already uses tools different from my defaults?**
The repo wins. Detection outranks personal defaults, so the config records the project's real choices, not yours.

**Do I have to run it?**
No. Other skills detect conventions on demand. Running setup just caches the result and lets you confirm greenfield choices up front.

## Invoking it

This page writes `/setup-skills` for brevity, but the prefix depends on how you installed. The plugin namespaces its skills, so it is `/jon:setup-skills` in Claude Code and Cursor and `@jon:setup-skills` in Codex. Installed as files with `npx skills`, it is plain `/setup-skills`.

## It's working if

- `.jon-skills/config.yaml` reflects what the repo actually uses, each entry tagged with how it was resolved.
- Running `create` or `project-shape` afterward does not re-ask questions the config already answers.
- Your personal defaults show up only where the project was genuinely silent.
- Each block you accepted sits between its own markers in `AGENTS.md` or `CLAUDE.md`, and re-running setup updates that block rather than adding a second one.
- Everything that was in your agent instructions file before is still in it.
