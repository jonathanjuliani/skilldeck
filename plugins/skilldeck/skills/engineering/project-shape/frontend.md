# Frontend structure (React web)

Organize a React app by feature, with a shared UI and lib layer underneath. Colocate everything a feature needs; reach for shared code only when two features truly share it.

## Feature-first layout

```text
src/
  features/
    <feature>/            # e.g. checkout, dashboard, auth
      components/         # components used only by this feature
      hooks/              # feature-specific hooks
      api/                # data fetching for this feature (query/mutation hooks)
      <feature>.schema.ts # Zod schemas for forms and API payloads
      <feature>.types.ts
      index.ts            # the feature's public surface
  components/             # shared, generic UI (design-system-level)
  hooks/                  # shared hooks
  lib/                    # framework-agnostic helpers, clients
  app/ or routes/         # routing per the framework's convention
  styles/
```

When the framework dictates routing (Next.js `app/`, Expo Router, TanStack Router), keep routes thin: a route file composes a feature, it does not hold feature logic.

## Principles

- **Colocation first.** A component used by one feature lives in that feature, not in a global `components/`. Promote to shared only on the second real consumer.
- **Server state vs client state.** Data from the server is server state: manage it with a query library (resolved via resolve-conventions), not by copying it into local state. Reserve client state for genuine UI state (open/closed, selected tab, draft input).
- **Data fetching lives in `api/`.** Components consume typed query and mutation hooks; they do not call fetch inline. This keeps caching, retries, and error handling in one place per feature.
- **Validate at boundaries.** Form input and API responses pass through Zod. A validated boundary means components work with trusted, typed data.
- **Keep components presentational where possible.** Push data access and logic into hooks so components stay easy to read and test.
- **Public surface via `index.ts`.** A feature exports what other features may use through its index; everything else is private to the feature. Avoid deep imports across features.

## Anti-patterns

- Global `components/`, `hooks/`, `utils/` trees that grow forever and force cross-cutting edits for one feature change.
- Duplicating server data into `useState`, then fighting to keep it in sync.
- Prop-drilling many levels: reach for context or a small shared store (resolved via resolve-conventions), not a prop chain.

## Named alternatives

Where a team wants a prescriptive scheme rather than the guidance above, Feature-Sliced Design is the best-known one for frontend: fixed layers from shared up to app, slices inside a layer that may not import from each other, and a declared public API per slice. It buys enforceable boundaries and a shared vocabulary at the cost of ceremony on a small app.

Adopt it wholesale or not at all. Half of FSD is worse than neither, because the layer names then promise a discipline the imports do not keep. Where the project already follows it, follow it.
