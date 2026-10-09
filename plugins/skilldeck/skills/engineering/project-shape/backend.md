# Backend structure (Node/TS)

Organize a backend service by feature or domain, with a thin transport layer over a testable core. The goal: business logic that does not know it is behind HTTP.

## Feature-first layout

```text
src/
  modules/
    <feature>/            # e.g. accounts, billing, notifications
      <feature>.routes.ts     # transport: HTTP/tRPC handlers, thin
      <feature>.service.ts    # use cases / business logic, framework-agnostic
      <feature>.repository.ts # data access behind an interface
      <feature>.schema.ts     # Zod schemas for inbound/outbound payloads
      <feature>.types.ts      # domain types
      <feature>.test.ts       # tests at the service seam
  lib/                    # cross-cutting, dependency-free helpers
  config/                 # env parsing (validated), constants
  server.ts               # composition root: wire modules, start transport
```

## Principles

- **Transport is thin.** Routes parse and validate input (Zod), call a service, and shape the response. No business logic in handlers.
- **Services are the seam.** Use cases live in services and take plain inputs, so they are testable without spinning up the server. This is where tests concentrate.
- **Data access behind an interface.** The service depends on a repository interface, not on the ORM directly. Swapping the datastore or faking it in tests stays local.
- **Validate at the edge.** Every inbound payload (body, query, params, env, external API responses) passes through a schema before it reaches logic. Trust nothing unparsed.
- **Composition root.** One place wires concrete implementations to interfaces and starts the server. Dependencies point inward, toward the domain.
- **Errors are typed and mapped.** Domain errors are their own types; the transport layer maps them to status codes in one place.

## Scaling up

- A layer only earns its place when it is doing work. Do not add a repository for a service that has no persistence, or a service for a route that only reads config.
- When a module grows large, split by sub-feature inside it before reaching for a new top-level structure.
- Shared domain logic used by more than one deployable is the signal to consider a monorepo package, not before.
