# Modern CSS

What the platform now does that is still routinely rebuilt in JavaScript or in a dependency. This is rung 4 of the ladder in `create` ("does the platform do it natively?") answered for the browser, and it is where the largest easy deletions in a frontend codebase are.

Snapshot date: 2026-09. Support moves; verify anything load-bearing against current baseline data rather than against this file or against memory.

## Layout

- **Container queries.** A component that responds to its own container rather than to the viewport. This is the one that removes the most JavaScript: every `ResizeObserver` written to make a card behave differently in a sidebar is a container query now. It also makes a component genuinely portable, since it stops depending on where the page decided to put it.
- **Subgrid.** Lets a nested grid align to its parent's tracks, which is what card grids with mismatched heading and body lengths always wanted. The alternative was fixed heights or a script measuring rows.
- **`aspect-ratio`.** Reserves space before the image loads, which removes a whole class of layout shift.
- **Logical properties.** `margin-inline`, `padding-block`, `inset`. Free correctness for right-to-left, and no cost if you never internationalise.

## Selection and state

- **`:has()`.** The parent selector. A form that styles its wrapper when a child is invalid, a card that changes when it contains an image, a layout that adapts when a slot is filled. Most "add a class from JavaScript so CSS can react" code exists only because this did not.
- **`:focus-visible`.** Focus ring for keyboard users without the ring appearing on every mouse click. This is the correct answer to "the outline looks bad", not removing the outline.
- **`@media (prefers-reduced-motion)`** and `prefers-color-scheme`. Both are obligations rather than enhancements: see `a11y-baseline.md`.

## Colour and theming

- **`color-mix()`.** Derive a hover, a disabled state, or a tint from a base colour without generating a dozen variables. Pairs well with the semantic layer in `design-tokens`, since a derived state stays correct when the base changes.
- **Wide-gamut colour** (`oklch` and friends). Perceptually even ramps, which is what makes a generated neutral scale look intentional rather than muddy in the middle.
- **`@property`.** Gives a custom property a type, which makes it animatable. Gradient and shadow transitions that used to need a library.

## Structure and cascade

- **Cascade layers (`@layer`).** Order specificity explicitly instead of by accident. The main reason to reach for it is integrating a third-party stylesheet without a specificity war, or retiring one.
- **Nesting.** Native, so a preprocessor is no longer required for this alone. Nest shallowly; deep nesting reproduces the specificity problem it was meant to avoid.

## Text and content

- **`text-wrap: balance`** for headings and `pretty` for body. Removes orphans and ragged headline breaks that previously needed a script or a manual line break.
- **`line-clamp`.** Truncation to a number of lines, without measuring anything.
- **`scroll-snap`**, and scroll-driven animation where support allows. Most carousel libraries are now a few lines of CSS plus a list.

## View transitions

Animated transitions between two states or two pages, handled by the browser rather than by keeping both trees alive in JavaScript. Worth reaching for where the transition explains a change, such as a list item expanding into a detail view. Not worth reaching for as decoration, and it needs a reduced-motion path.

## How to use this list

Not as a checklist to apply. The question at rung 4 of the ladder is always "does the platform already do this", and this file exists so the answer is informed rather than remembered. Two rules make it safe:

- **Verify support for the specific thing**, at the browsers the project actually targets, using current baseline data. This file is dated and browser support is the fastest-moving fact in it.
- **Degrade rather than gate.** Most of these fail into something acceptable: a container query that does not apply leaves the default layout, `text-wrap: balance` leaves a normal wrap. Where the failure is not acceptable, it is a dependency decision like any other, so call the Skill tool with "dependency-choice".
