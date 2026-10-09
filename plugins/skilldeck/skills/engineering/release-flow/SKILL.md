---
name: release-flow
description: Set up or run a versioning and release process for a JS/TS package, app, or monorepo (versioning, changelog, publishing). Use when the user is cutting a release, setting up release automation, or deciding on a versioning scheme. Defers to any process the project already has and to resolve-conventions. Not for how a change reaches production, its pipeline, flags, or rollout, which is ship-flow.
---

# Release flow

Version and ship a change with a process that is repeatable and honest about what changed. Releases go wrong when the version and the changelog are an afterthought; this skill makes them a byproduct of the work.

This skill is about versioning an artifact. Call the Skill tool with "ship-flow" for the path a change takes to production, which is a separate question: a continuously deployed service has a ship flow and no releases, a published library has releases and barely a ship flow.

The defining constraint: if the project already has a release process, you run that process, you do not invent a new one. A second, parallel release mechanism is worse than a mediocre single one.

## First, detect the existing process

Call the Skill tool with "resolve-conventions" and inspect the repo:

- A `.changeset/` folder then Changesets. A `release` config or `semantic-release` then that. Conventional-commit history plus a release workflow then commit-driven releases. A manual `CHANGELOG.md` and `npm version` then a manual flow.
- Match whatever is there. Only when there is genuinely none do you propose one.

## Choosing a process on greenfield

- **Changesets** for libraries and monorepos: contributors write a changeset per change describing the bump and the human-readable note; release aggregates them. Handles multi-package versioning well. The community default for monorepos.
- **Conventional commits + automated release** when the team already writes structured commits and wants versioning derived from them.
- **Manual semver** for a small single package: bump by hand, write the changelog entry, tag, publish. Fine until the cadence outgrows it.

Recommend, with the reason, then confirm.

## Versioning discipline (semver)

- **Patch** for backward-compatible fixes, **minor** for backward-compatible additions, **major** for anything that breaks a consumer. When unsure between minor and major, ask what a consumer would have to change; if the answer is "something", it is major.
- **Pre-1.0** signals instability: breaking changes may land in minors, but say so in the changelog.
- The changelog is written for the consumer: what changed and what they must do, not a commit dump.

## Running a release

1. Ensure the working tree is clean and CI is green on the release commit.
2. Determine the version bump from the accumulated changes (via the project's mechanism).
3. Update the changelog, bump the version, tag.
4. Publish through the project's channel (registry, app store track, deploy). Publishing and pushing are outward actions: confirm with the user before doing them, and never publish credentials or tokens.
5. Verify the published artifact and that the tag and changelog match what shipped.

## Rules

- **Use the project's process.** Detect first; invent only on true greenfield.
- **Version reflects impact, not effort.** A one-line breaking change is a major; a huge internal refactor with no API change is a patch.
- **The changelog is a contract with consumers.** Write it for them.
- **Confirm before publishing.** A release is hard to reverse; get an explicit yes, and let the user handle any credential entry.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "CI was green on the last commit" | You are releasing this commit. Fresh output, or no release |
| "The changelog can be written after the tag" | It will not be, and the tag is what consumers reach for |

## When this does not apply

Merging is not releasing. This skill governs the moment a version becomes something a consumer can install or a user can run, not every landing on the main branch.

## Before you hand it over

Before publishing, call the Skill tool with "verify-before-done" and prove CI is green on this commit. Publishing is an outward action that is hard to reverse, so get the user's explicit yes and leave any credential entry to them.

After publishing, check that the tag, the changelog entry, and the published artifact all describe the same change.
