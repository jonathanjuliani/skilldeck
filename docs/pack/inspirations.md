# Inspirations

Prior art this pack learned from, and the optional companions a few skills name.
Open this when you want something narrower, more opinionated, or more complete.
Back to [skilldeck skills](../../README.md).

## Optional companions

This pack is self-contained: nothing here requires another plugin to work. A few skills are better with company, and where that is true they name the companion rather than assuming it is installed.

| Want | Where it lives |
| --- | --- |
| A standalone session that grills a plan you already have | `grill-me` and `grill-with-docs` in [mattpocock/skills](https://github.com/mattpocock/skills). `align-first` here runs one cheap pass every time and escalates into a bounded interview when that pass does not land, which covers the same ground from the other end |
| A deeper test-driven discipline | `obra/superpowers` and `mattpocock/skills` both ship one. `testing-strategy` here carries the loop well enough to work alone |
| Extracting a token set from a live site | [arvindrk/extract-design-system](https://github.com/arvindrk/extract-design-system), which `design-inspiration` points at rather than reimplementing |
| Building and stress-testing a domain model | `domain-modeling` in [mattpocock/skills](https://github.com/mattpocock/skills). `agent-instructions` here covers what a `CONTEXT.md` should contain |

Claude Code's own `/code-review`, `/simplify`, `/run` and `dataviz` are referenced in a few places and ship with that harness. On Codex, Cursor or Gemini you will want an equivalent, and the skills that mention them say so rather than depending on them.

## Prior art

What this pack learned from. Each is worth reaching for directly when you want something narrower, more opinionated or more complete: this one is deliberately small and vendor-neutral, and that is a trade rather than a claim to be better.

| Repo | What it is | Why you would reach for it |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | A full methodology as composable skills: brainstorm, plan, worktree, subagent execution, TDD, review | You want the process to own the whole loop. Its `verification-before-completion` is the ancestor of `verify-before-done` |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 25 engineering skills mapped to a lifecycle, with personas and reference checklists | You want breadth. `security-hardening`, `observability` and `ship-flow` all go deeper there |
| [mattpocock/skills](https://github.com/mattpocock/skills) | A senior TypeScript workflow built around grilling the user until the ask is understood | You want a full interview. `align-first` here is the light version, not a replacement |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's own: document formats, artifacts, MCP builder, skill-creator | You need a document or an artifact. This pack does not go near those |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Forces the laziest solution that works, with intensity levels and a published benchmark | You want the anti-over-engineering stance always on. The YAGNI ladder in `create` is a narrow version of its ladder |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Karpathy's notes on LLM coding pitfalls as behavioral rules | You want one short file rather than a skill set. Its ideas are spread across `create`, `refactor` and `verify-before-done` |
| [educlopez/ui-craft](https://github.com/educlopez/ui-craft) | A design engineering system: one skill over 34 references covering heuristics, inspiration, motion, forms, recipes | You want depth on a specific surface. Its scored critique is the ancestor of `design-review`, its pattern analysis of `design-inspiration` |
| [julianoczkowski/designer-skills](https://github.com/julianoczkowski/designer-skills) | A nine-skill design pipeline: brief, IA, tokens, build, review, tasks | You want the design process driven end to end. The phase split in `design/` follows its shape |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design intelligence as searchable data: styles, palettes, font pairings, UX guidelines | You are doing real visual design. `frontend-craft` sets a direction; this has the reference library |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Anti-slop frontend for landing pages and portfolios, driven by a design read and three dials | You are building marketing surfaces. The read and dials in `design-brief` come from here |
| [arvindrk/extract-design-system](https://github.com/arvindrk/extract-design-system) | Extracts colours, type, spacing, radii and shadows from any public site into `tokens.json` and `tokens.css` | You want a real starting token set. `design-inspiration` points here rather than reimplementing it |
| [feature-sliced/skills](https://github.com/feature-sliced/skills) | Official Feature-Sliced Design v2.1: layers, slices, public API boundaries, import rules | You want one prescriptive frontend architecture. Note it carries no licence |
| [humanlayer/skills](https://github.com/humanlayer/skills) | A small set including `improve-claude-md` and agentic control-loop builders | You want an agentic loop. `agent-instructions` owes its conditional-rule idea to `improve-claude-md` |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Cuts token use hard by stripping the agent's prose | Long sessions where output volume is the cost |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Shapes output for action: next step first, state restated, no preamble | You want answers you can act on. Pick one of this and caveman, not both |
| [blader/humanizer](https://github.com/blader/humanizer) | Removes the structural tells of AI writing | You are shipping prose: docs, posts, release notes |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | A curated list of skills and tools | You are looking for something specific and want to search before building it |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | An agent harness performance system: skills, instincts, memory, security | You want to change the harness itself, not just add skills |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | An agent framework built to grow with its user | You are building a custom agent rather than extending one |

Links verified 2026-09. Star counts are omitted, since they are stale the day they are written.
