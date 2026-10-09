---
name: debug
description: Find why a JS/TS, React, or React Native behavior is wrong when the cause is unknown. Use when a test, request, screen, or job fails, the user asks why something is broken, or a failure started after a change. Reproduce first, then one hypothesis at a time. Not for a behavior-preserving restructure, which is refactor, not for proving a known fix is done, which is verify-before-done, not for a production incident still in progress, which is mitigate-incident, and not for a measured slow path, which is perf-audit.
---

# Debug

Find why something is wrong, then change the smallest thing that removes the cause. The output is a fix that is pinned, plus any signal the failing path should already have emitted.

The defining constraint: do not start editing until the failure is reproducible. A change made against a failure you cannot trigger again is a guess, and a guess that happens to pass leaves the next person with neither the bug nor the evidence.

## Reproduce before you touch it

Write the failing observation in one line: what you did, what you expected, what happened. Then make the smallest reproduction that shows it. A failing test, a single request, or one sequence on a screen is enough. If you cannot reproduce it, you do not have a fix yet, and editing the code will not create one.

When there is no local reproduction and the only evidence is production, call the Skill tool with "observability" and read the signals that already exist. Do not invent a local theory that the logs contradict.

## One cause at a time

Bisect before you hypothesize. Narrow the failure to an input, a layer, or a recent change, and say which of the three you are cutting.

Then state one hypothesis, the observation that would confirm it, and the observation that would kill it. Run that check. A hypothesis that survives becomes the next cut. A hypothesis you did not state is a print statement you will not know how to read.

Fix the cause, not the symptom. Swallowing the error, retrying forever, or special-casing the one input that failed leaves the path broken for the next input.

## Pin it, then backfill the signal

Call the Skill tool with "testing-strategy" for the seam that holds the failure. The pinning test is red on the old behavior and green after the fix. A fix with no pin is a fix the next change can undo silently.

This skill does not give new code its first logs, spans, or traces. Those land when the path is created. On a path you are already fixing, backfill only what is missing from the baseline: a failure log with the operation, the error, and a correlation id; a span across the boundary that failed; the aggregate rate, errors, and duration when the operation had none. Skip a signal the project already emits. Call the Skill tool with "observability" for how to emit it, and do not log a secret or personal data.

## Rules

- **Reproduction first.** No edit until the failure can be triggered on demand, or the production evidence has been read.
- **One hypothesis, then a check.** Parallel theories produce a diff nobody can explain.
- **The smallest change that removes the cause.** A cleanup bundled into the fix is a second change. A behavior-preserving restructure belongs to `refactor`, done separately.
- **New production paths are instrumented where they are created**, in `create`, `api-design`, `frontend-craft`, or `forms`. This skill only fills a hole on a path that already shipped silent.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "I will add some logs and poke around" | Unscoped prints are a hypothesis you never wrote down. State the check, or you will not know what the output means |
| "I know this code, the cause is obvious" | Then the reproduction is cheap, and it is the thing that proves the obvious cause is the actual one |
| "I will tidy the surrounding code while I am here" | The tidy change hides the fix in the diff and can itself be the next bug |

## When this does not apply

A failure whose cause is already known, and whose remaining job is to prove the fix, does not need this loop. A one-line typo you can see does not either. A production system that is still hurting users is an incident, not a local debugging session.

The shape survives where the rule yields. On a known cause, still name the observation that confirmed it, so the fix is attached to evidence.

## Before you hand it over

Check three things: the failure was reproduced before the edit, the change removes the cause rather than hiding the error, and a silent path you touched now emits the missing baseline signal.

Then call the Skill tool with "verify-before-done", because "fixed" is a claim about a path that was failing, and only a fresh run of the pinning check says it stopped.
