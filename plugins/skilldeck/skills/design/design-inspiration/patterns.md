# Patterns

Conventions abstracted from mature production interfaces, recorded as decisions rather than as measurements. Nothing here is one product's identity: where a pattern is specific enough to be recognisable as somebody's, it is named as a signature and left out.

Snapshot date: 2026-09. Convention drifts, so verify anything that carries real weight against current examples. The project outranks this file everywhere.

**Read the last section first.** "What shipped interfaces avoid" carries more signal than the rest combined, because it is mostly a list of what gets generated when nobody decided anything.

## Conventions worth reusing

Patterns widespread enough that departing from them costs the user something.

| Convention | Why it holds |
| --- | --- |
| Real product over illustration | A screenshot with plausible data proves the thing exists. Abstract graphics and mascots say nothing and read as a placeholder for a product that is not ready |
| Specific numbers over adjectives | "Cut the build from seven minutes to forty seconds" is checkable. "Blazing fast" is noise the reader has learned to skip |
| One primary action per view | Two equally weighted calls to action halve each other. Rank them, and make the secondary visibly secondary |
| Navigation that says where you are | Active state, breadcrumb, selected row. Cheap to add and the first thing missed when it is absent |
| Empty states that teach | The first screen a new user sees is usually the empty one. It should say what goes here and offer the action that fills it |
| Errors next to their cause | A message at the top of a form about a field at the bottom makes the user hunt. Say what is wrong, where, and how to fix it |
| A visible spacing scale | Consistent multiples of one base read as deliberate. Arbitrary values read as unfinished, even to people who cannot name why |

## Archetypes to choose between

These are shapes, not styles, and picking one deliberately is the point. Each suits a different read: see the `design-brief` skill.

**Landing and marketing**

- **Text-led.** Headline, subhead, one action, generous space, no imagery. Highest trust per pixel, and the hardest to do because the copy carries everything.
- **Product-led.** A large, real interface screenshot as the main visual. Best where the product is visually legible and the audience is technical.
- **Asymmetric.** Headline on one side, product or figure on the other, off-centre. More energy, and it needs real typographic control to avoid looking accidental.
- **Panel grid.** Several panels of unequal size, each carrying one capability. Suits products with a handful of distinct features; degrades into a wall when there are too many.
- **Editorial.** Typography as the primary visual, long-form structure, figures between passages. Suits point-of-view content and portfolios.

**Application surfaces**

- **List and detail.** The default for anything with records. Predictable, keyboard-friendly, hard to get wrong.
- **Dense table.** For operators comparing many rows. Needs sorting, filtering, sticky headers and no wasted vertical space; every pixel of padding is a row they cannot see.
- **Focused single task.** One thing on screen, everything else removed. For checkout, onboarding steps, destructive confirmations.
- **Canvas.** Direct manipulation of a spatial artifact. Expensive to build and to make accessible; choose it only when the object really is spatial.

These shapes are independent of motion intensity. A list-detail surface can be minimal or purposeful; a landing can be text-led and still cinematic. Pick the archetype for structure, then the motion level from [motion.md](motion.md).

## Signatures to leave alone

Recognisable enough that reusing them is imitation rather than convention: a wordmark or logotype, a specific brand hue, a named signature layout, a distinctive illustration or 3D style, a proprietary typeface, a recognisable mascot, a specific hero animation. Take the reasoning underneath if it applies; leave the artifact.

## What shipped interfaces avoid

The highest-signal list here. Each of these is common in generated interfaces and rare in ones that shipped to real users.

- **A gradient standing in for a decision.** A purple-to-blue wash over a dark hero is what appears when no direction was chosen. It is not ugly, it is uninformative.
- **Three equal feature cards.** Equal weight says nothing is more important, which is almost never true. Rank them.
- **Glass and blur applied everywhere.** A treatment used once is an accent; used on every surface it is a texture that costs contrast and legibility.
- **Ambient animation with no meaning.** Anything that loops forever without explaining a change becomes noise by the tenth viewing, and an accessibility problem before that.
- **Placeholders doing a label's job.** The text vanishes on focus, taking the only description of the field with it.
- **Centred everything.** Centre-aligned body text, centred forms, centred long headings. Reads as a template and hurts scanning.
- **Lorem ipsum surviving to review.** Fake copy hides the real problem, which is that nobody has decided what the interface says. Write the plausible sentence instead.
- **Icons carrying meaning alone.** An unlabelled icon row is a guessing game, and it is invisible to a screen reader.
- **More type sizes than anyone needs.** Restrained interfaces use a handful of sizes and two weights. Every extra size weakens the hierarchy the others were establishing.
- **Colour as the only signal.** State communicated by hue alone fails for colour vision deficiency, in greyscale, and in bright sunlight.
- **A dark theme retrofitted.** Inverting a palette designed in light produces contrast failures. Define by role from the start.
- **Perfect data in every example.** Names that fit, no empty lists, no errors, no loading. The states that break a layout are the ones nobody mocked up.
