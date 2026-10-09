---
name: forms
description: Build a form that people can actually complete, covering labels, validation timing, error recovery, submit states, required fields, autofill, mobile input, and multi-step flows. Use when adding or changing any input, form, or checkout flow, or when users abandon a form, mistype into it, or lose what they typed. Not for general component composition and accessibility, which is frontend-craft, and not for a single search box, toggle, or inline edit of one value.
---

# Forms

Get information out of a person and into the system without losing either the data or the person. Forms carry more failure modes per line of code than anything else in a UI, and most of them are decided in the first ten minutes of building one.

The defining constraint: the form's job is completion, not collection. Every field, every rule, and every validation moment is a place someone leaves, so each one has to earn its cost against the question "does the task fail without this". A form that collects perfect data from the third of people who finished it has not done its job.

## Ask for less

The cheapest fix for every problem below is the field that is not there.

- **Cut anything you do not act on.** A field nobody reads is pure abandonment with no upside. This is the YAGNI ladder applied to input: call the Skill tool with "create" for the general form of that argument.
- **Derive rather than ask.** Country from locale, city from postcode, currency from account. Ask only what cannot be inferred, and let the person correct the inference.
- **Split by obligation, not by tidiness.** Required now, optional now, later in settings. Anything that can wait should wait.
- **One column.** Side-by-side fields break the scan and are read in the wrong order more often than people expect. Pair only genuinely paired values, like expiry month and year.

## Label and describe

- **Every input has a real, persistent label.** A placeholder is not a label: it disappears exactly when the person needs it, takes the only description of the field with it, and is invisible to anyone reviewing a filled form.
- **Format guidance sits outside the input**, visible before typing and while typing. "DD/MM/YYYY" as placeholder text vanishes at the keystroke it was meant to guide.
- **Mark optional, not required**, when most fields are required. Marking every field with an asterisk carries no information.
- **The label says what the value is for**, in the domain's own words. Where a `CONTEXT.md` exists, its vocabulary wins.

## Validate at the right moment

Timing is most of the experience, and getting it wrong is the single most common form defect.

- **Never validate a field the person has not finished.** Marking an email invalid at the second character is the interface arguing with someone who is still typing.
- **Validate on blur, after the first interaction with that field.** Then, once a field has been marked invalid, revalidate as they type, so the error clears the moment it is fixed rather than at the next blur.
- **Validate on submit for everything**, including what the client cannot know.
- **Accept generously, normalise quietly.** Spaces in a card number, a phone number with or without the country code, a pasted value with trailing whitespace. Rejecting a format you could have parsed is the interface making its problem into theirs.
- **The client's rules and the server's are the same rules.** Share the schema rather than writing it twice: call the Skill tool with "api-design" for the contract, and "resolve-conventions" for the validation library. Two implementations drift, and the drift shows up as an error the form said would not happen.

## Fail without punishing

- **Never clear the form.** Losing typed input on a failed submit is the worst thing a form can do, and it is still common. Preserve everything, including what was invalid.
- **The message sits next to the field it concerns**, says what is wrong and what to do, and is associated with the input so a screen reader reaches it.
- **A summary at the top for a long form**, with each entry linking to its field, in addition to the per-field messages rather than instead of them.
- **Move focus to the first error** on a failed submit, so the person is not hunting.
- **Server errors land in the same place as client errors.** A person does not care which side rejected them.

## Submit exactly once

- **Disable on submit and say why**, with the button showing progress. Otherwise it is clicked three times and three records exist.
- **Make it idempotent on the server** anyway, because the network will retry and a double-submit will get through. Call the Skill tool with "api-design" for idempotency keys.
- **Confirm success visibly**, and say what happens next. A form that clears itself silently leaves people wondering whether it worked.
- **Guard against losing work** on navigation away from a long, dirty form.

## Meet the platform

- **Correct input types and `autocomplete` values.** These drive the mobile keyboard and the browser's autofill, and getting them right is close to free while getting them wrong makes a phone form miserable. A numeric field that raises a full alphabetic keyboard is a wrong input type.
- **Never block paste.** Especially on passwords and codes; it defeats password managers and prevents nothing.
- **Native controls first.** A native date input, select, or file picker brings keyboard support, mobile behaviour and accessibility for free. Replace one only when a real requirement forces it, and then own everything it was giving you.
- **The form works with the keyboard alone**, submits on Enter from a text input, and shows focus at every step.

## Multi-step

- **Show where they are and how much is left.** An unbounded flow reads as endless.
- **Persist between steps**, so back does not destroy the previous answers, and a reload does not restart the flow.
- **Validate each step at its own boundary**, not everything at the end.
- **Review before anything irreversible**, showing what will happen with a way back to change it.

## Rules

- **Fewer fields beats better fields.** Every one is a place someone stops.
- **The label never disappears.** Placeholders are hints, never names.
- **Never destroy typed input.** No exception is worth it.
- **One schema, both sides.** Client validation is a convenience layer over the server's rules, never a second set of them.
- **Native before custom.** A rebuilt control starts by losing everything the platform gave you.

## Trust and the failed submit

Call the Skill tool with "security-hardening" when the form can put a token or secret in the client, or an error might render server text. Call the Skill tool with "observability" for the client moment-0 baseline on a submit the user can fail. Skip both for a control that never leaves the device.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The placeholder is clear enough as a label" | It is clear until they click, which is the moment they need it. It also fails review, autofill and screen readers |
| "We validate on the server, so the client can be loose" | Then the person finds out after submitting, having waited, and often having lost the input |
| "It is a strict format, so we reject anything else" | You could have parsed the spaces out. Every rejected-but-parseable value is an abandonment you chose |
| "One more field is not much" | Each field measurably costs completion, and this is the reasoning that produced the form nobody finishes |

## When this does not apply

A single search input, a toggle, and an inline edit of one value are not forms in this sense. Reach for this at anything with several fields, anything that submits to a server, and anything a person could abandon partway.

Where the project has a form library and an established pattern, follow it. Consistency across forms matters more than any single improvement here, since people learn one form and expect the next.

## Before you hand it over

Fill the form in as a hostile user: submit it empty, submit it half-complete, paste into every field, get one field wrong and fix it, submit twice fast, and complete it with the keyboard alone. Then check the three that survive most often: input lost on a failed submit, a placeholder doing a label's job, and validation firing while the person is still typing.

That pass is manual, so it proves the form once and protects it never. The paths worth pinning are the ones you just walked by hand: a rejected submit that keeps what was typed, and a field that validates when it should. Call the Skill tool with "testing-strategy" for the seam those belong at.

Then call the Skill tool with "verify-before-done", because a form is easy to declare working from the one path you happened to complete.
