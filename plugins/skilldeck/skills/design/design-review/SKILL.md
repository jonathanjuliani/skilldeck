---
name: design-review
description: Critique an interface against usability heuristics and its own design read, scoring each finding and ranking by user impact so the output is an actionable list rather than an opinion. Use when reviewing a screen or flow, when asked whether a UI is any good, before shipping a user-facing change, or when an interface works but feels wrong and nobody can say why. Not for building or fixing the component itself, which is frontend-craft, and not for the static and computed accessibility failures a linter or axe should already gate.
---

# Design review

Judge an interface against named heuristics and produce a scored list someone can act on. This is the review counterpart to a code review, which reads the diff and says nothing about whether the result is usable. Claude Code ships `/code-review` for that half.

The defining constraint: a finding without a score and an impact is an opinion, and opinions about design get argued rather than fixed. Every finding here names the heuristic it violates, scores it, and states who it hurts and how, which converts "I don't like this" into a row a team can prioritise or reject on the record.

## Score against the read first

Call the Skill tool with "design-brief" for the read, or reconstruct it if none exists. Half of what looks wrong in an interface is not a usability defect, it is a mismatch: a marketing hero on an operations tool, motion at a density meant for scanning, a consumer aesthetic in front of a procurement committee.

Judge fidelity to the read before anything else, because a screen that fails the read needs a different design rather than a list of fixes.

## Then score the heuristics

Ten heuristics, each scored 1 to 5. The rubric is fixed:

| Score | Meaning |
| --- | --- |
| 1 | Blocks the user. The task cannot be completed |
| 2 | Severe friction. Users abandon, or repeat the error |
| 3 | Works but confusing. Completed with hesitation |
| 4 | Works, minor polish outstanding. No user impact |
| 5 | Nothing to add |

The ten, and what to look for in each, are in [heuristics.md](heuristics.md). Read it when you are scoring the ten, not before you have judged fidelity to the read.

**The dials do not move these scores.** Variance, motion and density are aesthetic choices; a 2 is a 2 on a playful marketing page and on a regulated dashboard. Accessibility findings in particular are never traded against a visual decision.

## Output

One table, ranked by impact rather than by heuristic order, so the first row is the thing to fix:

```text
| Heuristic | Score | Finding | Impact |
| --- | --- | --- | --- |
| Error prevention | 2 | Delete has no confirm and no undo | Any operator can destroy a record by mis-clicking; unrecoverable |
| Visibility of status | 2 | Submit gives no feedback for ~3s | Users click repeatedly, creating duplicate records |
| Consistency | 3 | Three button heights across the flow | Reads as unfinished; no task blocked |
```

Then two lines: what to fix first, and what you are deliberately not raising. A review that lists everything at equal weight has done the ranking work and thrown it away.

State what you could not assess. A review from reading code has not seen the interface run; say so rather than implying you did. Where the project can be launched, launch it. A screenshot answers questions that source cannot, and Claude Code ships a `/run` skill for exactly this.

## Rules

- **Every finding scores.** Unscored observations are the ones that get ignored, and they should be.
- **Impact is about the user, not the code.** "This component is duplicated" is a code-review finding. "The user cannot tell the save failed" is this one.
- **Rank, then cut.** Findings at 4 belong in a single closing line, not in the table.
- **Accessibility does not negotiate.** It is scored on the same rubric and never discounted for an aesthetic reason.
- **Judge the read before the pixels.** A faithful execution of a wrong read is not a good interface.
- **Say what you did not see.** A review of source is not a review of behaviour.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It looks fine to me" | You are not the audience, and you know where everything is because you just built it |
| "That is subjective" | Then it is not a finding. Score it against a named heuristic or drop it |
| "The design is intentional, so the score does not apply" | Intent explains a choice, it does not remove its cost. Record the score and the intent, and let the team decide |
| "Accessibility is a separate pass" | A separate pass is a deferred pass. It is scored here, on this rubric, like everything else |

## When this does not apply

Skip it for a copy change, a screen that follows an established pattern exactly, and anything with no user-facing surface. Reach for it before shipping something people will use, and when a screen works but feels wrong, which is what the read check is for.

A full ten-heuristic pass is too much for a single component. Score the heuristics that plausibly apply and say which you skipped.

## Before you hand it over

Check the review for the three ways it stops being useful: a finding with no score, an impact written about the codebase instead of the user, and a table where nothing is ranked so everything reads as equally urgent.
