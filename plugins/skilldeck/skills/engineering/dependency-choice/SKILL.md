---
name: dependency-choice
description: Decide whether to add a dependency and, if so, which one, judged against current community adoption and project fit. Use when the user is about to install a package, is choosing between libraries, or asks "what should I use for X". Checks current adoption on the web when available and defers to what the project already uses. Not for detecting which tool a project has already settled on, which is resolve-conventions, and not for removing a dependency that is on its way out, which is migration.
---

# Dependency choice

Decide whether a new dependency is worth its cost, and if it is, pick the one the community actually maintains and uses today. This is the plugin's dynamic principle applied to libraries: recommend what is current, not what was current when a skill was written.

The defining constraint: the default answer is "not yet". A dependency is a permanent liability (maintenance, security surface, bundle weight, lock-in), so it must clear a bar before it earns a place, and the smallest option that clears it wins.

## First, do you need it at all

Before comparing libraries, rule out adding one:

- **Is it already solved in the project?** A dependency doing this job may already be installed. Resolve via resolve-conventions and reuse it rather than adding a second.
- **Is it in the platform or framework?** The standard library, the Web/Node APIs, or the framework often already cover it (dates, fetch, crypto, validation primitives). Prefer the platform.
- **Is it small enough to own?** A few lines of well-understood code beats a dependency for a trivial need. Owning it is cheaper than tracking someone else's.

If none of these settle it, then compare.

## Compare candidates on evidence

When the web is available, check current signals rather than relying on memory, which goes stale fast in this ecosystem:

- **Adoption and momentum:** downloads and their trend, GitHub stars trajectory, whether the tools you already use recommend it now.
- **Maintenance:** recent releases, open-issue responsiveness, a real maintainer or team, not a single stale author.
- **Fit:** first-class TypeScript types, ESM support, tree-shakeability, and bundle size (decisive for frontend and especially mobile).
- **Cost:** transitive dependency weight, license, and how hard it would be to remove later.
- **Exposure:** a dependency runs with your privileges, so the axis is not only quality but blast radius. Check for known advisories, count what it drags in transitively, and treat an install script as code you have agreed to run. A package with few dependencies from a maintained source is a smaller bet than a popular one with a hundred. Call the Skill tool with "security-hardening" when the package touches authentication, cryptography, serialization, or anything handling untrusted input.

Cross-check the current community default in the resolve-conventions community-defaults reference, and verify it against the live signals; note if the consensus has moved since that snapshot.

## Recommend

Present the top one or two candidates with the evidence, a one-line rationale, and the tradeoff of each. Recommend, then let the user decide; on a project that already uses a comparable library, defer to it unless there is a strong, stated reason to switch. Never install silently.

## Rules

- **Bias to fewer dependencies.** Every add is permanent until proven otherwise. The strongest recommendation is often "you do not need this".
- **Current over remembered.** Verify adoption against live data when you can; say so when you could not and are going on a snapshot.
- **Fit beats popularity.** The most-starred option is wrong if it ships no types or bloats a mobile bundle. Weight fit for the surface.
- **Match the project first.** An installed, comparable library wins over a marginally better new one; consistency has value.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It is only a few kilobytes" | Bundle size is the smallest of the costs. The permanent ones are maintenance, security surface, and how hard it becomes to remove |
| "Everyone uses it" | Popularity is one signal of four, and the one most likely to be recalled from a stale snapshot rather than checked |

## When this does not apply

Skip the comparison where the project already uses a library for this job, which is a resolution rather than a choice, and where the user has decided already and asked you to install a specific package. Say once what the alternative would have been if you think it matters, then do as asked.
