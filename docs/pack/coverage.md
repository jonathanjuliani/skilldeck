# Coverage

Where the pack sits on an engineering job, and what it leaves out.
Open this when you want the map, not a skill to run.
Back to [jon-skills](../../README.md).

## Coverage

Folders are how the pack is authored. `foundation/`, `engineering/`, `design/`, and `process/` stay. The map below is how those skills cover an engineering job. It follows the five axes in [Engineering Ladders](https://github.com/jorgef/engineeringladders): Technology, System, People, Process, and Influence. A level on an axis is cumulative. This pack does not ship one skill per Developer, Tech Lead, or manager level. A ladder is which axes a role leans on. Developer leans Technology and System. Tech Lead leans System at Owns, Evolves, and Leads. A technical program manager leans Process. Engineering management is out of scope.

`align-first` stays model-invoked. It is the Challenges move on Process, and it runs on tasks that never touch code. The routing block's first row is the delivery channel: once per non-trivial task, then proceed under the stated assumption. It is not a session-long output style. A persistent mode would apply it to a typo, which the skill tells you to skip.

| Axis | Covered | Not in this pack |
| --- | --- | --- |
| Technology | Adopts to Masters: `resolve-conventions`, `ts-standards`, `create`, `project-shape`, `frontend-craft`, `forms`, `state-management`, `api-design`, `design-tokens`, `dependency-choice`, `perf-audit`, `security-hardening` | Creates: a new technology used by other teams |
| System | Enhances to Evolves: `create`, `refactor`, `forms`, `frontend-craft`, `api-design`, `project-shape`, `design-brief`, `information-architecture`, `design-inspiration`, `curate-design-inspiration`, `design-review`, `observability`, `ship-flow`, `verify-before-done`, `migration`, `release-flow` | Leads. `project-shape` classifies a repo that exists. `create` scaffolds a unit inside one. An empty-repo bootstrap, a skill that records an architecture decision, and an incident or mitigation skill are not shipped. |
| Process | Follows to Defines: `testing-strategy`, `verify-before-done`, `ship-flow`, `align-first`, `agent-instructions`, `investigate-product`, `plan-delivery`, `retro`, `diagram` | A deeper team-process design than `plan-delivery` and `retro` |
| People | | Mentoring, career conversations, and engineering management. A review skill is omitted because Claude Code ships `/code-review`. |
| Influence | `release-flow`, an artifact other teams can consume | Community reach, which is personal content rather than this pack |

The three System gaps worth a later skill are an empty-repo bootstrap, an architecture-decision record, and incident mitigation. This change does not add them, and it does not add People skills or one skill per ladder level.

The routing block stays a short moment table, read every turn once a repo opts in. The rows name recurring moments only. A new or changed surface reaches `design-brief` before components. `investigate-product`, `plan-delivery`, and `retro` stay off that table: they are user-invoked, so a line there would ask for a slash command on every coding task.
