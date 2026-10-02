---
name: frontend-craft
description: Build React and React Native interfaces in code that are well composed and accessible, covering component boundaries, props, and the accessibility obligations that hold at every visual choice. Use when creating or changing UI, building a component or screen, or reviewing component structure and accessibility. Takes the visual direction from design-brief and defers library choices to resolve-conventions. Not for judging whether the resulting interface is any good, which is design-review, and not for a form's validation and error-recovery behavior, which is forms.
---

# Frontend craft

Decide what an interface should look like and how its components should be shaped, then build it in whatever the project already uses. Two questions, kept separate: the design read is about the product and its audience, the composition is about the code.

The defining constraint: a component absorbs responsibilities until nothing can be changed safely, and accessibility is structural rather than cosmetic. Both failures come from deferring a decision, and both are far cheaper to make now than to retrofit: a prop added today multiplies the states of the component forever, and an element chosen wrongly is a rewrite rather than an attribute.

## Take the direction, do not invent it

This skill builds; it does not decide what the thing should look like. Call the Skill tool with "design-brief" for the read (surface kind, audience, references, dials, and the constraints that override taste), and with "design-inspiration" where the user has named a product or linked a reference. Where the project already has a design system, that is the direction and the brief will say so.

Build to the read, and say which part of it a decision came from when it is not obvious. An interface built with no read lands on the generated default, which is the failure the brief exists to prevent.

## Compose the components

- **A component owns one reason to change.** When a component fetches, decides, and renders, those three reasons collide in one file. Keep data access at the edge of a screen and let the pieces below it take what they need as props.
- **Compose rather than configure.** A component that has accumulated boolean props to cover variants has become a switchboard. Prefer smaller pieces the caller assembles, and reserve props for genuine data.
- **Keep the public surface small.** A component's props are its contract, so expose what a caller must decide and hide the rest. This is module depth applied to UI: call the Skill tool with "ts-standards" for the underlying principle.
- **Ask the platform first.** A container query, `:has()`, `color-mix()` or `text-wrap: balance` replaces a surprising amount of component JavaScript and several dependencies. When a platform CSS feature would replace component JavaScript, read [modern-css.md](modern-css.md) (the answer sheet for rung 4 of the ladder in `create`).
- **Split when a reason appears, not in advance.** A long component that does one thing is fine. Extract when a piece is reused, or when a part changes for reasons the rest does not.
- **State is a separate question.** Call the Skill tool with "state-management" for where a piece of state lives. Do not settle it inside a component by reflex.

## Accessibility is part of building it

Not a pass at the end, because the things that go wrong are structural and expensive to retrofit.

- **Semantic elements before ARIA.** A real button, link, label, heading, and list carry keyboard behavior, focus handling, and screen reader semantics for free. ARIA is for what the platform does not express, and a wrong ARIA attribute is worse than none.
- **Everything reachable by keyboard**, in an order that matches the visual one, with a focus indicator that is actually visible. Anything that traps focus, such as a modal, returns it where it came from.
- **Every control has an accessible name**, and every input has a real label rather than a placeholder standing in for one.
- **Contrast and target size meet the numbers.** When checking contrast or target size, the numbers are in [design-defaults.md](design-defaults.md). These are not preferences, and they are the easiest thing to get right at build time.
- **Let the machine catch what it can.** Most of the list above is checkable by a linter or by `axe` in CI, and anything checkable should be a gate rather than a thing someone notices later. When deciding which accessibility obligations a linter or axe should gate, the tiers are in [a11y-baseline.md](a11y-baseline.md).
- **Never signal with colour alone**, and honour a reduced-motion preference. On React Native the same obligations run through the accessibility props rather than through semantic tags.

## Rules

- **Build to a read you did not invent.** Where none exists, get one from `design-brief` before styling anything.
- **Follow the project's system.** An existing component, token, or pattern beats a better one you introduce alone. Consistency is most of what makes an interface feel designed.
- **The library comes from the project.** Styling approach, component library and icon set are resolved, never assumed.
- **Accessibility is not negotiable against aesthetics.** Where a visual choice breaks contrast, keyboard access, or a target size, the visual choice changes.
- **Show, do not describe.** When a direction is uncertain, build the smallest real version and let the user look at it. Where several directions are worth comparing, build them side by side behind one route rather than describing the difference.

## Trust and failures a user can hit

Call the Skill tool with "security-hardening" when this change can put a token, secret, or raw HTML in the client, or an error might render server text. Otherwise skip it. Call the Skill tool with "observability" when the user can hit a failed submit, a failed route, or a crash, and apply the client moment-0 baseline unless that failure is already reported.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "Accessibility can come in a later pass" | The expensive parts are structural: element choice, focus order, labelling. A later pass rewrites markup rather than adding attributes |
| "There is no design, so I will just make it look good" | "Good" with no read is the generated default. Getting a read is one sentence of work, and it belongs to `design-brief` |
| "One more boolean prop is quicker than splitting this" | It is quicker this once, and each one multiplies the states the component can be in, which is why it eventually cannot be changed at all |

## When this does not apply

A copy change, a bug fix inside existing markup, and a screen that follows an established pattern exactly do not need a design read. Skip it where the decision is already made and your job is to match. Skip the composition guidance where you are editing a component rather than shaping one.

The accessibility obligations do not have an exception. They are the part that yields to nothing, because the cost of adding them later is a rewrite and the cost of getting them wrong is falling on the user.

## Before you hand it over

Check the interface for the three failures that most often survive: a control that cannot be reached or operated by keyboard, an input whose only label is its placeholder, and a component that grew a new boolean prop instead of being split.

For anything user-facing about to ship, call the Skill tool with "design-review" for a scored pass.

Then call the Skill tool with "verify-before-done", because a component that renders in front of you is the weakest possible evidence that it still builds, still type-checks, and still passes the tests around it.
