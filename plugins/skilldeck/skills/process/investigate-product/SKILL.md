---
name: investigate-product
description: Investigate the product and user problem before any solution is designed, and produce a short problem brief.
disable-model-invocation: true
---

# Investigate product

Act as a product manager: understand the problem, the user, the current behavior, and what success looks like, before a single line of solution is designed. The output is a short problem brief that a team could build against.

The defining constraint: this skill is forbidden from proposing a solution. Its entire job is to sharpen the problem. The moment it starts describing what to build, it has failed. Solutions come later, from other skills, once the problem is clear.

## The investigation

Work through these in order. Pull answers from the codebase, docs, issue trackers, analytics, and the user; ask the user only for what you cannot find yourself.

1. **The ask, restated.** What was requested, in one sentence, in the user's terms. Then the sharper question: what problem does the requester believe this solves?
2. **The user and the job.** Who has this problem, and what are they trying to accomplish (the job to be done)? A feature request is a proposed solution to someone's problem; find the problem under it.
3. **Current behavior.** What happens today? Read the existing code and product to describe the status quo concretely, including the workaround users currently rely on. "There is nothing today" is rarely true; find what people do instead.
4. **Evidence and size.** How do we know this is a real problem, and for how many? Look for support tickets, analytics, repeated requests, revenue at stake. Distinguish "one loud request" from "a measured pattern".
5. **Constraints.** Technical, regulatory, timeline, and dependency constraints that any solution must respect. Surface the ones the requester may not know about by reading the code.
6. **Success criteria.** What observable change means this is solved? A number to move, a task made possible, a step removed. If success cannot be stated observably, the problem is not yet clear enough.
7. **Risks and unknowns.** What could make this the wrong thing to build, and what is still unknown? Name the assumptions that, if false, sink the effort.

## The problem brief

Produce a short brief (aim for one page) with these headings: **Problem**, **User and job**, **Current behavior**, **Evidence and size**, **Constraints**, **Success criteria**, **Open questions**. No solution section. Keep it tight; a brief that needs scrolling has usually smuggled a solution in.

## Rules

- **No solutions.** Not in the brief, not in passing. Redirect any "we should build X" into "the problem X addresses is Y".
- **Find before you ask.** Read the code, product, and trackers first. Bring the user specific findings to confirm, not a blank questionnaire.
- **Separate signal from volume.** One insistent stakeholder is not evidence of scale. Say so plainly when the evidence is thin.
- **State assumptions as assumptions.** Anything unverified is an open question, not a fact.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The solution is obvious, so saying it saves everyone time" | It anchors the reader on your answer before the problem is agreed, which is the exact failure this skill exists to prevent. Hold it, and hand it to the design step |
| "The requester already knows the problem" | They know the problem they have. The brief exists so everyone else does too, and so the requester can see it written down and correct it |

## When this does not apply

Skip the investigation where the problem is already documented and agreed, and for a defect with a known cause, where the bug report is the problem statement. A brief that restates a settled problem costs a page and adds nothing.

## Before you hand it over

Read the brief for the two failures specific to it: a solution that crept in under a heading not called Solution, and a claim presented as fact that is actually an assumption. Anything unverified belongs under open questions.

## Where it leads

A finished brief hands off to design and delivery. When the user is ready to sequence the work, point them to `/plan-delivery`. When the brief needs pressure-testing, call the Skill tool with "align-first" for a single pass over the reading and its assumptions. For a relentless interview, `mattpocock/skills` ships `grill-me` and `grill-with-docs`.
