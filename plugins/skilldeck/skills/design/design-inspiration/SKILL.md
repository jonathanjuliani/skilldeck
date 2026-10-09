---
name: design-inspiration
description: Take a design reference apart and reuse what makes it work without copying it, covering how to read a site or screenshot for its underlying decisions, how to extract a token set from a live page, and which patterns are conventions rather than one product's signature. Use when the user names a product to look like, links a site, pastes a screenshot, or asks for a direction based on something they admire. Not for growing the reference store from galleries in bulk, which is curate-design-inspiration, and not for turning a chosen direction into a token system, which is design-tokens.
---

# Design inspiration

Turn "make it like that" into decisions you can defend. A reference is evidence about what works for an audience, and the job is to find the decision underneath the surface, not to reproduce the surface.

The defining constraint: what transfers is the *why*, never the pixels. A product's exact palette, radius and hero layout are its identity and reproducing them makes a worse version of it, while the reasoning that produced them (this audience needs to trust us quickly, so restraint and specificity beat delight) transfers to a completely different-looking result. Copy the reasoning and you get something that fits. Copy the output and you get a knockoff that fits nothing.

## Get the reference stated properly

"Like Linear" is not usable yet. Push it to a decision:

- **Which part?** The density, the typography, the restraint, the keyboard-first interaction, the motion, the copy voice. Almost nobody wants all of a reference, and the parts often conflict.
- **Why that part, for this audience?** Call the Skill tool with "design-brief" if the read is not established. A reference that suits a different audience than yours is a trap, and it is the most common way a direction goes wrong: the user admires a consumer product and is building an internal tool.
- **What is off limits?** Anything that is the reference's identity rather than its craft: the logo, the wordmark, the exact brand hue, a signature illustration style, a distinctive named layout. Reusing those is not inspiration.

## Read the reference for its decisions

Work from the surface inward, and write down what you find as convention rather than as measurement:

1. **Structure.** What is on the page, in what order, and what got left out. What a mature interface omits is usually more informative than what it includes.
2. **Hierarchy.** What your eye lands on first, second, third, and what carries that: size, weight, colour, space, or position.
3. **Density and rhythm.** How much sits in a given area, and whether the spacing follows a visible scale.
4. **Type.** How many sizes and weights are actually in use. Restrained interfaces use far fewer than people expect.
5. **Colour discipline.** How much of the surface is neutral, and what colour is reserved for.
6. **Motion.** What moves, what it explains, and how long it takes. Assign intensity from [motion.md](motion.md): **minimal**, **purposeful**, or **cinematic**. When the motion is the reason for the read, also tag **complexity** (simple, medium, high) and **types** (loading, transition, text, image, scroll). When the user asks for more motion on a surface *and* a store lookup is needed, follow [store-selection.md](store-selection.md) (it filters the seed matrix among other tiers) before opening capture files.
7. **Copy.** Whether it is specific or generic. Specificity is a design property, and it is usually the thing that makes a reference feel credible.

Then state the transferable finding in one line each: "type is two weights and four sizes, no more", not "headings are 34px Inter Semibold".

## Extract a token set when you want the mechanical part

Reading a page by eye misses the scale it is built on. Where the reference is a live public site and the user wants a concrete starting point, a token extractor gets colours, type, spacing, radii and shadows out as data. The maintained tool for this is [`extract-design-system`](https://github.com/arvindrk/extract-design-system) (MIT), installable with `npx skills add arvindrk/extract-design-system`, which emits a W3C `tokens.json` and a `tokens.css`.

Treat the output as a **starting point to edit, never a result to ship**:

- Extracted colours carry the reference's brand identity. Replace the brand hues with your own and keep the structure (how many neutrals, what the ramp looks like, what is reserved for state).
- Extracted scales are worth more than extracted values. A 4px-based spacing scale and a 1.2 type ratio transfer; that product's exact grey does not.
- Re-check contrast after any substitution. A palette that passed at the source fails the moment a hue changes. The numbers are in `frontend-craft`'s design defaults.
- An extractor reads what shipped, including that product's mistakes and its dead CSS. It is evidence, not authority.

## Capture what you found

A reference read and discarded teaches once. When you write the store entry, use the format and the rules in [capture.md](capture.md). Write the findings to the personal store at `~/.skilldeck-skills/design/references/` (or another personal path confirmed this session), one file per reference, recording what you took, **what you rejected and why**, the surface and audience it came from, domains from [taxonomy.md](taxonomy.md), optional principles, and a date.

A shipped seed lives in [references/](references/). It is the community tier of this store: starter reads that travel with the plugin. New captures go to the personal store unless the user asks to ship them. Which seed or personal entries feed *this* task is a confirmed working set, not a silent outrank.

Offer capture rather than writing silently. When this task needs the inspiration *store* (not only a named live URL, screenshot, or paste), read [store-selection.md](store-selection.md) before opening any capture; stop until the user confirms the task working set. Do not load that companion when the store is unused. After the set is locked, open at most two or three bodies and follow [capture.md](capture.md). When the accepted set is thin for this surface, audience, and domain, or the user wants the base updated from galleries, Call the Skill tool with "curate-design-inspiration" (it will confirm before any crawl or write).

## Know convention from signature

The most useful distinction in this skill. A **convention** is a pattern so widespread that departing from it costs the user; reuse it freely. A **signature** is one product's recognisable choice; reusing it is imitation.

[patterns.md](patterns.md) records the conventions worth reusing, the archetypes worth choosing between, and the things mature interfaces reliably avoid. Read it when you are distinguishing convention from signature, last section first: it is the highest-signal part, and it is mostly a list of what generated interfaces do that shipped ones do not. [motion.md](motion.md) is the parallel axis for how the interface moves; read it when assigning intensity, complexity, and type, independently of the layout archetype.

## Rules

- **Name the part, never the product.** "Restrained type, two weights" is actionable and defensible. "Like Stripe" is neither.
- **The reasoning transfers, the pixels do not.** If your output is recognisable as the reference, you copied instead of learning.
- **Never reuse identity.** Logos, wordmarks, signature brand colour, distinctive illustration. That line is not aesthetic, it is other people's property.
- **Check the reference against your audience, not your taste.** A beautiful consumer product is the wrong reference for an operations tool, however much you admire it.
- **Extracted tokens are a draft.** Substitute the brand, keep the structure, re-verify contrast.
- **Capture findings, not values.** An entry that records pixel values is a museum of somebody else's CSS. Identity never enters the store at all.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The user linked it, so they want it reproduced" | They want the quality they saw. Reproducing the surface gives them a lesser copy of another product, on their own domain |
| "It works for them, so it works here" | It works for their audience doing their task. Transferring it without checking that is how a dense admin tool ends up with a marketing hero |
| "The extractor output is a design system" | It is a scrape of what shipped, brand identity and dead CSS included. It becomes a system after someone decides what to keep |

## When this does not apply

Skip this where the project has an established design language, since the inspiration question is already answered and inheriting beats importing. Skip it where the user has given a direction in their own terms rather than by reference.

## Before you hand it over

Check the result for the three ways this goes wrong: a finding recorded as a measurement instead of a convention, a brand colour or identity element carried over from the reference, and a pattern adopted from a product whose audience is not yours.
