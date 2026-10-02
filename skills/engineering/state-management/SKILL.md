---
name: state-management
description: Decide how state should be managed in a React or React Native app, separating server state from client state and choosing the right tool for each. Use when the user is adding state, sees prop-drilling or sync bugs, or asks which state library to use. Defers library choices to resolve-conventions. Not for how a component is composed or made accessible, which is frontend-craft, not for how entities are persisted, which is data-model, and not for a single value owned by one component that nothing else reads.
---

# State management

Decide where a piece of state lives and what manages it. Most state confusion is one mistake repeated: treating server data as if it were client state. Separate the two first, and the tool choices become obvious.

The defining constraint: the first question is never "which library", it is "is this server state or client state". Server state is a cache of something that lives elsewhere; client state is owned by the UI. They want opposite tools, and mixing them is the root of most sync bugs.

## Classify the state

- **Server state.** Data that originates on a server and can change without this client: lists, records, user data, anything fetched. It is a cache, with staleness, refetching, and invalidation as first-class concerns. Manage it with a server-state library (resolved via resolve-conventions; TanStack Query is the community default for web and RN). Never copy it into local component state and try to keep it in sync by hand.
- **Client state.** State the UI owns and the server never sees: which tab is open, a draft input, a toggled panel, a wizard step. Manage it with the lightest thing that works.

## Choose the client-state tool by scope

1. **Local first.** `useState` or `useReducer` in the component that owns it. Most state is local; keep it there.
2. **Lift only as far as needed.** Shared by a few nearby components? Lift to the nearest common parent, or use context for a genuinely tree-wide, low-frequency value (theme, current user, locale).
3. **A shared store for cross-cutting, frequently-updated state.** When many distant components read and write the same fast-changing state, reach for a small store (resolved via resolve-conventions; Zustand is the community default, Redux Toolkit when a large app needs its structure and devtools). This is the last resort, not the first reach.

## Form state

Forms are their own category: use the project's form library with schema validation (React Hook Form + Zod by default), not raw `useState` per field. The form owns its state; validation is a schema, shared with the API contract where possible.

## Rules

- **Server state is a cache, not local state.** If you are writing effects to sync fetched data into `useState`, stop and use a server-state library.
- **Reach for a global store last.** Local, then lifted, then context, then a store. Each step only when the previous genuinely does not fit.
- **Context is for low-frequency, wide values.** Putting fast-changing state in context re-renders the whole tree; that is a store's job.
- **One library per role.** One server-state library, one client store; do not run two of either. The specific libraries come from resolve-conventions, deferring to whatever the project already uses.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The global store is quicker than lifting it" | Quicker once, and a cost on every later read, because now any component can write it and none of them document that they do |
| "It is fetched data, but the store is right there" | Fetched data in a client store is a cache you maintain by hand, which is the bug class this skill exists to prevent |

## When this does not apply

A single boolean owned by one component needs no classification. Skip this where the state is plainly local and nothing shares it, and skip the tool choice entirely where the project has one settled pattern for the role. Follow that pattern instead.

## Before you hand it over

State bugs are the ones least visible in a rendered screen, because the wrong value looks exactly like the right one until the second interaction. Pin the transitions the classification turned on: what the component does when the server state is still loading, and what it does when two sources disagree. Call the Skill tool with "testing-strategy" for the seam those belong at.

Then call the Skill tool with "verify-before-done", because a re-render that looks correct is not evidence that the state it came from is.
