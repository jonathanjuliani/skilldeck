# Money

Read this when an entity holds an amount. Skip it for a count that is not money, and for a rename of a column that already stores minor units.

- **Store, send, and compute an integer in minor units, with the currency.** Cents, for a currency that has two decimals. A `number` you divide, and a float total, drift. A currency with no fractional unit uses the major unit as the integer. A currency with three decimals uses that scale, and the scale is named next to the amount.
- **The currency travels with the amount.** Never add amounts of different currencies. Convert in one named step, or refuse.
- **Round once, at a named step, and name the mode.** Half-even is the usual default, because it does not drift across many operations. A tax or legal rule may require half-up, and that rule wins when it applies. When an amount is split, the parts must sum back to the original (largest remainder). Do not drop or invent a unit.
- **The server is the price authority.** Recompute the total from the server's own prices. A total the client sends is only for detecting a mismatch. Do not charge it.
- **Display formatting is a view concern.** Format when rendering. Do not store a formatted string. On the web, `Intl.NumberFormat` is the platform tool. The project's locale formatter wins when it has one.
- **The column is an integer or an exact numeric, never a float.** A branded minor-unit type, or a small value that carries amount and currency together, is worth it when amounts cross a module boundary. A money library is a dependency decision. Call the Skill tool with "dependency-choice".
