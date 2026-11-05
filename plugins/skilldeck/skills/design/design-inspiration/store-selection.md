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

Ordered defaults and offers. Scan a location only when this gate reaches that tier, and only after any prior confirm said to continue. Do not touch the library on a task that failed the need-test above.

1. **Shipped seed:** [references/](references/) indexed by [references/README.md](references/README.md). Community starter reads that travel with the plugin.
2. **Public library:** [jonathanjuliani/design-references](https://github.com/jonathanjuliani/design-references). The larger public set, same capture format. Resolve it with the library check below. A missing checkout does not skip this tier.
3. **Scratch pad:** `~/.skilldeck-skills/design/references/`. Per machine. Notes that are not ready to publish. Default write target when the library checkout is missing or the user does not want the file published.
4. **Named alternates (offer text only, never auto-probe):** any other folder the user names.

Do not invent paths beyond the library URL and the two home directories above. A named alternate still waits for a yes plus a concrete path.

## Library check

Run this only when the gate reaches the library tier. There is no background poller.

Checkout path: `~/.skilldeck-skills/design/library`

Public repo: `https://github.com/jonathanjuliani/design-references`

Raw index: `https://raw.githubusercontent.com/jonathanjuliani/design-references/main/README.md`

Raw capture: `https://raw.githubusercontent.com/jonathanjuliani/design-references/main/references/<slug>.md`

1. If the checkout path exists, read `git remote get-url origin`. If that URL is not this repo, say so and use the public link for this read. Do not scan the wrong directory.
2. If it is that repo, compare `git rev-parse HEAD` with `git ls-remote` for the default branch (the `HEAD` line, or `refs/heads/main`).
   - Same commit: scan local frontmatter. Do not also download remote copies.
   - Ahead of the remote: say so, then scan local frontmatter.
   - Behind: say so and offer `git pull`. Pull only after a yes, then scan. If they decline, scan the local copy and say it may be stale.
   - The remote check fails: say so and scan the local checkout.
3. If the checkout path is missing, read the raw README index. Do not clone. Do not download the tree. After they confirm candidates, open at most two or three raw capture files.
4. Never commit or push. Never pull except the pull they just accepted. Never clone unless they asked. A clone is a write-path offer in [capture.md](capture.md), not part of this read.

## Cheap scan rules

1. **Brief first.** Domain (and surface/audience if known). Call the Skill tool with "design-brief" only if missing. Do not scan stores to invent the brief. Domain tags: [taxonomy.md](taxonomy.md).
2. **One tier at a time.** Seed index, then one confirm, then the library (local frontmatter or the public README), then one confirm, then scratch-pad frontmatter, then one confirm, then a named path only if they give one. Do not parallel-read all stores.
3. **Index and frontmatter only until lock.** Seed: prefer README **By domain**, then intersect archetype and/or motion (and principles when that is the reason). Do not walk every capture file or dump the full provenance table. Library without a checkout: the public README index only, until the working set is locked. Local library, scratch pad, and a named path: filenames plus YAML frontmatter only.
4. **Short candidate lists.** Cap at roughly five slugs plus one-line surface each. If more match, show the top matches and say how many more exist; expand only if asked.
5. **Batch confirms.** One message per tier (or one combined merge/override message once the tiers that have candidates are known). Not one turn per file.
6. **Early exit.** If the user chooses proceed on-demand / skip stores, stop scanning remaining tiers. Open no capture bodies.
7. **Bodies last.** After the working set is locked, open at most two or three capture bodies from that set. Never treat an index row as the finding.

## Flow

### 1. Seed tier

Cheap-filter the seed index for the brief. Then **one confirm**:

- **Related matches:** list the short candidate set. Ask whether to use those for this task, update/add more before proceeding (offer `curate-design-inspiration` or a capture write, each still confirms before write), or skip the seed for this task.
- **None related / empty for this brief:** ask whether to save basic seed use anyway (if any weak matches), search and save more (curate), or proceed with on-demand findings only (no store bodies).

If they choose on-demand / skip stores, lock an empty working set and stop the gate.

### 2. Library tier

Only after the seed step continued. Run the library check, then cheap-filter that source the same way. Then **one confirm**:

- **Related matches:** list candidates. Ask whether to use them, update/add more (curate/capture), or skip the library for this task.
- **None related:** ask whether to search/save more, or proceed with the current choices (seed and/or on-demand).

A missing checkout still reads the public index. It does not skip the tier and it does not clone.

### 3. Scratch pad (default `~/.skilldeck-skills/design/references/`)

Only after the library step continued. Cheap-filter scratch-pad frontmatter the same way. Then **one confirm**:

- **Related matches:** list candidates. Ask whether to use them, update/add more (curate/capture), or skip the scratch pad for this task.
- **None related / missing dir:** ask whether to search/save unpublished notes, or proceed with the current choices.

The scratch pad stays the default write target unless this session already confirmed the library checkout as the destination.

### 4. Combine accepted tiers

If two or more tiers contributed candidates the user accepted, ask once:

- **merge:** use every accepted tier for this task
- **one tier:** seed, library, or scratch pad only
- **listed override:** only the named slugs (from any accepted tier) for this task

Remind them this does not change files on disk.

If only one tier has accepted entries, skip this step.

### 5. Named alternate

Offer "another folder or path you name." Do **not** scan until they give a path and say yes. The public library is not this offer. It was already resolved.

- On success: cheap-filter that path; list candidates; ask merge with the current working set, listed override, or external-only for this task.
- On failure (no access, missing, empty): ask whether to retry with another path, proceed with the current working set, or stop.

### 6. Lock and open

State the locked working set (paths and slugs). Open at most two or three capture bodies from it. Say which entries feed each recommendation. A new capture writes to the library checkout only when they want it published and that checkout exists. Otherwise it writes to the scratch pad. If they want it published and the checkout is missing, offer to clone `jonathanjuliani/design-references` to `~/.skilldeck-skills/design/library` and stop until they say yes. The plugin seed only when they explicitly ask to ship a starter. Do not commit or push.

When the accepted set is thin for the surface, audience, and domain, or the user asked to search/save, Call the Skill tool with "curate-design-inspiration" only after they agreed. That skill confirms scope before any crawl or write, and dedupes only against locations authorized this session.

## Working-set modes (task only)

| Mode | Meaning for this task |
| --- | --- |
| `merge` | Union of accepted entries from the tiers already confirmed |
| `seed-only` | Only accepted seed entries |
| `library-only` | Only accepted public-library entries |
| `personal-only` | Only accepted scratch-pad entries |
| `external-only` | Only accepted entries from the opted-in named path |
| `listed-override` | Only the slugs the user named, from any confirmed tier |

None of these create, delete, move, or rewrite store files.

## After lock

Follow the body-open and provenance rules in [capture.md](capture.md). Format for any new write is also there.
