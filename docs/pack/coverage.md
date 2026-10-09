# Coverage

Where the pack sits on an engineering job, and what it leaves out.
Open this when you want the map, not a skill to run.
Back to [skilldeck](../../README.md).

A plugin install namespaces a command as `/skilldeck:`. `npx skills` stays unscoped.

## Coverage

Folders are how the pack is authored. `foundation/`, `engineering/`, `design/`, and `process/` stay. The map below is how those skills cover an engineering job. It follows the five axes in [Engineering Ladders](https://github.com/jorgef/engineeringladders): Technology, System, People, Process, and Influence. A level on an axis is cumulative. This pack does not ship one skill per Developer, Tech Lead, or manager level. A ladder is which axes a role leans on. Developer leans Technology and System. Tech Lead leans System at Owns, Evolves, and Leads. A technical program manager leans Process. Engineering management is out of scope.

`align-first` stays model-invoked. It is the Challenges move on Process, and it runs on tasks that never touch code. The routing block's first row is the delivery channel: once per non-trivial task, then proceed under the stated assumption. It is not a session-long output style. A persistent mode would apply it to a typo, which the skill tells you to skip.

| Axis | Covered | Not in this pack |
| --- | --- | --- |
| Technology | Adopts to Masters: `resolve-conventions`, `ts-standards`, `create`, `project-shape`, `frontend-craft`, `forms`, `state-management`, `api-design`, `data-model`, `design-tokens`, `dependency-choice`, `perf-audit`, `security-hardening`, `debug` | Creates: a new technology used by other teams |
| System | Enhances to Leads: `debug` (Enhances), `create`, `refactor`, `forms`, `frontend-craft`, `api-design`, `data-model`, `bootstrap-repo` (Designs), `project-shape`, `design-brief`, `information-architecture`, `design-inspiration`, `curate-design-inspiration`, `design-review`, `observability`, `ship-flow`, `verify-before-done`, `migration`, `record-decision` (Evolves), `release-flow`, `mitigate-incident` (Owns and Leads) | |
| Process | Follows to Defines: `testing-strategy`, `verify-before-done`, `ship-flow`, `align-first`, `agent-instructions`, `investigate-product`, `plan-delivery`, `retro`, `diagram` | A deeper team-process design than `plan-delivery` and `retro` |
| People | | Mentoring, career conversations, and engineering management. A review skill is omitted because Claude Code ships `/code-review`. |
| Influence | `release-flow`, an artifact other teams can consume | Community reach, which is personal content rather than this pack |

`project-shape` still classifies a repo that exists. `create` still scaffolds a unit inside one. `bootstrap-repo` is the empty tree, `record-decision` is the architecture decision, and `mitigate-incident` is the live incident. People skills are still out of scope, and so is one skill per ladder level. Engineering management is not this pack.

`security-hardening` and `observability` are preventive gates on the skills that write a boundary or a production path (`create`, `api-design`, `frontend-craft`, `forms`, and `bootstrap-repo` when the skeleton will serve users). They are also what you reach for when you ask, and what `debug`, `mitigate-incident`, and `ship-flow` reach for after the fact. `debug` backfills a path that already shipped silent. A new production path gets its correlation id, failure log, span, and aggregate signal in the change that creates it. The threat catalog and the per-surface pages stay inside those two skills and open only after the boundary or the surface is known.

The routing block stays a short moment table, read every turn once a repo opts in. The rows name recurring moments only. A new or changed surface reaches `design-brief` before components. Something broken with an unknown cause reaches `debug`. A new persistence boundary reaches `data-model`. A new trust boundary reaches `security-hardening`, and a new production operation reaches `observability`, each with the skip written in the same row. `bootstrap-repo`, `record-decision`, and `mitigate-incident` stay off that table: they are reach-for via their descriptions, not every-task rows. `investigate-product`, `plan-delivery`, and `retro` stay off it too: they are user-invoked, so a line there would ask for a slash command on every coding task.
