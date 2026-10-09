# Community defaults

The choice most JS/TS projects reach for today, per convention. This is tier 4: used only when the project and company are silent, offered as a recommendation with a reason, then confirmed with the user. Never applied silently.

Snapshot date: 2026-09, verified against current adoption data. This is a point-in-time read. When a choice matters and the web is available, verify current consensus before recommending and note if it has moved. Update this file with the date when you do.

## What moved since the 2026-08 snapshot

- **Vitest is no longer a close call.** It passed Jest on weekly downloads (roughly 40M against 36M, with Jest flat) and Angular 21 made it the default. **The exception matters here: Jest remains the only officially supported test runner for React Native**, so a React Native project takes Jest and that is a resolution, not a compromise.
- **Expo is now the official React Native default.** The core team no longer recommends starting from `react-native init`. Continuous Native Generation retired the old rule that native modules force the bare workflow, since config plugins cover almost everything. Bare is now for a native module that cannot be wrapped, or for working on React Native itself.
- **Drizzle passed Prisma on weekly downloads for the first time.** Prisma 7 dropped the Rust engine and cut its bundle from around 14MB to 1.6MB, so the old "Prisma is heavy" argument is weaker than it was. Neither is a default now.
- **Zod v4 settled the validation question** for most projects: roughly 14x faster than v3, 57% smaller, and still the largest ecosystem by a wide margin.
- **Oxlint gained a JavaScript plugin alpha**, which makes oxlint alongside ESLint a real hybrid rather than a trade-off, on codebases where the ESLint plugin surface cannot be given up.

## Tooling

| Convention | Community default (2026-09) | One-line rationale | Strong alternatives |
| --- | --- | --- | --- |
| Package manager | pnpm | Fast, disk-efficient, best-in-class workspaces, and the safe monorepo choice | bun (fastest, but adoption as a package manager is still a fraction of pnpm's), npm (ships with Node), yarn |
| Runtime | Node (LTS) | Ubiquitous, broadest compatibility | bun (speed), deno (security and std) |
| Module system | ESM | The ecosystem default for new packages | CJS only for legacy or specific tooling |
| Lint + format | Biome greenfield, ESLint + Prettier where plugin depth is needed | Biome is one fast tool with near-zero config; ESLint still has the unmatched plugin ecosystem | oxlint (fastest, and its JS plugin alpha now allows a hybrid alongside ESLint) |
| Test runner | Vitest, except React Native | Fast, TS and ESM native, Jest-compatible API, and now ahead on adoption | Jest (required for React Native, still mature everywhere else), bun test, node:test |
| E2E | Playwright | Cross-browser, reliable, good tooling | Cypress |
| Validation | Zod v4 | TS-first, much faster and smaller than v3, largest ecosystem | Valibot (far smaller bundle, for edge and browser), ArkType (fastest, type-native syntax) |
| Env parsing | Zod plus a typed loader | Validate env at the boundary like any other input | t3-env style wrappers |

## Web (React)

| Convention | Community default | Rationale | Alternatives |
| --- | --- | --- | --- |
| Framework | Next.js (App Router) | Still the ecosystem lead by a wide margin, RSC streaming, heavily production-hardened | TanStack Start (now production-ready, best type safety and client caching), React Router 7 (absorbed Remix, the path for existing Remix and CRA apps), Astro (content-led) |
| Data fetching / server state | TanStack Query | The server-state standard | RTK Query, framework loaders, tRPC |
| Client state | Zustand for shared, hooks and context for local | Small, unopinionated | Redux Toolkit for large apps, Jotai |
| Styling | Tailwind CSS v4 | Dominant by a wide margin, and the v4 engine made builds near-instant | CSS Modules, vanilla-extract and Panda (build-time, type-safe). Runtime CSS-in-JS is fading; do not start there |
| Components | shadcn/ui (Radix) | Copy-in, so the project owns its code | Headless UI, MUI, Mantine |
| Forms | React Hook Form with a Zod resolver | Performant and validated | TanStack Form |

## Mobile (React Native)

| Convention | Community default | Rationale | Alternatives |
| --- | --- | --- | --- |
| Toolchain | Expo | The officially recommended default. Config plugins and Continuous Native Generation mean native code no longer forces bare | Bare only for a native module that cannot be wrapped, or work on React Native itself |
| Navigation | Expo Router (file-based) | Aligns with Expo, typed routes, deep linking | React Navigation directly |
| Test runner | Jest | The only officially supported runner here, whatever the wider ecosystem does | None worth the friction |
| Server state | TanStack Query | Same as web | SWR |
| Styling | NativeWind | Shares the web mental model | StyleSheet, Tamagui, Unistyles |

## Backend (Node/TS)

| Convention | Community default | Rationale | Alternatives |
| --- | --- | --- | --- |
| HTTP framework | No single winner; Hono or Fastify for new services | Hono is fast and edge-portable, Fastify is mature and plugin-rich | Express (ubiquitous, legacy), NestJS (structure and DI at scale) |
| API style | tRPC for TS-to-TS, REST plus OpenAPI for public or polyglot | Match the consumer | GraphQL where clients need flexible queries |
| ORM / DB | Genuinely split: Drizzle or Prisma | Drizzle is SQL-close, tiny, and the better fit for edge and serverless; Prisma is higher-level with a data browser, and no longer the heavy option it was | Kysely (query builder), raw SQL |
| Validation at edges | Zod v4 | Validate every inbound payload | Valibot where bundle size is the constraint |

Recommendations are starting points, not verdicts. Present the default and one credible alternative, say why, and let the user decide.
