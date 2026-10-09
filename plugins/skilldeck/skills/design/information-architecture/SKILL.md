---
name: information-architecture
description: Define the structural layer of a product before visual design begins, covering content inventory, hierarchy, navigation model, screen and URL structure, naming, and the flows users take through it. Use when planning a new product area, when navigation has grown confusing, when users cannot find something, or before any visual work on a multi-screen surface. Not for the visual direction and audience read, which is design-brief, and not for how source files are laid out on disk, which is project-shape.
---

# Information architecture

Decide what content exists, how it is grouped, what it is called, and how someone moves through it, before anything is styled. This is the layer under the visual one, and it is the layer that determines whether a product feels findable.

The defining constraint: a visual pass cannot repair a wrong structure. When something is in the wrong place or called the wrong thing, better typography makes it a better-looking version of the same problem. Structure is cheap to change on a whiteboard, expensive once screens exist, and effectively permanent once URLs are public and bookmarked.

## Inventory before organising

List what actually exists, or will: the objects, the actions on them, the states they have. Read the code and the domain rather than inventing categories from the outside. Call the Skill tool with "resolve-conventions" for the project's own vocabulary, since a `CONTEXT.md` at the root is the authoritative naming source and its terms win.

Then, once, ask the question that resolves most structural arguments: **what does the user come here to do?** Group by that, not by how the system happens to be built. Grouping by internal architecture is how products end up with a menu that mirrors a database schema.

## Decide the shape

- **Hierarchy.** How many levels deep, and how wide at each. Prefer flat: three levels is usually enough, and each extra level is a place something hides. Where a level exists only to hold one child, remove it.
- **Navigation model.** Persistent global navigation for a handful of top-level areas; a sidebar where there are many peers and users move between them constantly; progressive disclosure for a long flow with one path. Pick one primary model and stay with it. Two competing navigation systems on one product is the most common cause of "I can't find it".
- **Screen structure.** For each screen: its one job, what must be visible on arrival, what is secondary, and what belongs on a different screen. A screen with two jobs will be redesigned later.
- **URL and route structure.** Readable, stable, hierarchical, and matching the mental model rather than the file layout. URLs are a public contract: once shared, changing one breaks a bookmark, and retiring one is a migration. Call the Skill tool with "migration" when an existing route has to change.
- **Naming.** From the domain and from the user's language, consistent everywhere. One concept, one word. Where the codebase and the interface disagree on a name, that is a real defect and it will keep producing bugs and support tickets.

## Trace the flows

For each significant task, write the steps as a sequence: entry point, each decision, each state, the end. Then look for what the sequence exposes and a screen inventory hides:

- A step that exists only because of how the system is built.
- A dead end with no forward action.
- A state nobody designed: empty, loading, error, partial, too many, not permitted.
- A loop the user can get stuck in.
- An entry point nobody arrives through, and a screen nothing links to.

Call the Skill tool with "diagram" to render a flow or a hierarchy where the structure is easier to see than to describe.

## Rules

- **Group by user intent, not by system structure.** The menu should not mirror the schema.
- **Prefer flat and wide over deep and narrow.** Depth is where content goes to be lost.
- **One job per screen.** Two jobs means a future split.
- **Names come from the domain.** Where a `CONTEXT.md` exists, its vocabulary is the answer and this skill does not invent an alternative.
- **URLs are a contract.** Design them once, deliberately, and treat changing one as a breaking change.
- **Structure precedes style.** Hand the finished structure to `design-brief` and `frontend-craft`; do not settle visual questions here.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "We will work out the structure as we build the screens" | Then the structure is whatever the first three screens implied, and the fourth will not fit. It is a whiteboard decision now and a migration later |
| "Just add it to the menu for now" | Every "for now" item is permanent, and the menu is the one place where the cost of that is visible to every user |
| "The user can search for it" | Search is a fallback for a findable product, not a substitute for one. Anything that can only be found by searching is effectively hidden |

## When this does not apply

A single screen, a component, and a change inside an existing structure do not need this. Reach for it when a surface has several screens that relate to each other, when navigation is already confusing, or when someone cannot find something that exists.

Where the product already has a working structure, inherit it. Proposing a reorganisation is its own piece of work with its own migration, not a step inside a feature.

## Before you hand it over

Check the structure for the three things that surface immediately once it is built: a level that holds exactly one child, a screen nothing links to, and a state nobody designed, which is almost always the empty one or the error one.
