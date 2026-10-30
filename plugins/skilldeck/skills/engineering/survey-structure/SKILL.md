---
name: survey-structure
description: Read an existing JS/TS repo and return a refactor backlog for its layout and module shape, without changing files.
disable-model-invocation: true
---

# Survey structure

Read an existing repository and return the refactors that would make the next change easier. The reply is the backlog. Nothing is written.

The defining constraint: this skill reports and stops. The obvious move is to fix the first finding while the files are open, and that move is how a survey becomes an unreviewed rewrite.

## Read, then list

Call the Skill tool with "resolve-conventions" for the project's posture. Call the Skill tool with "project-shape" for the shape and the layout that surface wants. Call the Skill tool with "ts-standards" for module depth, naming, and validation at the edge. The project's existing layout wins where it is already consistent, including where it is imperfect.

Reply with the detected shape and the evidence, then the findings. Each finding is one future refactor:

- The path.
- What is wrong, against the layout or the module rule.
- Why the next change is harder because of it.
- One motivation sentence, the kind `refactor` can carry alone.

A monorepo is a finding only when a second consumer of shared code already exists. A wide component counts as a wide module: many exports or boolean props, little hidden behind them. A layer that does no work (a repository with no persistence, a service that only reads config) is a finding. A folder tree organized by technical type, when the project is not already consistent about it, is a finding.

Group everything else as not-now, with the reason: a consistent layout, a one-file nit, a speculative package split.

## Hand off, do not start

Do not start a refactor, and do not edit. When the list is long enough that the order is contested, tell the user to run `/plan-delivery` on it. When they pick one item, they ask for that refactor in its own turn. One motivation per refactor.

Do not write the backlog into the repository. The reply is the artifact.

## Rules

- **Report, then stop.** A finding stated is the deliverable. A finding fixed is a different skill and a different turn.
- **One motivation per item.** A finding that needs two sentences of intent is two findings.
- **Match the project.** Where the tree is consistently one way, that way wins over the default in `project-shape`.
- **Name what you are not listing.** The not-now group is a decision, so an omission is not a silent drop.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "I will fix the first finding while I am here" | The survey then becomes the refactor, and the rest of the list never gets read |
| "The layout is a mess, so the ideal one applies" | A mess applied consistently is still the project's language. Name the friction, and leave the replacement for a turn that asks for it |

## When this does not apply

An empty or near-empty tree has nothing to survey. That job is `bootstrap-repo`. A user who already named the one refactor they want is not asking for a list. That job is `refactor`. A question about a single file whose neighbors already answer it is not a survey.

The report survives the exception. When you skip the list, say what was already settled so the next unit matches it.

## Before you hand it over

Check the reply for the three things this skill gets wrong: a file that changed, a finding with more than one motivation, and a reorg recommended where the current structure is already consistent.

Then confirm the worktree is unchanged.
