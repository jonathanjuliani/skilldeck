---
name: api-design
description: Design an API boundary (REST, tRPC, or GraphQL) with typed, validated contracts. Use when the user is adding an endpoint, designing a service interface, or deciding how a client and server should talk. Chooses the API style from the project and consumers, validates every payload, and defers tool choices to resolve-conventions. Not for an internal function signature nothing outside the module depends on, not for how entities are stored, which is data-model, and not for retiring a contract version, which is migration.
---

# API design

Design the contract between a client and a server so it is typed end to end, validated at the edge, and matched to who actually consumes it. The style question comes first; the endpoint shapes follow.

The defining constraint: the API style is chosen from the consumer, not from preference. A TypeScript client talking to a TypeScript server wants different plumbing than a public API serving unknown clients, and picking wrong makes every later decision harder.

## Choose the style

Call the Skill tool with "resolve-conventions" first: if the project already has an API style, match it. On greenfield, choose by consumer:

- **tRPC** when both ends are TypeScript in one repo or monorepo. Types flow without codegen; the client calls procedures like functions. Best DX, but couples client and server to the same types.
- **REST + OpenAPI** when consumers are public, polyglot, or external. A documented, versioned HTTP contract any client can use. Reach for it when you do not control every caller.
- **GraphQL** when many clients need to shape their own queries over a rich, interconnected graph and over-fetching is a real cost. Powerful, but it carries schema, resolver, and caching complexity; do not adopt it for a handful of endpoints.

State the choice and the reason. When it is a close call, present the two credible options and let the user pick.

## Design the contract

- **Validate every inbound payload.** Body, params, query, and headers pass through a schema (the project's validation library, Zod by default) before any logic runs. The parsed, typed value is what the handler works with.
- **Type the outputs too.** Responses are schemas, not ad hoc objects, so the contract is enforced in both directions and the client's types are trustworthy.
- **Model errors as part of the contract.** Define the error shape once (a discriminated result or a documented error body with codes), map domain errors to it in one place, and keep transport concerns (status codes) out of the domain.
- **Design for evolution.** Additive changes over breaking ones. For public REST, version explicitly. Make fields that might grow into objects objects from the start.
- **Assume every observable behavior is depended on.** With enough consumers, what your contract promises stops being the boundary: the ordering you never guaranteed, the exact error string, the incidental latency, the field that happens to be present all become things someone relies on. Two consequences. Make the surface as narrow as you can afford, since anything visible is effectively promised. And treat "nobody should be relying on that" as a hypothesis to check against real usage, not a defence.
- **One live version of a contract, wherever you can manage it.** Every additional supported version multiplies the states you test, the paths you debug, and the places a fix has to land. Prefer rolling consumers forward over keeping versions alive in parallel, and where a second version is genuinely necessary, it comes with a removal date and an owner. Call the Skill tool with "migration" for how to retire the old one.
- **Pagination, filtering, idempotency** are decided at design time for any collection or mutation that needs them, not bolted on later. Cursor pagination for large or live sets; idempotency keys for unsafe retried operations.

## Rules

- **Consumer picks the style.** Do not default to your favorite transport; default to what the caller needs.
- **No unvalidated input reaches logic.** The boundary is where trust begins.
- **The transport stays thin.** Handlers parse, call a service, and shape the response. Business logic lives behind the boundary, where the `create` and `project-shape` skills place it.
- **Contracts are shared, not duplicated.** In a monorepo, schemas and client types live in a shared package so both sides use one source of truth.

## Trust and signals on the new operation

Every new or changed contract accepts untrusted input. Call the Skill tool with "security-hardening" for the trust and authz pass. Shaping the contract stays here; that skill decides what the boundary is allowed to trust.

Call the Skill tool with "observability" and apply the moment-0 baseline to the new operation in the same change. Skip a signal the project already emits for that operation.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The only caller is our own frontend, so it can be trusted" | The caller is the network, not the frontend. Anything that can reach the endpoint will eventually send something the frontend never would |
| "TypeScript types already describe the payload" | Types are erased before the request arrives. A type is a claim about what should arrive and a schema is what checks whether it did |
| "We can add pagination when the collection gets big" | By then it has callers who expect an array, so adding it is the breaking change you were trying to avoid |

## When this does not apply

An internal function is not a contract in this sense. Reach for this skill at a boundary something outside the module depends on, not for every function signature. An additive change inside an established contract follows that contract rather than redesigning it.

## Before you hand it over

Check the contract for the three omissions that surface later as breaking changes: an inbound payload that reaches logic unvalidated, an error path with no defined shape, and a collection endpoint with no pagination decision.

A contract is a promise to someone you will not be in the room with, so the promise needs a test holding it: the rejected payload, the error shape, and the success case at minimum. Call the Skill tool with "testing-strategy" for which seam those sit at.

Then call the Skill tool with "verify-before-done", because a contract that compiles has not yet been shown to reject anything.
