---
name: bootstrap-repo
description: Turn an empty or near-empty JS/TS repository into the smallest runnable project. Use when the tree has no package manifest, the user just initialized a repository, or they ask to start a new app, service, or library. Community defaults are offered with a reason and confirmed before they are written. Not for adding a unit to a repo that already has a shape, which is create, not for classifying or reorganizing an existing tree, which is project-shape, and not for choosing tools inside a repo that already has them, which is resolve-conventions.
---

# Bootstrap repo

Turn an empty tree into a project that installs, tests, and runs. Stop at that. The first real feature is a later unit, written the way the rest of the pack writes units.

The defining constraint: an empty repo has no neighbors to copy, so every tool choice is a community or personal default and has to be confirmed before it is written. Guessing the stack and scaffolding a product on top of it is how a greenfield repo starts life already wrong.

## See that it is actually empty

Look for a package manifest, a lockfile, a workspace file, and source that already runs. Any of those means this is not an empty repo. Classifying that tree is `project-shape`. Adding a unit inside it is `create`.

Near-empty means a repository with a readme or a license and nothing that installs or tests. Treat that as empty. A single existing manifest is not empty, even when the rest of the tree is thin.

## Resolve, then write the skeleton

Call the Skill tool with "resolve-conventions". On an empty tree the project tier is silent, so the community tier applies: recommend each default with a reason and wait for confirmation. Do not install or write files on an unconfirmed stack.

Call the Skill tool with "project-shape" for the surface the user is starting (backend, frontend, mobile, or a library) and the layout that surface wants. Then write the smallest runnable skeleton, and nothing else.

After you know whether this is an app or a library, read one companion. Do not open both.

- An app, service, or client: [app.md](app.md)
- A library other packages import: [library.md](library.md)

A pure library, a local script, and a prototype get no production instrumentation and no trust-boundary pass. When the skeleton includes a server, or a client that talks to one, and that process will run for a user in production, call the Skill tool with "security-hardening" if it already accepts input, stores a credential, or writes a log, and call the Skill tool with "observability" so the moment-0 baseline is on that path before the skeleton is called done. A skeleton with no operation yet names the hook (correlation id, failure log, span at the boundary, rate, errors, and duration) and leaves the per-operation signals to the first real unit.

## Hand off, do not keep building

The first feature, screen, or endpoint is not part of the skeleton. Call the Skill tool with "create" for that unit once the skeleton runs.

Tell the user they can run `/setup-skills` to write `.jon-skills/config.yaml` and, if they want it, the routing block. That skill is user-invoked, so do not call it yourself. If they want `AGENTS.md` or `CLAUDE.md` as part of this bootstrap, call the Skill tool with "agent-instructions".

## Rules

- **Confirm the stack before any file.** A community default applied silently is an opinion the repo will now have to live with.
- **Smallest runnable.** Manifest, one entry, one test, one way to run. No sample feature, no extra packages, no folders nothing imports.
- **Match a surface, not a template product.** The layout comes from `project-shape` for the surface they named.
- **Stop when it runs.** Further units go through `create`, which will not send the work back here.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "I will scaffold the feature too, since the repo is empty" | The feature is a product decision. The skeleton only proves the toolchain runs |
| "Everyone uses this stack, so I do not need to ask" | An empty repo is the one place a default can still be refused. Ask |
| "I will add the monorepo tooling now so it is ready" | One deployable does not need a workspace. Shape grows when a second one exists |

## When this does not apply

A repository that already installs, tests, or builds is not bootstrapped again. A throwaway script you will not keep does not need a project skeleton.

The shape survives where the rule yields. When you skip the skeleton, say what was already there so the next unit matches it.

## Before you hand it over

Check the tree for the three things this skill gets wrong: a tool choice that was written before anyone confirmed it, a sample feature pretending to be the skeleton, and a project that does not actually install and test.

Then call the Skill tool with "verify-before-done" on the install and the test. A manifest that looks right is not a project that runs.
