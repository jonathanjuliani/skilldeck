# Capturing a reference

How a reference becomes a durable entry instead of a one-off reading. Without this step, every extraction is thrown away and the twentieth reference teaches as little as the first.

## Where it goes

There are two default stores, same format, different jobs. Optional alternate paths exist only when the user opts in during selection.

- **Personal (default):** `~/.skilldeck-skills/design/references/`, one markdown file per reference. Per machine, writable after install, accumulates across projects. This is where new captures go unless this session confirmed another personal path.
- **Shipped seed:** [references/](references/) in this skill. Travels with the plugin. Starter reads that cover the archetypes in [patterns.md](patterns.md) so the store is not empty on a fresh install.

Shipping a new file into the plugin is an explicit ask. An installed plugin is otherwise a read-only bundle, which is why day-to-day capture is personal.

For design the durable tiers still read: the project's own tokens and screens, then a company brand, then personal and seed stores, then the community conventions in [patterns.md](patterns.md). A captured note never outranks what the project already does. Which personal or seed entries feed *this task* is not a silent outrank: confirm the working set via [store-selection.md](store-selection.md) when a store lookup is needed.

## The entry

```text
---
source: https://example.com/pricing
captured: 2026-09-14
surface: marketing pricing page
audience: procurement committee comparing vendors
domains:
  - infrastructure
principles:
  - restraint
  - trust-first
motion: purposeful
motion_complexity: simple
motion_types:
  - transition
verify_after: 2027-03-14
---

## Taken

- Type is two weights and four sizes across the whole page. Restraint reads as confidence to a buying committee.
- Every claim carries a number. "Cut deploys from 7m to 40s", never "blazing fast".
- One primary action per section, repeated, never two competing.

## Rejected

- The dark mesh gradient hero. It is their brand, and it suits a developer audience rather than a procurement one.
- Scroll-triggered entrance on every section. Motion at this density fights the scanning the audience is doing.

## Not applicable here

- Their pricing table has four tiers. Ours has two, so the comparison layout does not transfer.
```

Three sections, and the middle one carries half the value. **Rejected** is what stops you re-evaluating the same reference in six months and reaching a different conclusion for no reason.

## Rules for what gets written

- **Findings, never measurements.** "Two weights, four sizes" transfers to any project. "34px Inter Semibold" transfers to none. A file full of pixel values is a museum of somebody else's CSS.
- **Identity never enters the store.** Logos, wordmarks, a signature brand hue, a distinctive illustration style, a named signature layout. This is the convention-versus-signature line from the parent skill, applied as a filter at write time rather than as advice at read time. A stored signature will eventually be applied by someone who has forgotten where it came from.
- **Always record the read it came from.** A finding without its surface and audience is unusable later, because you cannot tell whether it applies. This is why `surface` and `audience` are required fields.
- **Tag domains from the closed list.** Required on seed captures; required on new personal captures when writing from curation or a full read. Use one to three values from [taxonomy.md](taxonomy.md). Domains describe the source product's vertical, not the project you are designing for.
- **Tag principles when distinctive.** Optional. Zero to four values from [taxonomy.md](taxonomy.md). Omit rather than stretch. Principles are craft axes, never brand identity.
- **Tag motion when the read is clear.** Optional frontmatter `motion: minimal | purposeful | cinematic` for intensity, `motion_complexity: simple | medium | high` for implementation difficulty, and `motion_types` as a YAML list of `loading`, `transition`, `text`, `image`, `scroll` (see [motion.md](motion.md)). Omit any of these when that axis is not distinctive; do not invent tags to fill the fields. Intensity and complexity are independent: a short fade can be cinematic if it is the first impression, and a WebGL wait can be high complexity while staying purposeful.
- **Date it and set a reverification trigger.** Convention drifts. An undated store becomes confidently wrong, which is worse than a dated snapshot that admits what it is. Six months is a reasonable default; shorter for anything fast-moving.
- **One reference per file, named for the source.** Merging references loses the provenance that makes the store trustworthy.

## Reading the store back

Progressive disclosure is a hard gate, not a hint. Do not open every capture body, and do not treat the full provenance table as the finding.

1. **Need-test.** If this task does not need a store lookup, skip the store entirely (named live URL, screenshot, paste, or direction without store). Do not open [store-selection.md](store-selection.md).
2. **Confirm the working set.** When a store lookup is needed, follow [store-selection.md](store-selection.md) before opening any capture: brief first, one tier at a time (seed index, then personal frontmatter, then optional external), short candidate lists, stop until the user confirms. Modes are task-only; they do not change disk.
3. **From the brief**, name domain(s), archetype, motion need, and optional principles. Call the Skill tool with "design-brief" if the read is missing. Domain tags come from [taxonomy.md](taxonomy.md).
4. **After lock, open at most two or three** capture files from the confirmed working set whose tags and audience fit. An entry from a different audience is evidence about that audience, not this one. Audience mismatch still wins over a domain match.
5. **Never** load every seed body, treat a directory listing as the finding, substitute the provenance table for reading the two or three files you selected, or scan alternate paths the user did not opt into.

When the user asks for more motion on a surface and a store lookup is needed, filter the type-by-complexity matrix inside the same selection gate, then open locked files only. The personal store stays unindexed until scanning frontmatter costs more than reading it; tagged frontmatter is enough below that size.

Say when a recommendation came from the store and from which entry, the same way `resolve-conventions` names the tier a decision came from. A recommendation whose source is invisible cannot be argued with.

## When there is not enough in it yet

The shipped seed exists so a fresh install is not starting from zero. Below roughly fifteen *personal* entries, scanning that directory's frontmatter is faster than any index, and the personal store is mostly a notebook. That is the correct shape for it at that size. Build search when scanning starts costing more than reading, not before, and note that an index over five entries is a worse version of a prose file.

When the accepted working set is thin for the surface, audience, and domain in front of you, or the user wants the base populated or refreshed from galleries, Call the Skill tool with "curate-design-inspiration" only after they agreed in selection (or asked explicitly). That skill confirms scope first, deduplicates against locations authorized this session, and writes new capture files to the confirmed personal destination (default `~/.skilldeck-skills/design/references/`).
