# AGENTS.md

Guidance for an agent working **on this repository**, which is a skills plugin. It is not meant to be copied into another project: the reusable part of this repo is `skills/`, not this file.

## When adding or editing a skill

Read [`.agents/conventions.md`](.agents/conventions.md) first and follow it. It is the authority on anatomy, invocation, dependencies between skills, guardrails, style, and markdown. Do not restate its rules here or infer them from existing files.

Then, before finishing:

```bash
python3 scripts/validate.py
```

It checks frontmatter, naming, guardrails, links, manifest sync and markdown style. A commit is blocked on failure by `.githooks/pre-commit`, which needs `git config core.hooksPath .githooks` once per clone.

## When adding a skill, register it everywhere

A new skill is not installed until it is listed in every harness manifest, and the validator will fail until it is:

- `.claude-plugin/plugin.json` and `plugins/jon/.cursor-plugin/plugin.json` list each skill path explicitly (plugin loaders do not recurse into bucket folders).
- `.codex-plugin/plugin.json` points at `./skills/` as a directory and needs no per-skill entry.
- `docs/pack/skills.md` lists the skill under its bucket, and the four-bucket counts in `README.md` stay in sync.
- A **user-invoked** skill also needs `disable-model-invocation: true` in its frontmatter, `policy.allow_implicit_invocation: false` in its `agents/openai.yaml`, and a page under `docs/<bucket>/`.

## When changing how skills reach each other

The phrase `Call the Skill tool with "<name>"` is load-bearing and Claude Code specific. It is the only cross-skill mechanism in this repo that has been observed working, so do not reword it for portability without measuring the replacement. See `evals/RESULTS.md` for what was measured and what was not.

## When releasing

Add each change under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you make it. Release with `python3 scripts/version.py <patch|minor|major>` on a clean `main`, then `git push --follow-tags`. Never change the version in one file by hand: `python3 scripts/version.py --check` fails, and marketplace users only receive a change after a version bump.

## What this repo does not have

No Node toolchain, no package manager, no markdown formatter, no build step. The only dependency is pyyaml. A formatter was measured against this repo and rejected; the reasoning is in `.agents/conventions.md`. Do not add one back without reading that first.
