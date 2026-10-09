---
name: plan-delivery
description: Sequence a set of asks or features into phases by value versus effort, with a thin first slice, milestones, and explicit cut lines.
disable-model-invocation: true
---

# Plan delivery

Act as a delivery manager: take a pile of asks and turn it into a sequenced plan that ships value early and often. The output is a phased plan, ordered by value against effort, with a thin first slice and clear lines for what to cut under pressure.

The defining constraint: this skill plans sequence, not solution. It assumes the problem is understood and each item's shape is roughly known; its job is deciding what to build first, next, and never, not how to build any one thing.

## Inputs it needs

- The list of asks or features. If they are vague, run `/investigate-product` on the fuzzy ones first, or ask the user to sharpen them.
- A rough sense of value and effort per item. Draw value from the problem briefs and evidence; draw effort from the codebase and the user's estimate. Precision is not the goal; relative ranking is.

## The method

1. **List the candidates.** One line each: what it delivers and for whom.
2. **Score value and effort.** Rate each on value (impact on the user problem and its size) and effort (build cost, risk, unknowns), high/medium/low is enough. State the reasoning in a few words; a score without a why is noise.
3. **Rank by value against effort.** High-value, low-effort items lead. High-value, high-effort items get broken down until a high-value, low-effort slice falls out. Low-value, high-effort items go to a "not now" list, named explicitly so they are decisions, not omissions.
4. **Find the thin first slice.** The smallest end-to-end piece that delivers real value and de-risks the biggest unknown. It should be shippable on its own and teach the team something that reshapes the rest.
5. **Phase the rest.** Group the remaining work into a few phases, each ending at a milestone that is independently valuable (a user can do something new, a metric can move). Order phases so risk and learning come early, polish comes late.
6. **Draw the cut lines.** For each phase, state what gets cut first if time runs short, and what is non-negotiable. A plan without cut lines collapses the moment a deadline slips.

## The plan document

Produce: a ranked candidate table (item, value, effort, note), the **thin first slice** called out on its own, then **phases** with their milestone and cut line each, and a **not now** list with reasons. Keep it scannable.

## Rules

- **Value early.** Prefer many small shippable slices over one big reveal. Reordering for earlier value beats optimizing throughput.
- **Effort estimates are relative and revisable.** Do not pretend to precision. Re-rank as the first slices teach you the real costs.
- **"Not now" is a decision, not a gap.** Name what you are deliberately not doing and why, so it is a choice the team owns.
- **De-risk first.** When two items have similar value-per-effort, do the one that resolves the larger unknown first.
- **No solutioning.** If an item's approach is genuinely unknown, that is an effort risk to flag, not a design to invent here.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The estimates are too uncertain to rank" | Ranking needs relative order, not precision, and the uncertainty is itself an input: the uncertain item is the one to de-risk first |
| "Everything here is high priority" | Then nothing is sequenced, and the order gets set later by whoever is loudest. Force the ranking |

## When this does not apply

Two or three items in an obvious order do not need a plan. This skill earns its cost when the set is large enough that the sequence is genuinely contested, or when someone will have to cut scope under time pressure.

## Before you hand it over

Check the plan for the three things that make it collapse in practice: a first slice that is not actually shippable on its own, a phase with no cut line, and a "not now" list that quietly omits an item instead of deciding against it.

## Where it fits

Feed it briefs from `/investigate-product`. Its output feeds ticket-writing: hand the phased plan to whatever writes tickets in your setup, one per slice, each carrying the slice's value and its cut line.
