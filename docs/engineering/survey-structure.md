## What it does

Reads an existing JavaScript or TypeScript repository and returns a refactor backlog for its layout and module shape. It does not change files.

It plays the survey role that `refactor` refuses to mix into an edit. Each finding is one future refactor, with a path, what is wrong, why the next change is harder, and one motivation sentence.

## When to reach for it

You invoke this by typing `/survey-structure`, and the agent will not reach for it on its own. Reach for it when you want to see how an existing repo sits against its own shape and module rules before anyone starts moving code. For an empty tree, use `bootstrap-repo`. For one refactor you have already named, use `refactor`.

## The method it runs

It reads the project's conventions, classifies the shape, and applies the module rules. A layout that is already consistent wins, even when it is imperfect. A monorepo shows up only when a second consumer of shared code already exists. Everything that is not worth a refactor goes in a not-now group, with the reason.

The reply is the artifact. It does not write a file into the repository, and it does not start the first refactor.

## Common questions

**The list is long. What orders it?**
Run `/plan-delivery` on the findings. This skill lists them. It does not sequence a contested set.

**Can it fix the worst one while it is in there?**
No. A finding fixed in the same turn is a refactor that never got its own review. Pick one item afterward and ask for that refactor alone.

**Is this a quality review?**
No. It does not hunt bugs, score the product, or restyle an interface. A wide component counts only as a wide module.

## Invoking it

This page writes `/survey-structure` for brevity, but the prefix depends on how you installed. The plugin namespaces its skills, so it is `/skilldeck:survey-structure` in Claude Code and Cursor and `@skilldeck:survey-structure` in Codex. Installed as files with `npx skills`, the command stays unscoped: `/survey-structure`.

## It's working if

- The reply names the detected shape and the evidence for it.
- Each finding has one path and one motivation.
- The not-now group says why those items are not findings.
- The worktree is unchanged.
