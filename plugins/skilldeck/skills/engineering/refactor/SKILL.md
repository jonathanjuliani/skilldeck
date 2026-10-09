---
name: refactor
description: Execute a targeted, behavior-preserving refactor of existing JS/TS code to bring it in line with the project's conventions and standards. Use when the user wants to clean up, restructure, extract, rename, or de-duplicate code without changing what it does. Defers convention choices to the project. Not for work that changes behavior, not for finding why a behavior is wrong, which is debug, and not for retiring something the codebase still depends on, which is migration.
---

# Refactor

Change the shape of existing code without changing its behavior, moving it toward the project's conventions. This is the execution counterpart to a survey: a survey finds opportunities, this skill performs one cleanly.

The defining constraint: behavior is preserved and provable. Tests stay green through every step, and if the code under refactor has no tests at the seam you are changing, you add them first so the refactor has a safety net. A refactor that needs a behavior change is two changes: do the refactor first, the behavior change after, never blended.

## Before touching code

1. **State the motivation in one sentence.** "Extract the pricing logic out of the handler so it is testable." One motivation per refactor. If you find a second, note it and do it separately.
2. **Resolve the target shape.** Call the Skill tool with "ts-standards" for the conventions, and "resolve-conventions" for the project's actual posture. The target is the project's style, not an abstract ideal. Call "project-shape" when the refactor moves code between folders or modules.
3. **Understand the fence before you remove it.** Code that looks pointless usually is not. Before deleting a guard, a null check, a workaround, or an odd-looking branch, find out why it is there: `git blame`, the test that covers it, the issue it references, the bug it was added for. If you cannot find a reason, say so explicitly and treat the removal as a behavior change needing agreement, not as a refactor.
4. **Establish the safety net.** Identify the seam whose behavior must not change and confirm there is a test at it. If there is not, write one that pins current behavior before you refactor. For the discipline of writing that test first, call the Skill tool with "testing-strategy".

## The loop

Work in small, reversible steps, each keeping tests green:

- Make one structural change (extract a function, rename a symbol, split a module, remove a duplication).
- Run the tests. Green means keep; red means the step changed behavior, so revert and take a smaller step.
- Commit-sized units: each step should be something you could land on its own.

## What counts as a refactor here

- Extraction, inlining, renaming for clarity, de-duplication, splitting a wide module into a deeper one, moving code to the folder the shape dictates, tightening types (`any` to a real type, adding boundary validation).
- Not in scope: adding features, changing outputs, "while I am here" behavior tweaks. Those are separate changes with their own review.

## Rules

- **Green throughout.** If you cannot keep tests green, you are changing behavior, not refactoring.
- **One motivation.** Mixing several intentions makes the diff unreviewable and the risk uncountable.
- **Match the project, not the ideal.** Consistency with surrounding code wins over your preferred pattern.
- **Every changed line traces to the motivation.** Do not reformat, rename, or tidy code you merely happened to open. A diff carrying unrelated cleanup is harder to review and hides the real change inside it. Match the existing style even where you would have written it differently.
- **Leave breadcrumbs.** When the refactor reveals a deeper issue you are not fixing now, surface it rather than silently expanding scope. A broad survey of such issues is its own piece of work, not an extension of this one.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It is only a rename, it cannot break anything" | Renames break dynamic references, serialized values, and anything matching on the old name. Run the tests |
| "The suite is slow, so I will run it once at the end" | Then you learn that something in a batch of steps changed behavior but not which one, which defeats the reason for small steps |
| "There is no test at this seam, but the change is obviously safe" | Obvious safety is the claim the safety net exists to check. Write the pinning test, or say plainly that you are refactoring without one and get agreement |

## When this does not apply

If the change alters behavior, this is not a refactor and this skill does not govern it. Split it: refactor first, change behavior after, each with its own review.

The safety net requirement yields where a project has no test infrastructure at all and building one is a larger job than the refactor itself. The shape survives. Say so explicitly, take smaller steps than you otherwise would, and lean on types and manual verification rather than pretending the net is there.

## Before you hand it over

Check the diff for the two failures specific to refactoring: a behavior change that slipped in under the structural one, and a second motivation that crept in mid-loop. Then call the Skill tool with "verify-before-done", so that green means green now rather than green earlier.
