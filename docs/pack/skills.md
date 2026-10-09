# Skills

Every skill in the pack, one line each.
Open this when you want the full breakdown, not the four-folder summary.
Back to [skilldeck](../../README.md).

A plugin install namespaces a command as `/skilldeck:`. `npx skills` stays unscoped.

## What makes it different

Most skill sets bake in a stack. These resolve it. Before any tool or pattern choice, a skill walks one **precedence chain** and stops at the first tier that answers:

1. **Project** what the repo already uses (lockfile, `package.json`, configs, existing layout). Detection always wins.
2. **Company** a standardization config or skill carried by the repo.
3. **Personal** your seeded tiebreakers, only where the two above are silent.
4. **Community** on greenfield, the current default offered with a reason and confirmed before it is applied.

So the same skills work on a legacy npm/Jest service, a pnpm/Vitest monorepo and a fresh Expo app without special-casing.

Every skill also carries the guardrails that earn their place in it: **When this does not apply** (all of them, so a skill is not applied to a one-line change), **Excuses that do not hold** (the sentence an agent tells itself to skip the discipline, and the rebuttal), **Before you hand it over** (what actually goes wrong in that skill's output), and **Persistence** on the two that set a session-long posture. A guardrail shapes how a skill is applied and never reduces what the agent may analyze, search or consider. Authoring rules are in [`.agents/conventions.md`](../../.agents/conventions.md).

## Skills

### Foundation

- **resolve-conventions** (model-invoked): the precedence engine. Detects a project's conventions and resolves anything unresolved against personal then community defaults.
- **setup-skills** (user-invoked): one-time setup. Confirm personal defaults, detect the project, write `.skilldeck-skills/config.yaml`, and **optionally** add two blocks to the repo's `AGENTS.md` or `CLAUDE.md`: a verification rule, and a routing table mapping the moments of a task to the skill that owns each. Each is asked separately and written only between its own markers.
- **agent-instructions** (model-invoked): write or repair a repo's `AGENTS.md` or `CLAUDE.md` so its rules actually bind, on the budget of being read every turn.

### Engineering

- **project-shape** (model-invoked): detect single-repo, monorepo, or modular, and recommend folder and structure best practices per surface (backend, frontend, mobile).
- **bootstrap-repo** (model-invoked): turn an empty or near-empty repo into the smallest runnable project, with community defaults confirmed before they are written.
- **ts-standards** (model-invoked): JS/TS conventions reference (naming, types, error handling, module boundaries, validation at boundaries). Principles, not vendors.
- **create** (model-invoked): scaffold a new component, module, package, service, or screen to the resolved conventions and shape. Walks a YAGNI ladder first, since the cheapest unit of code is the one nobody writes.
- **refactor** (model-invoked): behavior-preserving refactor toward the project's conventions, tests green throughout, and no fence removed before it is understood.
- **api-design** (model-invoked): choose REST, tRPC, or GraphQL by consumer, with typed, validated contracts.
- **data-model** (model-invoked): design entities, invariants, and persistence shape before any table, collection, or ORM file is written.
- **security-hardening** (model-invoked): find where the system extends trust (untrusted input, access control, secrets, supply chain) and put the right control there. Also the trust pass when `create`, `api-design`, `frontend-craft`, or `forms` crosses a boundary.
- **state-management** (model-invoked): separate server state from client state and pick the right tool for each.
- **forms** (model-invoked): forms people can finish. Labels that persist, validation that fires at the right moment, errors that never destroy typed input, and submit that happens once.
- **frontend-craft** (model-invoked): compose React and React Native components well and treat accessibility as part of the build, reaching for the platform before a dependency. Takes its direction from `design-brief`.
- **testing-strategy** (model-invoked): choose seams and test kinds, concentrate effort on critical paths, and run the red-green loop.
- **debug** (model-invoked): reproduce a failure whose cause is unknown, fix that cause, pin it, and backfill a silent path. New code does not get its first signals here.
- **verify-before-done** (model-invoked): set the observable criterion before starting, then prove it with fresh command output before claiming anything is done, fixed, or passing.
- **dependency-choice** (model-invoked): decide whether to add a dependency and which, judged on current community adoption, fit, and exposure.
- **perf-audit** (model-invoked): measure, fix the dominant cost, re-measure; guidance per surface.
- **observability** (model-invoked): instrument for the questions production will ask, and alert on symptoms a user can feel. A new production path gets the moment-0 baseline in the same change.
- **ship-flow** (model-invoked): move a change to production in small steps, with CI as a gate, flags, staged rollout, and an undo path.
- **mitigate-incident** (model-invoked): stabilize a production system that is hurting users before explaining it, then name any signal that was missing.
- **migration** (model-invoked): retire an old dependency, API, or pattern with expand, migrate, contract, and treat deleting the old thing as the actual finish line.
- **record-decision** (model-invoked): write an architecture decision, including the options that were rejected, into the project's existing decision home.
- **release-flow** (model-invoked): versioning, changelog, and publishing, matching the project's existing process.

### Design

These skills are the decide half of System at Designs. The folder stays so that decision stays separate from the build in `frontend-craft`. See [Coverage](coverage.md).

- **design-brief** (model-invoked): establish the surface kind, the audience and what they are doing, the references, the dials, and the constraints that override taste. One sentence that the rest of the work is checked against.
- **information-architecture** (model-invoked): content, hierarchy, navigation, screen and URL structure, naming and flows, decided before anything is styled.
- **design-inspiration** (model-invoked): take a reference apart and reuse the reasoning rather than the pixels, including extracting a token set from a live page and knowing a convention from a signature.
- **curate-design-inspiration** (model-invoked): after user confirmation, discover categories and live examples from curated galleries, dedupe against the store, and write new capture entries to the personal store.
- **design-tokens** (model-invoked): name decisions by role rather than by value, define both themes together, and adopt a token system in a codebase that hardcodes values today.
- **design-review** (model-invoked): scored usability critique ranked by user impact, so a finding is a row a team can prioritise instead of an opinion.

They run in that order on a new surface: a read, then the structure, then the direction and its tokens, then the build in `engineering/`, then the score. On an existing product most of it is already answered and the job is to inherit rather than decide.

`design-inspiration` ships a seed of captured references under `skills/design/design-inspiration/references/`, and accumulates further reads in a personal store at `~/.skilldeck-skills/design/references/` by default. One file per reference, recording what was taken, what was rejected, and the audience it came from. New captures go to the personal store unless asked to ship. When a task needs the store (not only a named live URL or paste), `design-inspiration` confirms a session working set via `store-selection.md` before opening captures: seed, then default personal, then an alternate folder only if the user names the path. Merge and override apply to that task only and do not change files on disk. Both stores sit above the conventions in `patterns.md`. When the accepted set is thin or needs a gallery-driven refresh, `curate-design-inspiration` confirms scope, deduplicates against authorized locations, and writes new personal entries.

Accessibility splits three ways rather than being one pass: a linter catches the static mistakes, `axe` in CI catches the computed ones, and only what neither can see reaches a human review. `frontend-craft` carries that split, and `design-review` refuses to spend attention on anything the first two tiers should have gated.

### Process

These skills sit on the Process axis. `align-first` is model-invoked and runs once per non-trivial task through the routing block. `investigate-product`, `plan-delivery`, `retro`, and `diagram` are the Defines level. See [Coverage](coverage.md).

- **align-first** (model-invoked): restate the ask, name the assumptions you would otherwise make silently, surface only the branches whose answers change the work, then continue under stated defaults rather than blocking. Escalates into a bounded interview when that pass does not land, with the declared branch list as its budget.
- **investigate-product** (user-invoked): investigate the product and user problem before any solution is designed. Output is a short problem brief.
- **plan-delivery** (user-invoked): sequence a set of asks into phases by value versus effort, with a thin first slice and clear cut lines.
- **diagram** (model-invoked): choose the right diagram for what is being explained and render it.
- **retro** (user-invoked): turn a finished delivery into durable, owned changes that feed the next plan.

Some things are deliberately left out:

- a `bug-hunting` and a `quality` review skill, because Claude Code ships `/code-review` and `/simplify`. On another harness you may want an equivalent; this can change later
- an `item estimation` skill lives inside the `plan-delivery` one
