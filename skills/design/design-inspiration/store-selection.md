# Store selection (task working set)

Confirm which inspiration-store entries this task will use. Modes change the **working set for this task only**. They do not add, remove, or rewrite files on disk. Writes still need a separate yes via capture or `curate-design-inspiration`.

Read this file only after the parent skill's need-test says a **store lookup** is required. If the working set was already locked earlier in this task, do not re-run the gate.

## Need-test (do not load past here if false)

Skip this companion when:

- The project already has an established design language (inherit).
- The user gave direction in their own terms with no store ask.
- The user named a specific live URL, screenshot, or paste to read once (on-demand only).
- The skill was reached only for convention versus signature, a token-extract draft, or [patterns.md](patterns.md) / [motion.md](motion.md) without "use the store."

## Known locations

Ordered defaults and offers. Scan a location only when this gate reaches that tier, and only after any prior confirm said to continue.

1. **Shipped seed:** [references/](references/) indexed by [references/README.md](references/README.md). Community starter reads that travel with the plugin.
2. **Default personal:** `~/.skilldeck-skills/design/references/`. Writable per machine. Default destination for new captures unless this session confirmed another path.
3. **Known alternates (offer text only, never auto-probe):** any other folder the user names.

Do not invent paths. List the offer in the external-tier confirm and wait for a yes plus a concrete path.

## Cheap scan rules

1. **Brief first.** Domain (and surface/audience if known). Call the Skill tool with "design-brief" only if missing. Do not scan stores to invent the brief. Domain tags: [taxonomy.md](taxonomy.md).
2. **One tier at a time.** Seed index → one confirm → only then personal frontmatter → one confirm → only then offer alternates/external. Do not parallel-read all stores.
3. **Index and frontmatter only until lock.** Seed: prefer README **By domain**, then intersect archetype and/or motion (and principles when that is the reason). Do not walk every capture file or dump the full provenance table. Personal and external: filenames plus YAML frontmatter only.
4. **Short candidate lists.** Cap at roughly five slugs plus one-line surface each. If more match, show the top matches and say how many more exist; expand only if asked.
5. **Batch confirms.** One message per tier (or one combined merge/override message once both seed and personal candidates are known). Not one turn per file.
6. **Early exit.** If the user chooses proceed on-demand / skip stores, stop scanning remaining tiers. Open no capture bodies.
7. **Bodies last.** After the working set is locked, open at most two or three capture bodies from that set. Never treat an index row as the finding.

## Flow

### 1. Seed tier

Cheap-filter the seed index for the brief. Then **one confirm**:

- **Related matches:** list the short candidate set. Ask whether to use those for this task, update/add more before proceeding (offer `curate-design-inspiration` or a capture write, each still confirms before write), or skip the seed for this task.
- **None related / empty for this brief:** ask whether to save basic seed use anyway (if any weak matches), search and save more (curate), or proceed with on-demand findings only (no store bodies).

If they choose on-demand / skip stores, lock an empty working set and stop the gate.

### 2. Personal tier (default `~/.skilldeck-skills/design/references/`)

Only after the seed step continued. Cheap-filter personal frontmatter the same way. Then **one confirm**:

- **Related matches:** list candidates. Ask whether to use them, update/add more (curate/capture), or skip personal for this task.
- **None related / missing dir:** ask whether to search/save personal refs, or proceed with the current choices (seed and/or on-demand).

Default personal path stays `~/.skilldeck-skills/design/references/` unless the user already named another write target this session.

### 3. Combine seed and personal

If **both** tiers contributed candidates the user accepted, ask once:

- **merge:** use both tiers' accepted entries for this task
- **seed-only** or **personal-only:** drop the other tier from the working set
- **listed override:** only the named slugs (from either tier) for this task

Remind them this does not change files on disk.

If only one tier has accepted entries, skip this step.

### 4. External / known-alternate tier

Offer known alternates and "another folder or path you name." Do **not** scan until they give a path and say yes.

- On success: cheap-filter that path; list candidates; ask merge with the current working set, listed override, or external-only for this task.
- On failure (no access, missing, empty): ask whether to retry with another path, proceed with the current working set, or stop.

### 5. Lock and open

State the locked working set (paths and slugs). Open at most two or three capture bodies from it. Say which entries feed each recommendation. New captures this session write to the confirmed personal destination (default `~/.skilldeck-skills/design/references/`) unless the user asked to ship into the plugin seed.

When the accepted set is thin for the surface, audience, and domain, or the user asked to search/save, Call the Skill tool with "curate-design-inspiration" only after they agreed. That skill confirms scope before any crawl or write, and dedupes only against locations authorized this session.

## Working-set modes (task only)

| Mode | Meaning for this task |
| --- | --- |
| `merge` | Union of accepted entries from the tiers already confirmed |
| `seed-only` | Only accepted seed entries |
| `personal-only` | Only accepted personal entries |
| `external-only` | Only accepted entries from the opted-in external path |
| `listed-override` | Only the slugs the user named, from any confirmed tier |

None of these create, delete, move, or rewrite store files.

## After lock

Follow the body-open and provenance rules in [capture.md](capture.md). Format for any new write is also there.
