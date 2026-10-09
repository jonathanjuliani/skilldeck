---
name: ship-flow
description: Get a change from a working tree to production safely, covering commit and branch discipline, change size, CI as a quality gate, feature flags, staged rollout, and a rollback path. Use when setting up or fixing a pipeline, planning how a risky change reaches users, deciding how to split work into commits or pull requests, or preparing a deploy. Not for a production incident already hurting users, which is mitigate-incident, and not for version numbers, changelogs, or publishing a package, which is release-flow.
---

# Ship flow

Move a change from a working tree into production without either sitting on it or breaking it. This skill covers the path a change takes; call the Skill tool with "release-flow" for versioning an artifact, which is a different question with its own answers. A service that deploys continuously has a ship flow and no releases. A library published to a registry has releases and barely a ship flow. Many projects have both, and they should not be run as one process.

The defining constraint: risk scales with the size of a change and the time it waited, not with how carefully it was reviewed. Small and frequent beats large and cautious, because a small change that breaks something is diagnosable in minutes and a large one is an investigation. Every practice here follows from making changes smaller and the path shorter.

## Shape the change

- **A commit is one coherent step**, with a message saying why rather than what, since the diff already says what. Commits are also save points: commit at each green state so a bad step costs one revert instead of an afternoon.
- **A pull request is one reviewable idea.** Reviewers find real problems in a small diff and rubber-stamp a large one, so the size of a change determines the quality of its review far more than the diligence of the reviewer.
- **Separate mechanical from meaningful.** A rename across two hundred files, or a formatting pass, goes in its own commit or its own pull request. Mixed with logic, it hides the logic.
- **Branch as briefly as the project's model allows.** Long-lived branches accumulate conflicts and delay integration. Match whatever the project already does rather than importing a workflow.

## The gate

CI is a gate, not a notification. Anything the team agreed on runs there and blocks on failure, otherwise it is a suggestion that erodes.

- **Fast checks first.** Format, lint, types, unit tests, then the slow ones. Failing in ninety seconds is worth more than a thorough result in twenty minutes.
- **The same commands locally and in CI.** A check that only exists in the pipeline gets discovered at the worst moment, and one that only exists locally does not exist.
- **A red main branch is an emergency**, ahead of feature work. A tolerated red build teaches everyone to ignore the signal.
- **Never claim the pipeline is green from memory.** Call the Skill tool with "verify-before-done" before saying a build or a check passed.

## Decouple deploy from release

Deploying code and exposing behavior are separate acts, and separating them is what makes shipping calm.

- **A feature flag lets unfinished work land** on the main branch, off, and be turned on independently of a deploy. That is what makes small, frequent integration possible on work that takes weeks.
- **Flags are temporary by construction.** A flag with no removal owner becomes permanent, and permanent flags multiply the states the system can be in until nobody can reason about it. Record who removes it and when, at the moment it is added.
- **Roll out in stages** for anything risky: a fraction of traffic, an internal cohort, then everyone, watching the numbers between steps. Call the Skill tool with "observability" for what to watch, since a staged rollout you cannot measure is just a slower deploy.

## Before you deploy

- **Know how to undo it.** A rollback path is decided before the deploy, not discovered during one. A change that cannot be rolled back, such as a destructive migration, needs the expand-and-contract shape instead: add the new thing, move traffic to it, remove the old thing in a later deploy.
- **Migrations ship separately from the code that needs them**, and both directions work, or the deploy is one-way.
- **Deploying is an outward action.** Confirm with the user before deploying to a shared environment, and leave any credential entry to them.

## Rules

- **Small and often.** The strongest available lever on both risk and speed, and the one teams give up first under pressure.
- **The pipeline blocks or it is decoration.** A check that warns is a check that is ignored.
- **Every risky change has an off switch**, whether a flag, a staged rollout, or a rehearsed rollback.
- **Never carry unrelated work along.** A deploy containing two changes is a deploy you cannot bisect.
- **Match the project's process.** Branching model, pipeline, and environments are detected, not imported. Call the Skill tool with "resolve-conventions".

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It is safer to batch these and deploy once" | A batch fails as a unit and is diagnosed as a unit. Batching converts several small, attributable risks into one large, unattributable one |
| "The change is too small to flag" | Size does not predict blast radius. A one-line change to a shared path reaches everyone at once |
| "We will remove the flag later" | Later needs a name and a date, or the flag is permanent and the branch it guards is now dead code nobody dares delete |
| "CI is probably fine, it passed on my machine" | Then the check that matters is the one that has not run. Run it |

## When this does not apply

A personal project deploying by hand, a prototype, and a library with no deployment of its own do not need this. A production incident already hurting users is not a planned deploy either; that job is `mitigate-incident`. Reach for this skill when other people depend on the thing being up, which is the point at which an undo path stops being optional.

Where the project has no pipeline at all and building one is out of scope for the task, say which checks are running only in someone's shell, so the gap is visible rather than assumed covered.

## Before you hand it over

Check the plan for the three omissions that turn a routine deploy into an incident: no stated way to undo it, a migration that has to land in the same step as the code using it, and a flag added with nobody named to remove it.
