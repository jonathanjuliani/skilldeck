# CONTEXT

Shared vocabulary for skilldeck skills, which ship in the `jonathanjuliani/skilldeck` marketplace. Skills read this so their words mean the same thing across the set. When a project has its own `CONTEXT.md`, that project's terms win for that project.

## Core terms

- **Convention**: a concrete tool or pattern choice for a project (package manager, formatter, test runner, folder layout, naming style). Conventions are resolved, never assumed. See the `resolve-conventions` skill.
- **Precedence chain**: the fixed order for resolving a convention: **project** (detected) then **company** (config or standardization skill) then **personal** (seeded defaults) then **community** (recommend, then ask). Higher wins. A skill never applies a lower tier over a resolved higher one.
- **Detected**: read from the repository itself (lockfile, `package.json`, config files, existing layout). Detection always outranks any default.
- **Personal defaults**: the seeded tiebreakers in `resolve-conventions/defaults.yaml`. They apply only when nothing higher resolves the choice.
- **Community default**: the choice most projects reach for today, recorded in `resolve-conventions/community-defaults.md`. Offered with a one-line rationale, then confirmed with the user; never applied silently on greenfield.
- **Surface**: the kind of code a skill is acting on: **backend**, **frontend**, or **mobile**. Structure and defaults differ per surface.
- **Project shape**: **single-repo**, **monorepo**, or **modular** (a single deployable split into internal modules). See the `project-shape` skill.
- **Greenfield**: no existing convention to detect for the choice at hand. The only case where a default is proposed.

## Config

- `.skilldeck-skills/config.yaml` (per repo): resolved conventions and project shape for this repo, written by `setup-skills`.
- `.skilldeck-skills/company.yaml` (per repo, optional): company standardization choices that outrank personal defaults.
- `skills/design/design-inspiration/references/` (shipped with the plugin): starter design-reference captures, one file per source. Community seed for `design-inspiration`. Outranked by the personal store and by the project.
- `~/.skilldeck-skills/design/references/` (per machine, optional): captured design references, one file per source, written by `design-inspiration`. Personal, because an installed plugin is otherwise read-only and the value is in accumulating across projects. It is the design counterpart to tier 3 of the precedence chain and outranks the shipped seed.
- **Agent instructions blocks** (per repo, optional): two short blocks `setup-skills` offers to write into the repo's `AGENTS.md` or `CLAUDE.md`, each between its own markers and each on its own yes. The **verification block** (`skilldeck-skills:verification`) puts a completion gate in context without needing an invocation. The **routing block** (`skilldeck-skills:routing`) does the same for which skill belongs to which moment in a task. Both exist because a file read every turn reaches the model and a skill description only reaches it when something goes looking.

## Conventions for authoring these skills

See `.agents/conventions.md`.
