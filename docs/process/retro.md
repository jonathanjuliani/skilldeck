## What it does

Runs a retrospective after a delivery or phase, once any incident is stable, and turns it into a short list of durable lessons, each attached to a concrete change with an owner. It reconstructs what actually happened from the record before opinion enters.

Every finding must resolve to an action or an explicit decision not to act. It is not a feelings log; a retro that ends in observations changes nothing.

## When to reach for it

You invoke this by typing `/retro`, and the agent will not reach for it on its own. Reach for it at the end of a phase or project, or after an incident has been stabilized, when you want the next cycle to run better rather than repeat the same misses. A live incident is not this skill. It closes the loop that `/plan-delivery` opens: planning, delivery, then reflection that feeds the next plan.

## The three questions

What went well that we should deliberately keep, what went badly or surprised us, and what we will change. The first two are specific enough to repeat or avoid; the third is capped at two or three changes that will actually happen, each landed somewhere it will be seen at the right moment (a checklist, a `CONTEXT.md` entry, a ticket, a decision record). A lasting technical choice is written with `record-decision`.

## Common questions

**How is this different from just writing notes?**
Notes describe; this resolves. Each finding becomes an owned change or an explicit no-change decision, and lands where it will be seen next cycle.

**What if the work went fine?**
Then name what made it go fine, specifically, so it is repeatable. "Went well" is a lesson too when it is concrete.

**Won't this turn into blame?**
It is blameless by rule: the target is the system and the circumstances, never a person.

## Invoking it

This page writes `/retro` for brevity, but the prefix depends on how you installed. The plugin namespaces its skills, so it is `/skilldeck:retro` in Claude Code and Cursor and `@skilldeck:retro` in Codex. Installed as files with `npx skills`, it is plain `/retro`.

## It's working if

- The timeline is built from the record (tickets, commits, the plan), not memory.
- Each finding has a resolution: an action with an owner, or an explicit accept-no-change.
- The accepted changes are few and land somewhere durable, not just in the retro doc.
- The next `/plan-delivery` visibly reflects a change this retro produced.
