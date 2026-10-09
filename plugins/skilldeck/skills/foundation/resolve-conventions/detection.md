# Detection

How to read a repository to resolve conventions from the project itself (tier 1). Detection always outranks any default. Record the evidence for each finding so the resolution is auditable.

## Package manager and runtime

- `pnpm-lock.yaml` then pnpm. `yarn.lock` then yarn (check `packageManager` field for berry vs classic). `package-lock.json` then npm. `bun.lockb` or `bun.lock` then bun.
- `packageManager` field in root `package.json` is authoritative when present.
- `.nvmrc`, `.node-version`, or `engines.node` give the Node version. A `bun.lockb` or `deno.json` signals a non-Node runtime.

## Module system

- Root `package.json` `"type": "module"` then ESM, else CommonJS. Confirm against `tsconfig.json` `module`/`moduleResolution` and actual `import`/`require` usage in `src`.

## Lint and format

- `biome.json` or `biome.jsonc` then Biome.
- `.eslintrc*` or `eslint.config.*` then ESLint. `.prettierrc*` or a `prettier` key then Prettier. Both present is the common ESLint + Prettier pairing.
- `.oxlintrc.json` then oxlint.
- Check `scripts` in `package.json` (`lint`, `format`) to see what is actually wired.

## Test runner

- `vitest.config.*` or a `vitest` key then Vitest. `jest.config.*` or a `jest` key then Jest. `bun test` in scripts then bun test. Imports from `node:test` then the built-in runner. `playwright.config.*` then Playwright for e2e.
- The `test` script in `package.json` is the tiebreaker for what the team runs.

## Validation and schema

- Dependencies: `zod`, `valibot`, `arktype`, `yup`, `joi`, `io-ts`. Grep `src` for the import to confirm it is actually used at boundaries, not just installed.

## TypeScript posture

- `tsconfig.json` `compilerOptions.strict` and related flags. `interface` versus `type` usage across `src` shows the house style.
- Path aliases in `paths` reveal import conventions.

## Frameworks and surface

- Web: `next`, `remix`/`react-router`, `vite` + `react`, `@tanstack/router`, `astro`.
- Mobile: `expo` then Expo. `react-native` without Expo then bare RN. `ios/` and `android/` folders confirm a native project.
- Backend: `express`, `fastify`, `@nestjs/*`, `hono`, `koa`, `@trpc/server`, `graphql`.
- The presence of these in `dependencies` plus their entrypoints tells you the surface (backend, frontend, mobile).

## Project shape

- Root `pnpm-workspace.yaml`, or `workspaces` in `package.json`, or `turbo.json` / `nx.json` then monorepo. Call the Skill tool with "project-shape" for the full shape read and structure recommendations.

## Existing conventions and standards

- A `CONTEXT.md` at the repo root carries the project's own vocabulary; read it and let its terms win.
- `.skilldeck-skills/config.yaml` is a prior resolution cache. `.skilldeck-skills/company.yaml` or an in-repo standards skill is tier 2 and outranks personal defaults.
- `.editorconfig`, `CONTRIBUTING.md`, and existing folder naming under `src` all encode conventions; honor them over any default.

## When detection is silent

Nothing found for a given convention means it is greenfield for that choice. Only then do the default tiers apply: company, then personal ([defaults.yaml](defaults.yaml)), then community ([community-defaults.md](community-defaults.md), recommend then ask).
