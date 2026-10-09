---
name: agent-instructions
description: Write or improve a repository's agent instructions file (AGENTS.md or CLAUDE.md) so the rules in it are actually followed. Use when the user wants to create, review, shorten, or fix one, when instructions in it are being ignored, when onboarding a repo for agents, or when a rule keeps having to be repeated in conversation. Not for recording which tools a project uses, which is resolve-conventions, and not for the one-time per-repo setup of this pack, which is the user-invoked setup-skills.
---

# Agent instructions

Write the file an agent reads on every turn in this repository, and keep it worth its cost. This skill owns the operating instructions (`AGENTS.md`, `CLAUDE.md`), not the project's vocabulary, which belongs in a separate `CONTEXT.md` (see below).

The defining constraint: every line in this file is paid on every turn, in every session, forever, whether or not it is relevant. That budget is what makes the file good or useless. A short file of rules that bind gets followed; a long file of preferences gets skimmed, and then the rules that mattered get skimmed along with them.

## What belongs in it

Only what an agent cannot work out for itself and would get wrong:

- **Commands it would otherwise guess**: how to run the tests, the type check, the dev server, when they are not the obvious script names.
- **Constraints with consequences**: what must never be edited, what needs a migration, what breaks production, which directory is generated.
- **Non-obvious structure**: where a thing lives when the layout does not say so, and why.
- **Decisions already made**, so they are not relitigated every session.

## What does not belong in it

- **Anything detectable.** The package manager is in the lockfile, the formatter is in its config, the framework is in `package.json`. Writing them down again adds cost and creates a second source of truth that goes stale.
- **General good practice.** "Write clean code", "add tests", "handle errors" are already in the model. They dilute the lines that carry information.
- **Vocabulary and domain concepts.** Those go in `CONTEXT.md`, which is a different document with a different job. See below.
- **Anything aspirational.** A rule the team does not follow teaches the agent that rules here are optional.

## Make the rules conditional

An instruction that applies always competes for attention with every other instruction. An instruction attached to its trigger is quiet until it is relevant, then unmissable. Prefer the conditional form:

- Instead of "always use the repository pattern for data access", write "when adding a query, put it in `db/queries/` and export it through the repository, never call the client from a route".
- Instead of "be careful with migrations", write "when changing a table, add a migration in `migrations/`, never edit an existing one".

The pattern is: name the situation, then the rule, then the failure it prevents where the failure is not obvious. This is also what makes a rule testable, since you can ask whether it fired in the situation it names.

## The other file: CONTEXT.md

An agent instructions file says how to work here. A `CONTEXT.md` says what the words mean here: the domain terms, the concepts the team names in conversation, the distinctions that matter. Keeping them separate is what keeps the instructions file short, and the vocabulary one is the higher-leverage of the two, because every name in the codebase and every sentence an agent writes gets shorter and more accurate once the shared language is written down.

Keep it to terms that are genuinely load-bearing and genuinely local: a word the team uses in a specific way, a distinction outsiders get wrong, a concept with no obvious name. Not a glossary of the whole domain, and nothing a dictionary already covers. One line each.

It is read by the rest of this plugin rather than merely stored: `resolve-conventions` treats it as authoritative for naming, and `ts-standards`, `information-architecture` and `forms` all defer to its terms. `setup-skills` offers to seed a minimal one. Where a project deserves a deeper treatment, a dedicated domain-modeling skill (`mattpocock/skills` ships one) builds and stress-tests the model rather than just recording it.

When you are writing or restructuring the file (not when diagnosing why one is ignored), the outline is in [structure.md](structure.md).

## Improving one that is being ignored

When the user says the agent does not follow the file, diagnose before rewriting:

1. **Measure the length.** Past a screen or two, adherence falls off. The fix is usually deletion, not emphasis.
2. **Count the unconditional rules.** A wall of always-applies instructions is the most common cause. Convert them to their triggers.
3. **Find the rules that are wrong.** A stale instruction that contradicts the code teaches the agent to distrust the file. Remove it or fix it.
4. **Find the rules nothing enforces.** Something a linter, a type, or a CI check could enforce should be enforced there instead, and deleted from here. A rule that a machine can check does not belong in a document.
5. **Only then, strengthen what remains.** Emphasis works when it is rare.

Deleting is the main move. A file that halves in length usually gets followed more, not less.

## Rules

- **Every line earns its place on every turn.** If you cannot say what goes wrong without a line, it goes.
- **Never write what the repo already says.** Detectable facts belong to detection. Call the Skill tool with "resolve-conventions" rather than transcribing the stack into prose.
- **Conditional over absolute.** Attach a rule to the situation that triggers it.
- **Enforce in code where code can enforce it.** A document is the weakest available control, so use it for what nothing else can hold.
- **Show the diff and ask.** This file is the user's, and it shapes every future session. Never rewrite it wholesale without agreement.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "More instructions means better adherence" | The opposite, past a point. Attention is finite, and every added line is taken from the ones already there |
| "It is only one more line" | It is one more line on every turn of every session, and it is never audited again once written |
| "Better to write it down in case the agent forgets" | Then it is written down in case, competing with the rules that are load-bearing. Write it if a specific failure happened, not in case one might |

## When this does not apply

A repo where the file is short, current, and working does not need this. Nor does a one-off script or a throwaway. Reach for it when the file is long, when a rule keeps having to be repeated in conversation, or when nobody can say what is in it.

## Before you hand it over

Check the result for the three things that make these files fail: a rule that restates something detectable from the repo, an unconditional rule that should name its trigger, and a rule nothing enforces that a linter or a type could. Then check the length against what it was, since a rewrite that grew the file has usually made it worse.
