# Monorepo layout

A monorepo is worth it when several deployables share code that must version and build together. Until then it is overhead. When it is warranted, keep the split predictable.

## When to adopt one

Adopt a monorepo when at least one is true:

- Two or more deployables (web + mobile, several services) share domain logic, types, or validation.
- Shared code is currently being copy-pasted or published to a private registry just to reuse it internally.
- Builds and tests need caching and task orchestration across packages.

Do not adopt one for a single app "in case it grows". Convert when the second consumer actually appears.

## Layout

```text
apps/                    # deployables (thin: compose packages)
  web/
  mobile/
  api/
packages/                # shared, versioned internally
  core/                  # domain types, pure logic
  validation/            # shared Zod schemas
  api-client/            # typed client shared by apps
  ui/                    # shared components (only if genuinely shared)
  config/                # shared tsconfig, biome/eslint, tsup presets
tooling/                 # scripts, generators
```

## Principles

- **Apps are thin, packages hold the substance.** An app wires packages together and owns its platform concerns; reusable logic lives in packages.
- **Boundaries are explicit.** Each package has a clear public entry (`exports` / `index.ts`). No deep imports into another package's internals. Dependencies flow from apps to packages, and among packages without cycles.
- **Share the core, not the UI, across platforms.** Web and mobile share types, validation, and clients; UI components stay per platform unless a design system truly spans both.
- **Shared config as packages.** A `config` package centralizes tsconfig, lint/format, and build presets so every package stays consistent. The concrete tools come from resolve-conventions.
- **One workspace manager, one task runner.** The package manager and task orchestrator (turbo, nx, or plain workspace scripts) are resolved via resolve-conventions; do not mix two.

## Splitting a package

Split a new package out only when code is shared by two consumers, or when a bounded piece has a stable interface and its own lifecycle. A package per feature inside a single app is usually premature: prefer modular folders within the app first (the modular single-deployable shape).
