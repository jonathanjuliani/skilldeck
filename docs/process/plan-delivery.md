## What it does

Takes a pile of asks or features and sequences them into a phased plan ordered by value against effort, with a thin first slice, milestones, and explicit cut lines for what to drop under pressure. It plays the delivery-manager role.

It plans sequence, not solution. It assumes each item's shape is roughly known and decides what to build first, next, and never, rather than how to build any one thing.

## When to reach for it

You invoke this by typing `/plan-delivery`, and the agent will not reach for it on its own. Reach for it when you have several things to build and need an order that ships value early. For understanding a single fuzzy ask first, use `/investigate-product`; for turning the resulting plan into tickets, use your your ticket-writing step skill.

## The method it runs

Score each candidate on value and effort (high/medium/low, with a one-line why), rank by value against effort, then find the thin first slice: the smallest end-to-end piece that delivers real value and de-risks the biggest unknown. The rest gets grouped into phases, each ending at an independently valuable milestone, each with a cut line. A "not now" list names what you are deliberately not doing, so omissions are decisions.

## Common questions

**My effort estimates are rough.**
That is expected. Estimates are relative and revisable; the first slices teach you the real costs and you re-rank. Precision is not the goal, ordering is.

**Why insist on cut lines?**
A plan without them collapses the first time a deadline slips. Deciding in advance what is non-negotiable and what goes first keeps the slip from becoming a scramble.

**What feeds it?**
Problem briefs from `/investigate-product`, and your own sense of value and effort. Its output feeds ticket-writing.

## Invoking it

This page writes `/plan-delivery` for brevity, but the prefix depends on how you installed. The plugin namespaces its skills, so it is `/skilldeck:plan-delivery` in Claude Code and Cursor and `@skilldeck:plan-delivery` in Codex. Installed as files with `npx skills`, the command stays unscoped: `/plan-delivery`.

## It's working if

- There is a single, shippable thin first slice called out on its own.
- Every phase ends at a milestone a user or metric would notice.
- Each phase has a stated cut line.
- The "not now" list exists and says why, rather than quietly dropping things.
