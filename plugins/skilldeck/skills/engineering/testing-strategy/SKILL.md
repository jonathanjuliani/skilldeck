---
name: testing-strategy
description: Decide what to test, at which seams, and with which kinds of tests (unit, integration, e2e) for a JS/TS/React/React Native project. Use when planning test coverage for a feature, deciding where a test belongs, or setting up a testing approach. Defers the runner and tools to resolve-conventions. Not for proving that a suite actually ran and passed before a completion claim, which is verify-before-done.
---

# Testing strategy

Decide where testing effort should land before writing any test: which seams matter, what kind of test covers each, and where the lines are drawn. Strategy is the plan, and the loop below executes it.

The defining constraint: you cannot test everything, so the strategy is about *choosing seams*, not maximizing coverage. Test at agreed public boundaries on the critical paths; a high coverage number over trivial code is not a strategy, it is noise.

## Pick the seams

A seam is a public boundary where behavior is observable without reaching inside. Before planning tests, name the seams and confirm them:

- **Backend:** the service or use-case layer (inputs in, outputs out, datastore faked) is the primary seam. The HTTP layer gets a thin integration test that the wiring works.
- **Frontend / mobile:** the seam is behavior a user can observe. Test a component or hook through its public props and rendered output, not its internal state.

Concentrate tests on complex logic and critical paths (the flows whose failure hurts most). Leave trivial glue and framework boilerplate untested.

## Choose the kind of test

- **Unit** for logic with clear inputs and outputs: pure functions, reducers, services with faked dependencies. Fast, many, cheap.
- **Integration** for the wiring between units: a route through to a faked datastore, a component with its real hooks and a mocked network. Fewer, higher-value.
- **End-to-end** for a handful of the most critical user journeys through the real system. Few, slow, precious; do not try to cover edge cases here.

Weight toward the base: many unit tests, fewer integration, a thin layer of e2e on the journeys that must never break. As a starting shape, roughly 80 percent unit, 15 integration, 5 end to end. Treat it as a smell detector rather than a target: a suite that inverts it is usually slow and flaky, and one that is all unit tests usually has never proven the pieces fit together.

Size matters more than the label. A test that touches no network, no database, no filesystem and no clock runs in milliseconds and can run on every save. Once a test needs any of those, it belongs in a slower tier that runs less often. Keep the fast tier genuinely fast, because a suite nobody waits for is a suite nobody runs.

## What makes a test worth keeping

- **Tests behavior, not implementation.** It survives a refactor because it exercises the public seam, not internals. A test that breaks when behavior has not changed is testing the wrong thing.
- **Independent expected values.** The assertion's expected value comes from a known-good source (a literal, a worked example, the spec), never recomputed the way the code computes it.
- **Reads like a specification.** The name states the capability ("rejects an expired invite"), so the suite doubles as documentation.
- **Descriptive beats dry.** A little duplication inside tests is worth paying for. A test that spells out its own setup can be read top to bottom and understood in isolation, while one assembled from shared factories and helpers sends the reader on a tour of four files to learn what is being asserted. Extract from tests only when the duplication actively hurts.
- **If it is worth caring about, pin it with a test.** A behavior nobody has written a test for is one that no process protects, however senior the person relying on it.

## Rules

- **Confirm seams before writing tests.** Effort lands where it was agreed, not everywhere.
- **Coverage is a diagnostic, not a target.** Use it to find untested critical paths, not to chase a percentage.
- **Mock at boundaries, not internals.** Fake the datastore or the network; do not mock the collaborators inside the unit under test.
- **The runner comes from the project.** Resolve it via resolve-conventions and match it.

## Run the loop

Once the seams are agreed, each test is written the same way, and writing the test first is what keeps it honest:

1. **Write the failing test**, at an agreed seam, asserting the behavior you want.
2. **Watch it fail, and read the failure.** A test that passes before the code exists is asserting nothing, and a failure message you did not read may be failing for a reason you did not intend.
3. **Write the least code that makes it pass.**
4. **Watch it pass**, then run the rest of the suite to confirm nothing else moved.
5. **Refactor with the test green**, if there is anything to clean up. The `refactor` skill carries that discipline, and reaches back here for the pinning test, so treat this step as the handoff point rather than a second invocation.

Then call the Skill tool with "verify-before-done" before reporting anything as covered.

For a deeper treatment of the discipline, several packs ship a dedicated TDD skill, `obra/superpowers` and `mattpocock/skills` among them. This skill covers the loop well enough to work on its own and hands off cleanly if you install one.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "Coverage is already high here" | Coverage says which lines ran, not which behavior is pinned. A critical path can be fully covered by tests that assert nothing about it |
| "I will add tests once the shape settles" | The shape settles around whatever was easy to build untested, which is rarely a testable seam |

## When this does not apply

One obvious test for one function does not need a strategy. This skill earns its cost when there is a real choice about where effort lands: a feature spanning several units, an unfamiliar area, or a suite that is expensive and not paying for itself.
