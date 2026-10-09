---
name: resolve-conventions
description: Resolve which tool or pattern a project should use (package manager, formatter, test runner, validation, folder layout, naming) by detecting the project first and deferring to it. Use when any task needs a stack or convention decision, before scaffolding, refactoring, adding a dependency, or setting up tooling, and whenever the right choice depends on what a project already uses. Not for deciding where code should live, which is project-shape, and not for judging whether to take on a new dependency at all, which is dependency-choice.
---

# Resolve conventions

Decide which tool or pattern a project should use by resolving it against a fixed precedence chain, never by assuming a vendor. This skill is the reference the rest of the plugin consults before it makes any stack choice.

The defining constraint: a convention is only ever *resolved*, never defaulted-into blindly. Detection of what the project already does outranks every default, and a greenfield default is proposed with a rationale and confirmed, never applied silently.

## The precedence chain

For every convention (package manager, formatter/linter, test runner, validation library, framework, folder layout, naming style, and so on), resolve in this order and stop at the first tier that answers:

1. **Project (detected).** Read the repository. A lockfile, a `package.json` field, a config file, or the existing folder layout is the answer. Detection always wins. See [detection.md](detection.md).
2. **Company.** If the repo carries `.skilldeck-skills/company.yaml` or a company standardization skill (for example an in-repo code-standards skill), defer to it. It outranks personal and community defaults.
3. **Personal.** The seeded tiebreakers in [defaults.yaml](defaults.yaml). Apply only when tiers 1 and 2 are silent.
4. **Community.** For anything still unresolved on a greenfield project, recommend the current community default from [community-defaults.md](community-defaults.md) with a one-line rationale, then ask the user to confirm or override. Never apply a community default without confirmation.

A higher tier always wins. Never apply a lower tier over a resolved higher one: if a repo uses npm and Jest, you use npm and Jest, even though the personal defaults are pnpm and Vitest.

## How to use it

1. **Read the cache.** If `.skilldeck-skills/config.yaml` exists, it holds conventions already resolved for this repo. Trust it unless the repo has visibly changed. It is written by the `setup-skills` skill.
2. **Detect.** For each convention the task needs, run the checks in [detection.md](detection.md). Record what you found and how you found it (the evidence), so the choice is auditable.
3. **Fill the gaps.** For conventions detection could not resolve, walk tiers 2 through 4. On greenfield, present the community recommendation and the personal default together and let the user pick.
4. **Report the resolution.** State each resolved convention and the tier it came from, briefly. "Package manager: pnpm (detected: pnpm-lock.yaml). Test runner: none found, recommend Vitest (community default), your personal default is also Vitest, confirm?" Transparency is the point: the user should always see why a choice was made.

## Rules

- **Detect before you decide.** Never propose a default for something the repo already answers.
- **Recommend before you impose.** On greenfield, the community default is a recommendation with a reason, not a decision.
- **Ask before you assume.** A default is applied only after the user confirms, or when a higher tier resolved it unambiguously.
- **Keep vendors out of other skills.** Other skills call this one for choices; they must not hardcode a package manager, formatter, or test runner in their own steps.
- **Freshness.** [community-defaults.md](community-defaults.md) is a snapshot with a date. When currentness matters for a specific choice and the web is available, verify the current community consensus before recommending, and note if it has moved.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "This repo almost certainly uses X" | Detection costs one file read and removes the guess entirely |
| "It is greenfield, so the personal default applies" | Tier 3 resolves the choice, it does not authorize applying it silently. Greenfield is exactly where you present and ask |
| "The cache is there, so it is current" | Trust it unless the repo has visibly changed. Then re-detect, and say that you did |

## When this does not apply

Skip the resolution when the user has already named the tool for this task, when the choice was settled earlier in the conversation, or when nothing about the work touches a convention (reading code, answering a question, writing prose). A throwaway script that will never be committed does not need a resolved stack either.

The shape survives the exception. Even when you skip the chain, say which tool you used and why it was already settled, so the choice stays auditable.

## What this skill is not

It does not install anything, edit configs, or scaffold. It resolves and reports. The skills that act on the resolution (`create`, `project-shape`, and others) call this one first, then do the work.
