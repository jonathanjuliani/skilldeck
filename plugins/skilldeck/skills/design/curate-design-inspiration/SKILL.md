---
name: curate-design-inspiration
description: "Populate or refresh the design-inspiration store from curated gallery sites by discovering categories, picking live project examples, and writing capture.md entries after user confirmation. Use when the inspiration base is thin or not enough for the current surface and audience, when the user asks to populate, update, or curate design inspiration from galleries, or when design-inspiration finds too few relevant store entries. Not for reading a single reference the user already named or linked, which is design-inspiration."
---

# Curate design inspiration

Grow the design-inspiration store from curated galleries of live sites, so later reads have enough relevant entries. The job is discovery and capture into the personal store, not redesigning the product in front of you.

The defining constraint: **confirm with the user before any gallery crawl or store write.** Being model-invoked means you may reach for this when the base is thin or the user wants an update; it does not mean you may populate the store silently. No confirmation, no crawl, no write.

## When to reach for this

- The personal store is thin (roughly under fifteen entries), or fewer than two or three entries match the current surface, audience, and domain.
- The user asks to populate, update, or curate the inspiration base from galleries.
- Call the Skill tool with "design-inspiration" has already checked the store and found not enough for the read.

Always stop and confirm scope before continuing. If the user declines, stop.

## The flow

1. **Enter only after a yes.** Reach here from an explicit curate ask, or from design-inspiration's store selection after the user agreed to search/save. Do not crawl because a tier looked thin without that yes.
2. **Read authorized stores first.** Scan frontmatter only in locations authorized this session: by default `~/.skilldeck-skills/design/references/` and the shipped seed under `design-inspiration/references/` (use its [README index](../design-inspiration/references/README.md) and each file's `source` frontmatter). If selection confirmed another personal or external path, include that path too. Do not probe alternate locations the user did not opt into. Do not open capture bodies for existence checks. Normalize URLs: lowercase host, strip `www.`, trailing slash, and tracking query params.
3. **Confirm scope.** Ask which sources from [sources.md](sources.md) for this session (read it when choosing galleries, not before they have agreed to a crawl), which domain gaps from [taxonomy.md](../design-inspiration/taxonomy.md) matter (for example "finance dense-table"), which gallery categories (or "discover the main ones"), how many examples per category (default two or three), and confirm destination: default `~/.skilldeck-skills/design/references/`, or re-confirm if this session already chose another personal/external write target. Do not start browsing until they agree.
4. **Map categories from the galleries.** Use the tags, collections, and filters the sources themselves expose. Cross with taxonomy domains, the archetypes in [patterns.md](../design-inspiration/patterns.md), and the motion levels in [motion.md](../design-inspiration/motion.md) only to prioritize gaps (domain first; then landing text-led / product-led / editorial; app list-detail / dense table / focused task / canvas; motion minimal / purposeful / cinematic). Prefer *product* URLs for app archetypes (issues list, checkout, canvas editor), not the marketing homepage of the same brand.
5. **Pick candidates.** Few, current, with the *project* URL (the live site), never only the award or gallery page.
6. **Dedupe before any read or write.** If a normalized `source` already exists in an authorized location or the seed, skip it. Also match obvious slug to filename (for example `linear.app` against `linear.md`). Never create a second file for the same project. If `verify_after` has passed and this session is an *update*, offer to refresh the existing file in place; only rewrite after confirmation.
7. **Read the project** with the discipline of design-inspiration: structure, hierarchy, density, type, colour, motion, copy. Call the Skill tool with "design-inspiration" for the read method when needed. Screenshots may help you see the page in-session; never persist images into the store.
8. **Write** one markdown file per new reference to the confirmed destination (default `~/.skilldeck-skills/design/references/`), using the format and rules in [capture.md](../design-inspiration/capture.md): Taken, Rejected, Not applicable; required `domains` from [taxonomy.md](../design-inspiration/taxonomy.md); principles when the read is clear; findings never measurements; identity never enters.
9. **Summarize.** What was added, what was skipped as duplicate, which domain and archetype gaps remain, and offer to ship into the plugin seed only if the user asks.

Prefer a small confirmed batch over a wide automatic sweep. One or two sources and a handful of categories beat all of [sources.md](sources.md) in one go.

## Deduplication contract

Before every write:

- Compare the candidate's normalized `source` against every `source:` in locations authorized this session and the shipped seed.
- Treat host-equivalent URLs as the same project (`https://www.example.com/` and `https://example.com` are one entry).
- Skip duplicates quietly in the summary; do not ask again for each skip unless the user asked to refresh expired entries.
- Refresh means overwrite the same path, never a parallel file.

## Rules

- **Confirm, then crawl.** Reaching for the skill is allowed; writing without a yes is not.
- **Gallery is not the reference.** Capture the linked project. The gallery page is only a finder.
- **Findings, not pixels.** No screenshots in the store. The durable artifact is the capture markdown.
- **Personal store by default.** Destination defaults to `~/.skilldeck-skills/design/references/`; re-confirm if the session chose another path. Shipping into the plugin is an explicit ask.
- **Stop early when covered.** Two or three relevant entries for the surface, audience, and domain are enough; do not pad the store.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The base is thin, so I should fill it without asking" | Thin is the reason to *offer* this skill. The confirm gate is what keeps a bulk crawl from happening mid-task |
| "The gallery page is enough to capture" | The gallery is curatorial metadata. The transferable decisions live on the project |
| "It is almost the same URL, so a second file is fine" | Two files for one project destroy provenance and invite contradictory Taken/Rejected notes |

## When this does not apply

Skip this when the store already has enough entries for the surface, audience, and domain in front of you, when the user has named a specific reference to read (that is design-inspiration alone), and when the project already has an established design language so inspiration import is the wrong move. The confirm gate still applies if you reached here by mistake: ask, and stop if they decline.

## Before you hand it over

Check the batch for three failures specific to this skill: a write that happened without confirmation, a duplicate `source` that slipped past normalization, and a capture that stored identity or measurements instead of findings (or skipped required `domains`). Then list skips and remaining gaps honestly.
