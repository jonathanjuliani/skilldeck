---
name: migration
description: Remove or replace something a codebase still depends on, covering deprecation, incremental migration to a new library or pattern, and deleting code nobody uses. Use when sunsetting a feature, upgrading across a breaking major version, replacing a dependency or an internal API, or clearing out code that looks dead. Not for the first design of a model nothing depends on yet, which is data-model, not for restructuring code that is staying, which is refactor, and not for removing something with no callers left, which is just a deletion.
---

# Migration

Retire an old thing in favour of a new one without a period where both are half-wired and nothing is trustworthy. The unit of work here is not the new code, which is usually the easy part, but the removal of the old, which is the part that gets abandoned.

The defining constraint: a migration is finished when the old thing is gone, not when the new thing works. Every unfinished migration leaves a codebase permanently more complicated than either the before or the after, and a codebase carrying three of them costs more than the sum, because now every change has to be correct in three worlds.

## Decide whether to migrate at all

Code is a liability, so removing something is a win on its own terms, and adding a second way of doing something is a cost even when the second way is better.

Before starting, answer what makes this worth a migration rather than leaving it: a security or support cliff, a cost that compounds, a capability genuinely blocked. "The new one is nicer" does not survive contact with a half-finished migration. If the honest answer is that the old thing works, the correct outcome is to leave it and say so.

Then answer the harder question: **who finishes it, and by when.** A migration with no owner and no date is a decision to have two systems forever.

## Expand, migrate, contract

The shape that keeps the codebase working throughout:

1. **Expand.** Add the new thing alongside the old. Nothing switches yet, and both work. Where they must share state or data, this is the step that has to be correct in both directions.
2. **Migrate.** Move callers over incrementally, in reviewable batches, each one landing and shipping on its own. Keep the old path working until its last caller is gone. This is where a feature flag earns its place: call the Skill tool with "ship-flow" for the rollout and the undo path.
3. **Contract.** Delete the old thing, its tests, its config, its documentation, and its dependency. **This step is the migration.** A codebase where step three never happened has paid every cost and collected no benefit.

For anything touching stored data, the same shape applies with the extra rule that the expand step ships and settles before the contract step is even written. A migration that changes the shape of data and the code reading it in one deploy has no rollback.

## Deprecate before you remove

When other people's code depends on the thing, removal needs a runway.

- **Say what replaces it.** A deprecation notice with no migration path is an announcement that someone else now has a problem.
- **Make it visible where the decision is made**, which is the editor and the build, not a changelog nobody reads. A type-level deprecation and a build warning reach the caller; a wiki page does not.
- **Advisory or compulsory, decided up front.** Advisory means the old path keeps working indefinitely and adoption is voluntary, which is honest but means you own both forever. Compulsory means a date exists after which it breaks, and it only works if the date is communicated, real, and held.
- **Removal is a breaking change** for anything with external consumers. Call the Skill tool with "release-flow" for the versioning that implies.

## Deleting code that looks dead

The cheapest migration is a deletion, and the risk is deleting something that was not dead.

Establish it is unused rather than assuming: search for callers including dynamic and string-based references, check the routes and the config, and prefer evidence from production over reading. Telemetry answers this better than grep does, and call the Skill tool with "observability" where nothing currently reports it.

Then delete it outright. Commenting it out or leaving it behind a flag preserves the maintenance cost and removes the clarity, which is the worst of both. Version control is the archive, and a deletion is one revert away.

## Rules

- **The migration is the contract step.** Anything short of the old thing being gone is work in progress, and it should be reported that way.
- **One migration at a time.** Two in flight in the same area multiply the states a reader has to hold, and neither finishes.
- **Never migrate and improve in the same change.** Port the behavior exactly, then change it separately, or you cannot tell a migration bug from an intended difference.
- **Incremental, always shippable.** Each batch lands on its own. A migration that only works when it is complete is a rewrite wearing a migration's clothes.
- **A removal date needs an owner.** Both, written down, or the deprecation is permanent.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "We will remove the old one once everything is moved" | That is the step that gets dropped when the next priority arrives. Schedule the contract step with the work, not after it |
| "Leave it, it might still be used somewhere" | Then find out. "Might be used" is what keeps dead code alive for years, and it is answerable with a search and a metric |
| "Might as well clean it up while porting it" | Now a behavior difference and a porting bug look identical, and the diff cannot be reviewed against the original |
| "It is deprecated, so nobody should be calling it" | Should is not a control. If it still works, it is still load-bearing until the callers are counted |

## When this does not apply

Replacing something with no callers is a deletion, not a migration, so just delete it. A dependency upgrade with no breaking changes is an upgrade. Reach for this skill when something is depended on and has to stop being depended on.

The shape yields where the old and new genuinely cannot coexist, which happens with some data and infrastructure changes. Then the migration is a cutover, and the requirement moves to a rehearsed rollback and a tested restore rather than incrementalism.

## Before you hand it over

Check for the three residues a migration leaves when it stops early: the old dependency still in `package.json` after its last caller went, tests and fixtures still covering the removed path, and documentation still describing the old way as current. Then say plainly which step the migration is at, since "migrated" and "both still exist" are routinely reported as the same thing.

The suite has to move with the code. Behavior that survives the migration needs a test at its new home before the old one is deleted, or the contract step quietly drops its only guarantee. Call the Skill tool with "testing-strategy" for where those tests belong.

Then call the Skill tool with "verify-before-done", because "migrated" is the claim most often made while both things are still in the tree.
