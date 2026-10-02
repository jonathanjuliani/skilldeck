---
name: verify-before-done
description: Turn a task into a verifiable criterion before starting, and prove that criterion with fresh command output before claiming the work is done, fixed, passing, or ready. Use whenever a task is about to be handed back, before committing, opening a PR, or reporting a fix, and whenever a claim about tests, builds, types, or behavior is about to be made. Not for finding an unknown cause, which is debug, not for choosing which seams to test or what kind of test to write, which is testing-strategy, and not for explaining or exploring, where no claim is being made.
---

# Verify before done

Decide what would prove this task is finished before starting it, then produce that proof before saying it is finished. This skill sits at both ends of a piece of work: it sets the criterion at the start and enforces it at the end.

The defining constraint: a claim about the state of the code is only as good as the command output backing it, and that output has to be from this run. Nothing else counts. Not the code looking right, not a previous green run, not a subagent reporting success, not the strength of your own conviction. Confidence is not evidence, and the gap between them is where broken work gets handed over.

## Set the criterion first

A task phrased as an intention cannot be verified, so convert it into an observable outcome before any code is written. "Add validation" becomes "invalid payloads return a 400 with the error shape, proven by a test that fails today". "Fix the bug" becomes "a test reproducing the reported symptom fails now and passes after". "Speed it up" becomes a number and the command that measures it.

Do this at the start, out loud, in one line. A criterion invented after the work is finished tends to be the criterion the work already meets.

For multi-step work, pair each step with its check as you plan it, so a step cannot be marked done on the strength of having been attempted.

## The tests are part of the change, not a follow-up

A suite that never covered the thing you changed cannot report on it, so the state of the tests is a precondition of the gate rather than a separate chore:

- **Look for the test before assuming either way.** Find whether a test already exists at the seam this change touches. Assuming there is one is how an untested path ships; assuming there is not is how a duplicate lands next to the one that was already there.
- **If nothing covers it, write the test.** At the public boundary the change is observable from, in the project's runner, asserting the behavior rather than the implementation.
- **If behavior changed, the tests asserting the old behavior are now wrong.** Update them in the same change. A test left failing because "it tests the old way" is an unfinished change, not a known issue.
- **Deleting, skipping, or loosening a failing test is not reaching green.** Where that is genuinely the right call, say so out loud and say why, because it is a decision about coverage and not a step in getting to a pass.

Both of the last two are how a green suite stops meaning anything: the assertion still runs, and it no longer describes the system.

## Resolve the commands from the project

The commands that constitute proof come from the repository, never from habit. Call the Skill tool with "resolve-conventions" to learn the project's test runner, type checker, linter, and build, and run what the project actually wires up in its scripts. Running `vitest` in a Jest repo proves nothing about that repo, and inventing a command that does not exist produces an error you may misread as a failure of the code.

## The gate

Before any statement that work is complete, fixed, passing, green, or ready:

1. **Name the claim.** What exactly are you asserting?
2. **Name the command that proves it.** If no command can prove it, the claim is an opinion, so label it as one.
3. **Run it fresh and in full.** Not a filtered subset, not a remembered result from earlier in the session. The full command, now.
4. **Read the whole output.** Exit code, failure count, and any error text. A suite that reports passes while exiting non-zero has not passed.
5. **Compare the output against the claim.** They are frequently narrower than each other. Passing unit tests do not establish that the original symptom is gone.
6. **Walk the criterion you set at the start**, item by item, against what the output actually shows. Not the suite being green: the specific outcome you said would prove this task finished, plus anything the request asked for that the criterion missed.
7. **State the claim with its evidence**, or state the real status instead.

The steps that get skipped are 5 and 6, and they fail differently. Running the command and glancing at green is not the same as checking that green answers the question you were asked, which is 5. And a suite that answers the question you were asked is still not the whole of what you were asked for, which is 6. Work finished against a criterion nobody rechecked tends to be work finished against the half of it you remembered.

## What each claim actually requires

| Claim | What proves it | What does not |
| --- | --- | --- |
| Tests pass | Full suite output this run, zero failures, exit 0 | An earlier run, a filtered subset, the tests you happened to write |
| Types are clean | The project's type check, exit 0 | The editor showing no squiggles, the linter passing |
| Build succeeds | The build command, exit 0 | Types passing, dev server starting |
| The bug is fixed | A test reproducing the reported symptom, failing before and passing after | Changed code that looks correct, a passing suite that never covered it |
| The regression test works | Seen failing before the fix, passing after | Passing once, after the fix |
| Performance improved | The same measurement as the baseline, re-run | A change that should be faster |
| A subagent finished | The diff, and the checks re-run yourself | The subagent reporting success |
| Requirements are met | Each criterion walked and matched | The suite being green |
| Behavior changed as intended | A test asserting the new behavior, plus the old assertions updated to match | The old tests deleted, skipped, or loosened until the suite passes |
| This change is covered | A test at the seam it touches, failing without the change | A green suite that never exercised the path you edited |

## Persistence

This gate applies to every claim for the rest of the session, not only the first one. It does not lapse when the task changes or when a session runs long, and the temptation to skip it grows precisely as fatigue and time pressure grow. If you are unsure whether it still applies, it does.

It stops applying when the user says to stop verifying, and the user is entitled to say that. Confirm in one line and continue.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It should work now" | Then the command will confirm it, and running it costs seconds |
| "The linter passed" | A linter reads style, not types, and neither reads behavior |
| "I ran it a few messages ago" | The code has changed since; that is why you are claiming something new |
| "The subagent said it succeeded" | You are relaying a claim you did not verify, under your own name |
| "It is a one-line change" | One-line changes are where unrun tests hide, because nobody expects them to break |
| "That test was already failing before I started" | Then say so and show it failing on the base commit. Otherwise it is your failure now, and "pre-existing" is the easiest thing in the world to assume |
| "That test asserts the old behavior, so it can go" | The behavior changed, so the assertion changes. Deleting it removes the only thing that would have caught the change going wrong |

## When this does not apply

Not every exchange makes a claim about the state of the code. Skip the gate when explaining, exploring, reading, or answering a question, and when producing work that has no executable check at all, such as a plan or a brief. In those cases there is nothing to run, and inventing a ritual around it wastes the user's time.

The gate also yields when the user explicitly asks for an unverified draft, or when the verification is genuinely unavailable (no runner is configured at all, the build needs credentials you do not have). An existing runner with no test covering your change is not that case: that is the test you write. Then the shape survives even though the rule yields: say plainly what you could not verify and what it would take, rather than quietly upgrading an assumption into a claim.

## Rules

- **No completion claim without fresh output.** If the command did not run in this exchange, the claim is not available to you.
- **Hedging is not a substitute for running it.** "Should pass" and "seems fixed" are the sound of a skipped verification, not a softer claim.
- **Report the real status when it is bad.** A failing suite reported honestly is worth more than a green one asserted falsely, and costs the user far less later.
- **Verify a delegate's work yourself.** Any claim you pass on becomes yours.
- **The commands come from the project.** Resolve them rather than assuming them, so the proof is proof about this repository.
