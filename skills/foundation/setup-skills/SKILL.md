---
name: setup-skills
description: One-time setup for the jon skills plugin. Confirm your personal defaults, detect the current project's conventions, and write the per-repo config the other skills read.
disable-model-invocation: true
---

# setup-skills

Set up jon-skills for a machine and a repo: confirm the personal defaults, detect what the current project already uses, and cache the resolution so the other skills run without re-detecting every time.

The defining constraint: this skill only records decisions, it never changes project tooling. It writes `.skilldeck-skills/config.yaml` only after a yes, and with a separate yes it seeds vocabulary and installs agent instructions blocks. It does not install packages, edit build config, or refactor.

## What it does

1. **Confirm personal defaults.** Read the personal defaults file at `skills/foundation/resolve-conventions/defaults.yaml`. Show the current personal defaults (package manager, lint/format, test runner, validation, naming, framework leanings) and let the user edit any of them. These are tier 3: tiebreakers used only when a project is silent.
2. **Detect the project.** Call the Skill tool with "resolve-conventions" to read the current repo and resolve its conventions from the project first. Then call the Skill tool with "project-shape" to determine single-repo, monorepo, or modular, and the surfaces present (backend, frontend, mobile).
3. **Report the resolution.** Show each resolved convention and the tier it came from (detected, company, personal, or a greenfield recommendation awaiting a choice). Resolve any greenfield gaps with the user now.
4. **Ask, then write the config.** Ask whether to write `.skilldeck-skills/config.yaml`. Write it only after a yes. It holds the resolved conventions, project shape, and detected surfaces, each with its evidence. This is the cache the other skills trust. If the file already exists, show the diff against a fresh detection and ask before overwriting.
5. **Offer to seed vocabulary.** If the repo has no `CONTEXT.md`, offer to create a minimal one so terms stay consistent. Do not overwrite an existing `CONTEXT.md`.
6. **Offer the verification block.** Ask whether to add a short verification rule to the repo's agent instructions file (`AGENTS.md` or `CLAUDE.md`). The text and the placement rules are in [agent-instructions-block.md](agent-instructions-block.md). This matters because `verify-before-done` is model-invoked and a completion gate has to be in context at the moment a claim is written, not waiting to be reached for. Default to offering it; never write it without a yes.
7. **Offer the routing block.** Ask separately whether to add the routing table, which lists which skill belongs to which moment in a task. Same file, same procedure, same payload rules in [agent-instructions-block.md](agent-instructions-block.md). It exists because a skill nobody reaches for does not run, and a repo's instructions file is read every turn while a skill description is only read when something goes looking for it. Ask separately from step 6 and take a separate yes: a repo may want the gate without the routing, or the reverse.

## Scope

- **Per machine**: personal defaults live in `skills/foundation/resolve-conventions/defaults.yaml`. Editing them here changes them for every repo.
- **Per repo**: `.skilldeck-skills/config.yaml` is specific to the current repository. Run setup once per repo you work in, or let the skills detect on the fly if you skip it.
- **Per repo, opt in**: `CONTEXT.md` and the verification and routing blocks in `AGENTS.md` or `CLAUDE.md` are the only files outside `.skilldeck-skills/` this skill writes, and each only after its own explicit yes.

## Rules

- Never modify build config, lockfiles, or source. Setup records, it does not act.
- Never write a personal or community default into `config.yaml` as if it were detected. Mark each entry with its tier and evidence so the cache stays honest.
- If `.skilldeck-skills/config.yaml` already exists, show the diff against a fresh detection and ask before overwriting.
- Write each block only between its own markers, and only after a yes for that block. On a repeat run, replace what is between the markers rather than appending a second copy, and if that text has been edited, show the difference and ask.

## When this does not apply

The other skills detect on the fly, so setup is a convenience and not a prerequisite. Skip it on a repo you are passing through, on a repo whose conventions are already unambiguous, and any time the user just wants the task done. Never run it unprompted; it is user-invoked for exactly that reason.

## Before you hand it over

Check the written config against the three things that go wrong here: every entry carries its tier and its evidence, no personal or community default is recorded as though it were detected, and the only files touched outside `.skilldeck-skills/` are ones the user said yes to, each still carrying its own content around anything you added.
