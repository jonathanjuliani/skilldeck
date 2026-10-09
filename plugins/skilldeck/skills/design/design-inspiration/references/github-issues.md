---
source: https://github.com/vercel/next.js/issues
captured: 2026-09-13
surface: product issue list with filter chrome and row-to-detail
audience: contributors and maintainers triaging open work on a public repo
domains:
  - developer-tools
  - ops-admin
principles:
  - density
  - operator-speed
  - keyboard-first
motion: minimal
verify_after: 2027-03-13
---

## Taken

- List and detail share one product grammar: status, title, labels, assignees, comments, age. Opening an issue continues that grammar instead of inventing a second visual language.
- Filter and search sit above the list as work controls, not marketing modules. The job is triage, so chrome earns its place by narrowing the set.
- Each row carries the metadata that decides the next click (labels, comment count, author, relative time) on the same line as the title.
- Empty and filtered states stay inside the list surface. The product does not replace the feed with a hero when nothing matches.
- Density is high on purpose. Cards would slow scanning for people who live in the queue.

## Rejected

- Importing GitHub's marketing homepage chrome into an issues product. The marketing surface is a different read (see the separate github.com capture).
- Softening rows into equal cards or illustration panels. That fights triage density.
- Ambient motion on filter changes. Instant list updates match how operators scan.

## Not applicable here

- Store when designing a records list that opens into a detail view inside a product. Wrong for marketing heroes, canvas editors, or single-field checkout.
