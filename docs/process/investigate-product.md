## What it does

Investigates a product or user problem before any solution is designed, and produces a short problem brief a team could build against. It plays the product manager role: sharpen the problem, size it, and state what success looks like.

It is forbidden from proposing a solution. The entire job is the problem; the moment it starts describing what to build, it has failed.

## When to reach for it

You invoke this by typing `/investigate-product`, and the agent will not reach for it on its own. Reach for it when a feature request or ask arrives and you are tempted to jump to building. It is the guard against building the wrong thing well. For sequencing work you already understand, use `/plan-delivery` instead; for pressure-testing a brief you have written, use your `/align-first`, or a dedicated interview skill if you have one.

## The brief it produces

A one-page document with fixed headings: Problem, User and job, Current behavior, Evidence and size, Constraints, Success criteria, Open questions. There is deliberately no solution section. The leading idea is that a feature request is a proposed solution to someone's problem, and the brief's job is to recover the problem underneath it.

## Common questions

**How is this different from writing a spec or PRD?**
This comes before. It defines the problem; a spec or PRD defines the solution once the problem is agreed.

**What if I already know the solution?**
Write the problem anyway. If the problem is real and well-stated, a known solution loses nothing. If it is not, you just saved the build.

**It keeps refusing to tell me what to build.**
By design. Take the finished brief to design and to `/plan-delivery`.

## Invoking it

This page writes `/investigate-product` for brevity, but the prefix depends on how you installed. The plugin namespaces its skills, so it is `/skilldeck:investigate-product` in Claude Code and Cursor and `@skilldeck:investigate-product` in Codex. Installed as files with `npx skills`, it is plain `/investigate-product`.

## It's working if

- The brief states an observable success criterion, not a vague goal.
- Current behavior is described concretely from the actual product and code, including today's workaround.
- Evidence separates one loud request from a measured pattern, honestly.
- There is no solution anywhere in it.
