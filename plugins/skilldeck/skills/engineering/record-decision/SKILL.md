---
name: record-decision
description: Write a durable architecture decision into the project's existing decision home. Use when a choice will outlive the pull request, such as storage, an API style, a repository split, an auth model, or an explicit refusal, or when the user asks for an ADR or an architecture decision. Not for explaining a shape that is already decided, which is diagram, not for sequencing work, which is plan-delivery, not for rules that bind every agent turn, which is agent-instructions, and not for lessons after a delivery, which is retro.
---

# Record decision

Write down a choice that will still matter after this change is merged, including what was rejected. The output is a decision record. It is not the implementation of that decision.

The defining constraint: a decision without the rejected options is a preference. The next person cannot tell a settled tradeoff from an accident, and they will reopen it.

## Find where decisions already live

Look for an existing home before inventing one: `docs/adr/`, `docs/decisions/`, `ARCHITECTURE.md`, or a decisions section the project already keeps. Match its filename, status words, and tone. Call the Skill tool with "resolve-conventions" and with "project-shape" only to find that home, not to redesign the repo around it.

When nothing exists, propose `docs/adr/` and use [adr-template.md](adr-template.md) as the payload. Say that you are proposing the home, and write the record only after the user accepts the location. One new home, not a second folder beside one that already works.

## Write the decision, not the build

State the decision in one sentence, in the form "we will X", including a refusal ("we will not X") when that is the choice.

Then two or three real options. Each rejected option gets the reason it lost, specific enough that a later reader can tell whether the reason still holds. An option nobody would actually choose does not count.

Record the consequences: what becomes easier, what becomes harder, and what would force the decision to be reopened. Leave implementation for a separate ask. Do not start the migration, the schema, or the endpoint from this skill.

When the choice cannot be understood as text, call the Skill tool with "diagram" for one picture. A decision that reads clearly does not need one.

## Rules

- **The project's format wins.** A template is the fallback for a repo that has no decisions yet.
- **Rejected options stay in the record.** Deleting them makes the choice look obvious and invites the same debate next month.
- **One decision per record.** A record that settles storage and authentication settles neither.
- **Status is explicit.** Proposed until the user accepts it, then accepted. A superseded decision points at the record that replaced it rather than being edited into its opposite.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The pull request description already explains it" | A pull request is closed and forgotten. The next change will not open it |
| "We only need the option we picked" | Without the rejected options, every new teammate re-runs the same argument |
| "I will implement it while I write the record" | The record is how you agree. The implementation is a later change that can be reviewed against it |

## When this does not apply

A choice that only this change cares about, a naming nit, and a decision the project has already recorded do not need a new record. Point at the existing one.

The shape survives where the rule yields. When you skip the record, say the choice in one sentence anyway, so it is not only in the diff.

## Before you hand it over

Check the record for the three failures that make it useless later: no rejected option, a decision sentence that does not say what will be done, and a write-up that started building the thing.

Do not claim the decision is accepted unless the user accepted it.
