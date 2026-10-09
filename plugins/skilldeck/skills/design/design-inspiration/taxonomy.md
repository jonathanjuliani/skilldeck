# Taxonomy

Closed vocabularies for tagging a capture so the store can be filtered without opening every file. Read this when writing or assigning `domains` and `principles` on a capture, and when filtering the seed against a brief. Surface and audience stay free prose; these tags are the lookup keys.

Snapshot date: 2026-09. The lists are closed: do not invent values. Omit a tag when that axis is not distinctive.

## Domains

Vertical or product family. One to three per capture. Primary filter for "does this project match this reference?"

| Tag | Fits |
| --- | --- |
| `finance` | Lending, banking, markets UIs, commercial finance ops |
| `payments` | Checkout, payment rails, billing, money movement |
| `crypto-defi` | DeFi protocols, crypto markets, on-chain dashboards |
| `developer-tools` | IDEs adjacent tools, runtimes, APIs, docs for builders, code review |
| `infrastructure` | Cloud, deploy, data platforms, GPU, durable execution |
| `productivity` | Calendar, launchers, workspace, async video, personal ops |
| `ops-admin` | Internal tools, SRE, admin consoles, dense operator work |
| `security` | Privacy, identity protection, cloud security |
| `health` | Healthcare, labs, clinic, consumer health memberships |
| `hr` | People ops, reviews, hiring workflows |
| `education` | Learning products, language, courses |
| `marketplace` | Two-sided markets, listings, launches |
| `editorial` | Blogs, magazines, archives, long-form indexes |
| `portfolio` | Personal designer or engineer sites for hiring scans |
| `studio-agency` | Studio and agency marketing selling craft |
| `hardware-commerce` | Device and product commerce, hardware pages |
| `public-sector` | Government and regulated public services |
| `ai-ml` | Model labs, agents, generative tools, Physical AI |
| `creative-tools` | Design, canvas, motion, photo, site builders |
| `social` | Feeds, communities, saving and sharing |
| `legal` | Contracts, e-sign, deal rooms, counsel workflows |

Audience mismatch still wins over a domain match. A beautiful finance marketing page is the wrong reference for an operator table in the same vertical if the audience job differs.

## Principles

Craft axes that transfer. Zero to four per capture. Omit when none are distinctive. Never encode brand identity here.

| Tag | Fits |
| --- | --- |
| `restraint` | Few sizes and weights, quiet chrome, trust through understatement |
| `density` | High information per screen, tight spacing, tables and lists that earn every pixel |
| `trust-first` | Specific claims, plain language, low theatre for sceptical buyers |
| `keyboard-first` | Shortcuts, focus order, and scanning that favour hands on keys |
| `search-first` | Query or filter as the product entry, not a marketing hero |
| `typographic` | Type carries hierarchy and presence more than imagery |
| `product-as-proof` | Real UI or data as the main visual evidence |
| `task-focused` | One job on screen; everything else removed or demoted |
| `editorial-voice` | Long-form structure, POV copy, archive or magazine rhythm |
| `operator-speed` | Built for people who live in the screen; speed over delight |

## How to assign

1. Pick domain(s) from what the *source product* is, not from the project you are designing for. Filtering happens at read time against the brief.
2. Add principles only when the Taken section would still make sense without naming the product.
3. Prefer fewer tags. Two precise domains beat five overlapping ones.
4. Seed captures always have at least one domain. Principles stay optional.

## How to filter

From the brief, name domain(s), archetype, motion need, and optional principles. Use the seed indexes in [references/README.md](references/README.md) and personal-store frontmatter only, then open at most two or three matching files. The full procedure is in [capture.md](capture.md).
