# Accessibility baseline

What a machine catches, what it cannot, and where each belongs. The point of this split is budget: a human review that spends its attention on a missing `alt` has not looked at the things only a human can see.

Snapshot date: 2026-09. The tools move; the three tiers do not.

## Tier 1: static, caught at lint time

`eslint-plugin-jsx-a11y` for React and React Native, or the equivalent for the project's linter, resolved via `resolve-conventions`. These are markup mistakes visible without running anything:

- An image without alternative text, or a decorative image not marked as such.
- An interactive handler on a non-interactive element (`onClick` on a `div`) with no role and no keyboard handler.
- A form control with no associated label.
- An anchor with no href, or a button whose only content is an icon with no accessible name.
- A positive `tabindex`, which reorders focus away from the document.
- An ARIA attribute that does not exist, or one applied to a role that does not accept it.
- A heading level skipped in source order.

Wire this into the same gate as the rest of the lint. Call the Skill tool with "ship-flow": a check that warns is a check that is ignored.

## Tier 2: runtime, caught in a test or in CI

`axe-core`, driven from the project's test runner or through Playwright, plus Lighthouse for a page-level pass. These need a rendered page because they are computed rather than written:

- Colour contrast, text and non-text, against the actual painted background.
- Target sizes.
- Accessible names as the browser computes them, including through composition.
- Landmark structure, duplicated or missing.
- Focus visibility on real focus.
- Language attributes, frame titles, table header association.

Run it on the handful of screens that matter and on any new user-facing surface, not on everything. Coverage here is a diagnostic, exactly as it is for tests.

## Tier 3: judgement, no tool will ever catch it

This is what a design review is for. Call the Skill tool with "design-review" to score these; do not expect a linter to raise them.

- **Focus order matching the visual order.** A tool confirms focus is reachable, never that the sequence makes sense.
- **Whether alternative text is useful.** "image" passes every check and tells the reader nothing.
- **Whether colour is the only signal.** Contrast can pass while hue carries the entire meaning.
- **Whether an error message is actionable.** Present, associated, and still useless is the common case.
- **Whether the reduced-motion path is equivalent** rather than merely shorter or missing.
- **Whether the empty, loading, error and partial states exist at all.** Nothing flags a state nobody built.
- **Whether the copy is readable** by the audience the brief named.

## The rule this file exists for

**Never spend review attention on tier 1 or tier 2.** If those findings reach a human, the gate is missing, and adding the gate is the fix rather than reporting the finding again. A review's whole value is tier 3, and tier 3 is invisible while the obvious things are still red.
