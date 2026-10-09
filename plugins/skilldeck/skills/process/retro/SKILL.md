---
name: retro
description: Run a retrospective after a delivery or phase, once any incident is stable, and turn it into durable lessons and concrete changes.
disable-model-invocation: true
---

# Retro

Look back on a piece of finished work and convert what happened into a small number of changes worth keeping. The output is not a feelings log; it is a short list of lessons, each attached to a concrete change to how the next one runs.

The defining constraint: every finding must resolve to an action or an explicit decision not to act. A retro that ends in observations changes nothing; a retro that ends in one owned change is worth the hour.

## Gather what actually happened

Reconstruct the timeline from evidence before opinion: what was planned versus what shipped, where the estimates missed, what slipped, what broke, and where time actually went. Pull from the delivery plan (the `/plan-delivery` output if there was one), the tickets, the commits, and the incident notes. Bring facts to the discussion, not vibes.

## Ask the three questions

For the work under review, answer plainly:

1. **What went well** that we should deliberately keep doing? Name it specifically enough to repeat; "good communication" is not actionable, "the daily 10-minute sync caught the API mismatch early" is.
2. **What went badly or surprised us?** The slippage, the rework, the thing nobody owned. Describe the situation and the impact without assigning blame to a person; the target is the system, not the individual.
3. **What will we change?** For each item worth acting on, one concrete change, with an owner and a place it lives (a checklist, a template, an ADR, a `CONTEXT.md` entry). Cap it: two or three real changes that happen beat ten that do not.

## Make the lessons durable

A lesson that lives only in the retro doc is forgotten by the next cycle. Land each accepted change where it will be seen at the moment it matters: a step added to a skill or checklist, a note in the project's `CONTEXT.md`, a ticket for a process fix. When the lesson is a lasting technical choice, call the Skill tool with "record-decision" and let that record be the home. Say where each one went.

A live incident is not this skill. Stabilize it first (that job is `mitigate-incident`), then run the retro once the system is calm.

## Rules

- **Blameless.** Analyze the system and the circumstances, never a person. The point is a better process, not a culprit.
- **Evidence before opinion.** Establish what happened from the record first; interpretation comes after the facts are on the table.
- **Every finding resolves.** Each becomes an action with an owner, or an explicit "we accept this, no change". No orphan observations.
- **Few changes, actually made.** Two changes that land beat a dozen that decorate a document.
- **Feed it forward.** The changes should shape the next `/plan-delivery`, closing the loop from planning to delivery to reflection.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "We will remember this next time" | The next cycle is staffed by people mid-task, not people reading this document. A lesson that is not landed somewhere is not a lesson |
| "Nothing here is actionable, it just went badly" | Then the finding is that nobody knows why, and the action is to instrument whatever would have told you |

## When this does not apply

A delivery small enough that nothing surprised anyone does not need a retro, and neither does work already reviewed in one. The trigger is a surprise worth not repeating, not the calendar.

## Before you hand it over

Check the output for the failure that makes retros ceremonial: a finding with no owner, no home, and no explicit decision to accept it. Check the count too, since a list of ten changes is a list of zero changes.
