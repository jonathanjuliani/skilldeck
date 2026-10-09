---
source: https://rive.app
captured: 2026-09-17
surface: motion-runtime product marketing with a live example reel
audience: designers and engineers choosing how to ship interactive graphics
domains:
  - creative-tools
  - developer-tools
principles:
  - product-as-proof
motion: purposeful
motion_complexity: simple
motion_types:
  - loading
verify_after: 2027-03-17
---

## Taken

- Wait and idle states are the product, not a spinner. A vertical reel of live UI (dash, clock, game select, phone) keeps moving while the rest of the page is readable, so the wait explains capability instead of stalling first paint.
- State-machine graphics replace looping decoration. The same asset can sit still, react, or show progress, which is why a loader can stay small and still feel alive.
- The headline and two install paths stay still. Motion is reserved for the proof column, so chrome does not compete with the claim.
- First paint does not depend on the reel. Type, CLI, and editor actions are usable if the examples fail to play.

## Rejected

- The wordmark, condensed display face, and brand examples (vehicle dash, named game UI). Those are identity.
- Copying a specific character or gauge as a loader. Reuse stateful wait, not their illustration.
- Ambient loops on every page. A reel that never explains a state becomes noise on an operator surface.

## Not applicable here

- Store when a wait or idle state should still look like the product. Wrong for a dense table, a checkout, or any surface where motion would hide the task.
