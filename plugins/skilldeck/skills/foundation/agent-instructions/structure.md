# File outline

Read this when you are writing or restructuring the file, not when diagnosing why an existing one is ignored.

Lead with what is needed most often. Group by situation rather than by topic, so a rule is found by the work being done. Keep it scannable: an agent reads this under time pressure alongside everything else in context.

Prefer one file. Where a monorepo genuinely needs per-package instructions, a nested file next to that package holds only what is specific to it, and the root file stays the general one.

`AGENTS.md` is the cross-tool convention and the right default. `CLAUDE.md` is the Claude Code specific name. Where both exist, one should point at the other rather than each carrying half the rules, because two files drift.
