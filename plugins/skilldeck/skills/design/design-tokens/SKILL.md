---
name: design-tokens
description: Establish or adopt a token system so design decisions live in one place instead of being retyped, covering naming by role, both themes from the start, the scales, and how to migrate a codebase that hardcodes values today. Use when starting a design system, adding a theme, replacing scattered literal values, or turning an extracted or chosen direction into something buildable. Not for deciding what the direction should be in the first place, which is design-brief, and not for a single component or a prototype where literals are correct.
---

# Design tokens

Turn a design direction into named values the code uses, so a decision is made once and changed once. This is the link between what `design-brief` decided and what `frontend-craft` builds.

The defining constraint: a token is a decision with a name, not a variable with a value. `--gray-200` is a variable and it tells a reader nothing about when to use it; `--surface-raised` is a decision and it survives the palette changing underneath. Naming by role rather than by value is what separates a token system from a find-and-replace of hex codes, and it is the whole reason a theme change is a swap rather than a rewrite.

## First, find out whether one exists

Call the Skill tool with "resolve-conventions". A project with a component library, a Tailwind theme, a CSS custom property block, or a token file already has a system, and your job is to extend it in its own idiom. Adding a second token system is worse than an imperfect single one, because now every value has two possible homes and nobody knows which is authoritative.

Only where nothing exists, or where the values are scattered literals with no naming at all, does this skill establish something.

## Name by role, in two layers

- **Primitives** are the raw scale: the neutral ramp, the brand hues, the spacing steps, the type sizes. Named by what they are, and **never used directly in a component**.
- **Semantic tokens** are the decisions, named by job: `surface`, `surface-raised`, `border-subtle`, `text-muted`, `danger`, `focus-ring`. These are what components reference.

The indirection is the point. A component asking for `text-muted` keeps working when the neutral ramp is retuned; a component asking for the fourth grey breaks silently and looks slightly wrong in a way nobody can locate. Where a component genuinely needs its own decision, add a component-level token that points at a semantic one rather than reaching past it to a primitive.

## Cover both themes from the start

Define every colour by its role in both light and dark before shipping either. A dark theme derived later by inverting a light palette produces contrast failures, because the relationships that worked in one direction do not hold in the other.

The same applies to anything else that is theme-dependent: shadow, which needs different treatment on a dark surface, and any colour used as a border rather than as a fill. Re-verify every pair against the contrast numbers in `frontend-craft`'s design defaults; a token that passes in light and fails in dark is a token that has not been defined yet.

When you are naming spacing, type, radius, or motion steps, read [scales.md](scales.md) after the semantic layer exists. Skip it while you are still deciding whether a system exists or what to name.

## Where they live

The format follows the stack rather than a preference: CSS custom properties, a Tailwind theme, a native token file for React Native, or a shared package where several surfaces consume the same system. Resolve it, do not choose it. In a monorepo with more than one consumer, tokens belong in a shared package so the contract has one source: call the Skill tool with "project-shape" for the placement.

Where the direction came from an extracted reference, the extraction is a draft. Call the Skill tool with "design-inspiration" for what to keep from it and what to replace, and expect to substitute the brand hues entirely.

## Adopting them in a codebase that has none

This is a migration, not a rewrite, so it follows that shape. Call the Skill tool with "migration".

1. Inventory what is actually used, which is usually a smaller and messier set than anyone expects.
2. Define the semantic tokens the inventory implies, not the ones a complete system would have.
3. Replace literals surface by surface, keeping the old values working until their last caller is gone.
4. Delete the literals, and add a lint rule that stops new ones. Without step four the codebase now has both, which is the failure mode of every abandoned token migration.

## Rules

- **Semantic names, not value names.** A token named for its colour is a hex code with extra steps.
- **Components never touch primitives.** The indirection is the feature; skipping it makes the theme unchangeable.
- **Both themes, defined together.** Deriving one from the other is where contrast failures come from.
- **Extend the existing system.** A second token system is the worst outcome available here.
- **Fewer steps.** A scale nobody can hold in their head is not a scale.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "We only have one theme, so roles are overkill" | The second theme, or the rebrand, arrives later and finds every component asking for a specific grey |
| "This one component needs a slightly different value" | Then it needs a component-level token pointing at a semantic one, not a literal. The literal is the thing you will find in three years and be unable to explain |
| "We will name them properly once the design settles" | The names are the design. Values move constantly and names should not, which is backwards if you name by value |

## When this does not apply

A single component, a prototype, and a project with a design system already in place do not need this. On a throwaway, literals are correct and a token system is ceremony.

Where the project has a system that is genuinely bad, that is its own piece of work with its own migration and its own agreement. Do not begin it inside a feature.

## Before you hand it over

Check the system for the three failures that make it decorative: a token named for its value rather than its job, a component reaching past the semantic layer to a primitive, and a colour pair that was never checked in the second theme.

Then call the Skill tool with "verify-before-done", because replacing literals with tokens touches far more files than it appears to, and a build that still compiles is not evidence that every swapped value landed on the right one.
