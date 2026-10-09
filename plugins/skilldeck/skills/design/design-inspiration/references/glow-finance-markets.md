---
source: https://app.glowfinance.xyz/markets
captured: 2026-09-11
surface: dense lending-market table
audience: operators comparing rates across assets
domains:
  - crypto-defi
  - finance
principles:
  - density
  - operator-speed
verify_after: 2027-03-11
---

## Taken

- The work is a sortable table: asset, price, deposit, APYs, then row actions. Density is the point; padding is a row they cannot see.
- Filter and search sit on the table, not in a separate "explore" chapter. Operators arrive to compare, not to be onboarded.
- Row actions are named (Deposit, Borrow) and Borrow is disabled where it does not apply. State is in the control, not only in colour.
- Risk footnotes are on the page. A markets UI that omits them is selling, not operating.
- Sans plus a tabular face for numbers. Spacing is a tight 4/8 (table density). Small radius on controls; first and last cells in a row share a corner.

## Rejected

- A cookie modal covering the first rows. Consent that sits on the data is a first-paint failure for this audience.
- Decorative cards above the table restating "access markets". The table is the access.
- Purple as the only signal on Connect Wallet. Hue-only primary actions fail in greyscale.
- Impossible radius values in the scrape. Dead CSS.

## Not applicable here

- Store-only pass. Apply when a product is named. This is the dense-table archetype. It does not transfer to a marketing hero or a focused checkout.
