---
name: create
description: Scaffold new JS/TS code (component, hook, module, package, service, endpoint, or screen) to a project's resolved conventions and shape. Use when the user wants to add or generate a new unit of code and it should match how the project is already built. Detects the stack first; recommends and asks on greenfield. Not for an empty or near-empty repo with nothing to match, which is bootstrap-repo, not for designing entities and persistence before any file exists, which is data-model, not for changing code that already exists, which is refactor, and not for adding a line inside a file that already answers every convention question by example.
---

# Create

Scaffold a new unit of code so it lands consistent with the project: the right folder, the right conventions, the right structure, with nothing hardcoded. This is where the precedence engine becomes concrete files.

The defining constraint: this skill writes zero opinions of its own. Every tool and pattern it uses is resolved from the project, then company, then personal, then community. It generates code that looks like the surrounding code, not like a template.

## Before you scaffold

The cheapest unit of code is the one nobody writes. Walk this ladder first and stop at the first rung that answers, because every rung below it then becomes unnecessary:

1. **Does this need to exist yet?** Being asked for it is not the same as needing it, so this rung is not cleared by the fact that the request exists. When the ask is framed around a future need ("we will want", "eventually", "so we can later"), name in one line what carrying it costs from today and what the smaller version would be, then build it if the user still wants it. A unit built for an anticipated need starts accruing maintenance immediately and usually guesses the shape wrong, because the need that eventually arrives is not the one that was imagined.
2. **Does the project already have it?** A helper, hook, type, or module doing this job is often a few folders over. Re-implementing what already exists is the most common way a codebase grows without gaining anything. Call the Skill tool with "resolve-conventions" for what is already in place, and read the neighbors before concluding there is nothing.
3. **Does the language or runtime cover it?** The standard library and the platform APIs handle more than they get credit for.
4. **Does the platform do it natively?** A native input type rather than a component library, a CSS capability rather than a JS one, a database constraint rather than application code. Fewer moving parts, and someone else maintains them.
5. **Does an installed dependency solve it?** A library the project already carries beats a new one. Call the Skill tool with "dependency-choice" before adding anything.
6. **Only then, scaffold the smallest thing that works.** Smallest means the fewest files and the least indirection that solves today's case, not a tidy layering of it. A module exporting a value is a complete answer where a provider, a hook, a context and a config file would be four places to look.

Say which rung you stopped at and why, in one line. When a rung between 1 and 5 answers, that answer is the deliverable. Scaffolding the unit anyway, after finding it was unnecessary, is the failure this ladder exists to prevent.

## Steps

1. **Resolve the stack.** Call the Skill tool with "resolve-conventions" to learn the package manager, language settings, test runner, validation library, and framework the project uses. If `.skilldeck-skills/config.yaml` exists, it is the cache; trust it.
2. **Resolve the placement.** Call the Skill tool with "project-shape" to learn the shape (single-repo, monorepo, modular) and the surface (backend, frontend, mobile), so the new unit lands in the right folder with the right internal structure.
3. **Apply the standards.** Call the Skill tool with "ts-standards" for naming, type shape, boundary validation, and module depth.
4. **Confirm the plan, then generate.** State what will be created and where, in one short list (files, their folder, the conventions applied and their tier). On greenfield choices, show the recommendation and ask. Then write the files.
5. **Match the neighbors.** Before writing, read one or two sibling units in the same folder and mirror their structure, imports, and naming. A consistent-but-imperfect match beats an ideal that stands out.
6. **Wire it in.** Register the new unit where the project expects (route table, index export, navigator, DI/composition root), following the existing pattern. Do not invent a new registration mechanism.
7. **Guard the path you just created.** Skip an internal helper, a local script, and a prototype. When the unit will run for a user in production, call the Skill tool with "security-hardening" if it accepts input, stores a credential, or writes a log, and call the Skill tool with "observability" for the moment-0 baseline. Do not paste their lists in here.

## What "consistent" means here

- **Folder and naming** follow the detected layout and casing, not the personal default, whenever the project has one.
- **Validation at the boundary**: a new endpoint, form, or external call gets a schema in the project's validation library.
- **Tests where the project puts them**: if siblings have colocated tests in the project's runner, the new unit gets one too. For a test-first build, call the Skill tool with "testing-strategy".
- **Public surface**: export through the module's `index.ts` if that is the pattern; keep internals private.

## Rules

- **Never introduce a new tool to satisfy a personal default.** If the project uses Jest, write a Jest test, not a Vitest one. The personal default applies only to a genuinely greenfield project, and even then it is offered, not imposed.
- **Confirm before creating on greenfield.** When there is no convention to detect, show the recommended choice and its rationale and get a yes before generating.
- **No scaffolding sprawl.** Generate the unit the user asked for and its direct wiring, not a speculative layer of folders "for later".
- **Say what you assumed.** Where the request left something open, state the assumption instead of silently picking. If two readings produce different units, present both and ask.
- **Report what you did and why.** After generating, list the files and the tier each convention came from, so the choices stay auditable.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The project uses Jest, but Vitest is better" | Better is not the criterion. A second test runner in one repo is worse than either runner alone |
| "I will scaffold the surrounding folders now to save time later" | Later can scaffold for itself, and usually wants a different shape than you guessed |
| "There is no sibling to match, so the personal default applies" | Look one level wider before concluding there is no precedent. A repo with genuinely no precedent is greenfield, which means you ask |

## When this does not apply

Adding a line to an existing file is not scaffolding a unit. Skip the full resolution when the change lands inside a file that already exists and already answers every convention question by example. An empty or near-empty repository is not a unit either; that job is `bootstrap-repo`. Reach for this skill when something new arrives with its own folder, wiring, or public surface inside a project that already runs.

## Before you hand it over

Three things go wrong in this skill's output. Check each against the files you just wrote: the new unit reads like its siblings rather than like a template, it is actually wired in where the project expects, and no folder was created that nothing yet uses.

Then call the Skill tool with "verify-before-done" before reporting the work as complete.
