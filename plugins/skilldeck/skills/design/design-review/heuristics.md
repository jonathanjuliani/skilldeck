# Heuristics

The ten usability heuristics, with what to look for in each and the failure that shows up most often in generated interfaces. Adapted from Jakob Nielsen's ten usability heuristics (Nielsen Norman Group, 1994), which are the standard vocabulary for this kind of review.

Each is scored 1 to 5 on the rubric in `SKILL.md`. Score what applies and say which you skipped.

## 1. Visibility of system status

The interface always says what is going on.

Look for: every async action has a pending state; submit disables while in flight; success is confirmed rather than assumed; the current location is visible in navigation; anything past a few seconds shows progress rather than a spinner that could mean anything.

Common failure: submit with no feedback, so the user clicks three times and creates three records.

## 2. Match with the real world

The interface speaks the user's language, not the system's.

Look for: no internal jargon in user-facing copy; icons follow convention; dates and numbers formatted for the reader; error text a person can act on; consistent metaphors.

Common failure: "Entity not found" instead of "We couldn't find that project", and raw timestamps instead of relative time.

## 3. User control and freedom

Users act by mistake and need a way back.

Look for: destructive actions offer undo, or confirm when undo is impossible; multi-step flows can be exited without losing work; cancel is always available; nothing irreversible happens on a single click.

Common failure: delete with no confirm and no undo.

## 4. Consistency and standards

The same thing looks and behaves the same way throughout.

Look for: one button hierarchy; one spacing scale; consistent labels for the same concept; platform conventions honoured rather than reinvented.

Common failure: three button heights and two words for the same object across one flow.

## 5. Error prevention

Better to make the error impossible than to report it.

Look for: constrained inputs instead of free text where a set of options exists; sensible defaults; formats accepted generously and normalised; confirmation only where the action is genuinely irreversible.

Common failure: a free-text field that must match an exact format, validated only on submit.

## 6. Recognition over recall

Nothing important should have to be remembered.

Look for: options visible rather than memorised; labels persisting rather than vanishing on focus; context carried across steps; a summary before a final commit.

Common failure: a placeholder used as the only label, so the field is unlabelled the moment it is focused.

## 7. Flexibility and efficiency

Accelerators for the frequent user without burdening the new one.

Look for: keyboard access to the common path; bulk actions where a list invites them; sensible defaults that skip work; state remembered between visits where that helps.

Common failure: an operations tool where every action needs the mouse.

## 8. Aesthetic and minimalist design

Nothing competes with what matters.

Look for: one primary action per view; ranked rather than equally weighted elements; a restrained type and colour range; decoration that carries information.

Common failure: three equal feature cards, and colour applied until none of it signals anything.

## 9. Help users recognise and recover from errors

When something fails, the message is useful.

Look for: plain language; the cause named; a specific next step; the message placed next to the field or action it concerns; the user's input preserved.

Common failure: a form that clears itself on a validation error.

## 10. Help and documentation

Where help is needed, it is where the difficulty is.

Look for: guidance at the point of confusion rather than in a separate manual; empty states that teach; examples for anything with a format; nothing that requires reading documentation to complete a core task.

Common failure: an empty state that says "No items" and offers nothing.

## Accessibility, scored on the same rubric

Not a separate category and never discounted for a visual reason. The numbers are in `frontend-craft`'s design defaults; a violation there is a finding here.

Score the judgement tier here. Anything a linter or `axe` would have caught belongs in the project's gate, not in this table: see `a11y-baseline.md` in `frontend-craft` for which is which. A review reporting a missing label has found a missing gate.

Look for: semantic elements before ARIA; keyboard reachable in an order matching the visual one; a visible focus indicator; an accessible name on every control; real labels rather than placeholders; contrast and target sizes meeting the numbers; nothing signalled by colour alone; reduced-motion honoured.

Common failure: a custom control built from a `div`, unreachable by keyboard and silent to a screen reader.
