---
name: perf-audit
description: Audit and improve performance of a JS/TS backend, React web app, or React Native app. Use when something is slow, a page or screen janks, a bundle is too big, or an endpoint is over budget. Measures before changing, fixes the dominant cost first, and re-measures. Not for instrumenting a system so production questions can be answered later, which is observability, and not for restructuring code that is fast enough, which is refactor.
---

# Performance audit

Find why something is slow and fix the cost that actually dominates. Performance work goes wrong when it starts from a guess; this skill starts from a measurement and ends with one.

The defining constraint: measure before you change, and change one thing at a time. An optimization you did not measure is a guess, and a guess that adds complexity for no gain is a regression in everything but speed.

## The loop

1. **Define the budget and the symptom.** What is slow, observed how, and what would "fixed" be (a page interactive under N seconds, an endpoint under N ms, a bundle under N KB)? Without a target you cannot know when to stop.
2. **Measure.** Get real numbers with the right tool for the surface (below). Find the dominant cost: the one thing responsible for most of the gap. Amdahl's law rules here; optimizing a 5% cost is wasted motion.
3. **Fix the dominant cost.** One change, aimed at that cost. Prefer the fix that removes work over the one that does the same work faster.
4. **Re-measure.** Confirm the number moved and nothing else regressed. Then stop, or repeat for the next dominant cost if still over budget.

## Budgets when nobody has set one

Step 1 needs a number, and a project often does not have one. These are the defaults to propose, not to impose: a budget the team agreed is worth more than a good one they did not.

| Surface | Measure | Budget | Note |
| --- | --- | --- | --- |
| Web | Largest Contentful Paint | 2.5s | Field data at the 75th percentile, not a lab run on your machine |
| Web | Interaction to Next Paint | 200ms | The responsiveness measure that replaced first input delay |
| Web | Cumulative Layout Shift | 0.1 | Usually images and fonts without reserved space |
| Web | Initial JS, compressed | Around 150 to 200KB | A ceiling to argue with, not a law. Route-split before raising it |
| Backend | Endpoint latency | Set p95 and p99, never the mean | An average hides the users having the worst time, who are the ones complaining |
| Backend | Queries per request | 1 to 2 for a simple read | Anything growing with result count is the N+1 to fix first |
| Mobile | Cold start to interactive | Under 2s on a mid-range device | Measure on real hardware; a simulator on a laptop is not evidence |
| Mobile | List scrolling | No dropped frames on a mid-range device | Virtualize before optimizing anything else |

Where the project has its own budgets, service levels, or a performance clause in a contract, those replace this table entirely.

After you know the surface, read [surfaces.md](surfaces.md) for where the dominant cost usually sits and how to measure it. The loop above still applies; this is the lookup, not a substitute for measuring.

## Rules

- **No fix without a before-number.** If you cannot measure it, you cannot claim you improved it.
- **Dominant cost first.** Rank costs and fix the largest; ignore the rest until it becomes the largest.
- **One change at a time.** Batched changes make it impossible to attribute the win or the regression.
- **Do not trade correctness or clarity for a micro-gain.** Caching and concurrency add failure modes; add them only when the measured win justifies the complexity, and make the tradeoff explicit.
- **Stop at the budget.** Performance is met when the target is met. Further tuning past the budget is cost without value.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It is obvious what the bottleneck is" | Obvious bottlenecks are wrong often enough that the profession invented profilers. Measuring costs less than the wasted fix |
| "There is no time to measure" | Then there is no time to find out in a week that the change did nothing, which is the alternative |
| "It is clearly faster, so there is no need to re-measure" | Changes that are clearly faster routinely move a cost rather than remove it, and the second measurement is what tells the two apart |

## When this does not apply

Skip the loop where there is nothing to measure yet: a known-quadratic algorithm in code with no users, an obviously redundant network call in a path being written right now. Fix those and move on.

The shape survives even there. Skipping the before-number also gives up the right to claim an improvement, so describe what you changed rather than how much faster it now is.

## Before you hand it over

Check that both numbers are present and comparable: the same measurement, under the same conditions, before and after. Then call the Skill tool with "verify-before-done", because a performance claim is exactly the kind that gets asserted without fresh output.
