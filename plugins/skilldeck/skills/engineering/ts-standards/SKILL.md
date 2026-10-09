---
name: ts-standards
description: JS/TS conventions reference for writing and reviewing code, covering naming, types vs interfaces, error handling, module boundaries, validation at edges, and async patterns. Use when writing new TypeScript, reviewing code for quality, or deciding how to structure types and modules. Defers concrete tool choices to resolve-conventions and to any project or company standard. Not for which tool a project uses, which is resolve-conventions, and not for restructuring existing code as a task in its own right, which is refactor.
---

# TypeScript standards

The house rules for JS/TS that hold across projects: what to name things, how to shape types, where to validate, and how to keep modules honest. Principles, with the reasons, so they transfer.

The defining constraint: these are defaults that yield to the project. When a repo, a company standard, or its `CONTEXT.md` says otherwise, that wins. Consistency within a codebase beats any rule here. Call the Skill tool with "resolve-conventions" for the project's actual posture before applying a default.

## Persistence

This is a posture, not a one-off check. It applies for as long as you keep writing or reviewing JS and TS in this session, not only to the first file, and it does not lapse when the work moves to a different module.

It yields the moment the project speaks, which is the constraint above rather than an exception to it, and it stops entirely when the user asks for something written a different way.

## Simplicity

- **No abstraction for a single use.** An interface with one implementation, a factory producing one thing, a config option for a value that never varies: each is a cost paid now against a benefit that may never arrive. Add the layer when the second case shows up.
- **No handling for states the types rule out.** Defensive code for impossible conditions is code to read and maintain, and it misleads the next reader into believing the case occurs.
- **Solve the problem in front of you.** Speculative generality is the most expensive habit in a codebase because it is invisible: nobody ever deletes an abstraction that might one day be needed.
- **If it could be half the size, make it half the size.** Then check it still reads clearly. Brevity bought with comprehension is not a saving.

## Types

- **Prefer `type` aliases; reach for `interface` when you need declaration merging or `extends` ergonomics.** Pick one style per codebase and hold it.
- **Model the domain in the type system.** Use unions and discriminated unions to make illegal states unrepresentable. A `status: "loading" | "error" | "ready"` with per-variant fields beats a bag of optional booleans.
- **`unknown` over `any`.** `any` disables checking silently; `unknown` forces a narrowing at the boundary. Ban `any` except at genuinely untyped edges, and narrow immediately there.
- **Infer, do not annotate, what the compiler already knows.** Annotate function inputs and public return types for stability; let locals infer.
- **Keep types close to their use.** Domain types live with their feature or module, not in a global `types.ts` dumping ground.

## Naming

- Names come from the domain, not the mechanism. `pendingInvites`, not `dataArray2`. When a `CONTEXT.md` exists, use its vocabulary so names match the shared language.
- Functions are verbs (`sendInvite`), values are nouns (`invite`), booleans read as assertions (`isExpired`, `hasSeat`).
- File and symbol casing follows the project; the personal default is kebab-case files, PascalCase components and types, camelCase values, UPPER_SNAKE_CASE constants.

## Boundaries and validation

- **Validate every input at the edge.** Request bodies, query params, env vars, external API responses, and form input pass through a schema (Zod by default, resolved per project) before any logic sees them. Inside the boundary, data is trusted and typed.
- **Parse, do not just check.** Turn unstructured input into a typed value once, at the edge, and pass the typed value inward. Do not re-validate the same data in five places.
- **Modules are deep.** A module exposes a small public surface and hides the work behind it. A wide, shallow module (many exports, little logic each) leaks its internals and is hard to change. Export through an `index.ts`; keep the rest private.

## Errors

- **Fail loudly at boundaries, handle deliberately inside.** Do not swallow errors with an empty catch. Either handle an error meaningfully or let it propagate to a place that can.
- **Type your domain errors.** Distinct error types (or a discriminated result) let callers respond precisely instead of string-matching messages.
- **Prefer results for expected failures, throws for exceptional ones.** A "user not found" is an expected outcome worth modeling; a corrupted invariant is a throw.

## Async

- **`async`/`await` over raw promise chains** for readability. Handle rejection explicitly.
- **Run independent work concurrently** with `Promise.all`, and use `Promise.allSettled` when partial failure is acceptable. Do not serialize awaits that have no dependency.
- **No floating promises.** Every promise is awaited, returned, or explicitly marked fire-and-forget with handling.

## Comments and dead code

- Comments explain *why*, not *what*. The code says what. Delete commented-out code; version control remembers it.
- No em-dashes in code comments or docs (project convention here).

These are the starting posture. The moment the project speaks, follow the project.

## When this does not apply

These defaults do not govern generated code, vendored code, or a file the project deliberately keeps in a different style. In those places, matching what is there beats correcting it. Nor do they apply to a throwaway script, where the cost of the conventions outlives the code.
