---
name: design-brief
description: Establish what an interface should be and for whom before anything visual is decided, covering the surface kind, the audience, the references, the dials, and the constraints that override taste. Use when starting a design, redesigning something, picking a visual direction, or when a request arrives with no stated direction at all. Not for the content, navigation and screen structure underneath the direction, which is information-architecture, and not for building the result in code, which is frontend-craft.
---

# Design brief

Decide what this surface is, who it is for, and what visual language follows from that, before a single decision about colour or layout. The output is a short read that the rest of the design work is checked against, not a document project.

The defining constraint: the audience picks the aesthetic, not preference, and not the model's default. An interface nobody made a decision about will land on whatever gets generated when nothing was decided, which is why so much of it looks the same. One paragraph of deliberate read is most of the difference.

## First, check whether this is already settled

On a project with a design system, a token set, or a consistent set of existing screens, the brief is largely decided and your job is to follow it. Call the Skill tool with "resolve-conventions" for the component library, styling approach and tokens in place, read two or three existing screens, and say in one line what the established language is. Then stop. Inventing a direction next to a working one is how a product starts looking like two products.

Reach for the full read on a new surface, a deliberate redesign, or a project whose existing screens have no language to inherit.

## The read

Six things, each answerable in a line. Pull what you can from the product, the code, and any reference the user named; ask only for what you genuinely cannot find.

1. **Surface kind.** Marketing page, product screen, internal tool, dashboard, editorial, portfolio, onboarding flow. This alone rules out most of the decision space, since a dense operations table and a pricing page share almost nothing. When the vertical is clear, also name one or two **domain tags** from design-inspiration's taxonomy (`finance`, `developer-tools`, `editorial`, and peers) so a later inspiration lookup can filter the seed without opening blog refs for a finance app.
2. **Audience, and what they are doing when they arrive.** A procurement committee comparing vendors, an operator who lives in this screen eight hours a day, a recruiter scanning for thirty seconds, a customer who is annoyed and looking for a refund. What they are doing matters more than who they are.
3. **What they already use.** People read a new interface against the ones they know. Naming the two or three products the audience uses daily tells you which conventions are invisible to them and which will feel foreign.
4. **References, and what specifically is wanted from each.** "Like Linear" is not a reference until it says which part: the density, the typography, the restraint, the keyboard-first interaction. Call the Skill tool with "design-inspiration" for how to take a reference apart without copying it, and pass the domain tag(s) from the read so it can filter. If that skill uses the inspiration store, it will confirm a task working set before opening captures.
5. **The dials.** Variance, motion and density, set from everything above. When you set those three, the mapping is in [dials.md](dials.md).
6. **Constraints that override taste.** Accessibility-critical audiences, regulated or public-sector contexts, low-bandwidth or older devices, trust-first commerce, products used by children, an existing brand you do not own. These are not inputs to be balanced against aesthetics. They win.

## State it in one line

Before any building, say the read out loud in a single sentence: **this is a `<surface kind>` for `<audience doing what>`, in a `<language>`, at `<variance>/<motion>/<density>`** (and name the domain tag when inspiration will be needed).

- "An internal reconciliation dashboard for operators who live in it all day, information-dense and keyboard-first, at low/low/high (domains: finance, ops-admin)."
- "A pricing page for a procurement committee comparing three vendors, restrained and typographic, leaning on the existing design system, at low/low/medium (domains: infrastructure)."
- "A portfolio for hiring managers scanning in thirty seconds, editorial and typographic, at high/medium/low (domains: portfolio)."

That sentence is the artifact. It is what `design-review` scores against later, and what makes a disagreement about the design a disagreement about the read rather than about taste.

## Where the surface has more than one screen

The read settles what it should feel like, not how it is organised. Where the work spans several screens that relate to each other, call the Skill tool with "information-architecture" before any visual decision: content, hierarchy, navigation, naming and flows are cheap to change now and effectively permanent once routes are public. A brief handed straight to building skips the layer that decides whether the thing is findable.

## Where the direction has to become buildable

The read decides the language; it does not produce the values. Call the Skill tool with "design-tokens" to turn it into named decisions the code can use, which is also where an extracted reference stops being a draft.

## When the read is genuinely ambiguous

Ask **one** question, not a questionnaire, and only where two plausible reads produce materially different interfaces. Where you can infer it, infer it and say so, so the user can correct one sentence instead of answering six.

## Rules

- **The audience decides.** Not your preference, not the reference the user linked, not what looks impressive in isolation.
- **Constraints outrank aesthetics.** Where a visual choice breaks an overriding constraint, the visual choice changes. There is no negotiation on that axis.
- **A reference is taken apart, never copied.** Name what you want from it and why it fits this audience.
- **Inherit before you invent.** An existing language, even an imperfect one, beats a better one introduced on one screen.
- **The brief is a paragraph.** A brief that needs scrolling has become a project, and it will not be read at the moment it matters.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "There is no design direction, so I will make it look good" | "Good" with nothing decided is the generated default. The read costs one sentence and is the entire difference |
| "The user linked a reference, so the direction is settled" | A link is not a read. Which part of it, and why it suits this audience, is the part that was skipped |
| "It is an internal tool, so it does not need a read" | Internal tools have the most demanding audience: people who use one screen for hours and pay for every wasted click |

## When this does not apply

A copy change, a bug fix inside existing markup, and a screen that follows an established pattern exactly do not need a brief. Skip it where the decision is already made and the job is to match.

## Before you hand it over

Check the read for the two ways it goes wrong: an audience described by who they are rather than what they are doing, and a reference named without saying which part of it is wanted. Both leave the read sounding complete while deciding nothing.
