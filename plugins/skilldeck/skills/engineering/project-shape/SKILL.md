---
name: project-shape
description: Determine whether a project is a single repo, a monorepo, or a modular single-deployable, and recommend folder and structure best practices per surface (backend, frontend, mobile) for JS/TS/React/React Native. Use when adding a package or module to an existing tree, reorganizing folders, or deciding where new code should live. Not for turning an empty tree into the first runnable project, which is bootstrap-repo, not for choosing which tools a project uses, which is resolve-conventions, and not for writing the unit that goes in the folder, which is create.
---

# Project shape

Read a project's shape, then recommend where code should live and how folders should be organized for the surface at hand. Shape and structure are separate questions: shape is how the repo is split; structure is how one unit is organized inside.

The defining constraint: this skill recommends against the shape the project already has, not against an ideal. It detects the shape first and only proposes a change when the current one is actively causing friction, and even then as a suggestion.

## Read the shape

Call the Skill tool with "resolve-conventions" for the raw detection signals, then classify:

- **Single-repo (single package).** One `package.json`, one deployable or library. No workspace config. Simplest; correct for most apps and libraries until a second deployable appears.
- **Monorepo.** Multiple packages under one repo with a workspace manager (`pnpm-workspace.yaml`, `workspaces`, `turbo.json`, `nx.json`). Correct when several deployables or shared libraries need to version and build together. See [monorepo.md](monorepo.md).
- **Modular single-deployable.** One deployable, internally split into feature or domain modules with enforced boundaries (one app, many modules, no separate packages). A middle point: modular structure without monorepo tooling overhead.

State the shape you detected and the evidence. Recommend a different shape only with a concrete reason (a second deployable is appearing, shared code is being copy-pasted, build times demand caching) and present it as a tradeoff, not a mandate.

## Recommend the structure

Identify the surface (backend, frontend, mobile) and, after you know which it is, apply the matching reference. Do not open all four.

- Backend: [backend.md](backend.md)
- Frontend (React web): [frontend.md](frontend.md)
- Mobile (React Native): [mobile.md](mobile.md)
- Monorepo layout across surfaces: [monorepo.md](monorepo.md), once you have classified the shape as a monorepo

The through-line across all surfaces: **organize by feature or domain, not by technical type.** Group what changes together. A `users/` folder holding its component, hook, service, and types beats parallel `components/`, `hooks/`, `services/` trees that force you to touch four folders for one change. Keep modules deep (a small public surface hiding real work) and boundaries explicit.

## Rules

- **Defer to the existing layout.** If the repo already has a consistent structure, match it. Consistency beats your preferred pattern. Propose a reorg only when the current structure is demonstrably hurting.
- **Do not impose a monorepo.** A single app does not need one. Recommend monorepo tooling only when there is a real second consumer of shared code.
- **Shape follows need.** Start as simple as the project allows and grow shape only when a concrete pressure appears.
- **Vendors come from resolve-conventions.** This skill decides layout; the package manager, build tool, and test runner are resolved there.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The current layout is a mess, so the ideal one applies" | A mess applied consistently is still the project's language. Propose a reorg as its own piece of work rather than smuggling one into an unrelated change |
| "This will be a monorepo eventually" | Eventually is not a second consumer. Shape follows a pressure that exists |

## When this does not apply

Skip the shape read when the user asked where a single file goes and the answer is obvious from its neighbors, and when the work happens entirely inside one existing module. A structural read on a one-file change is overhead that teaches nobody anything. An empty or near-empty tree has no shape to classify; that job is `bootstrap-repo`.
