---
name: data-model
description: Design the entities, invariants, and persistence shape of a JS/TS system before any table, collection, or ORM file is written. Use when adding entities, a schema, or a model migration, or when the user asks how something should be stored, including SQL and ORM questions. Not for the HTTP contract, which is api-design, not for where React state lives, which is state-management, not for retiring a shape the code still uses, which is migration, and not for scaffolding the repository module, which is create.
---

# Data model

Decide what is stored, what must always be true, and how the shape will change, before any persistence file exists. The output is that decision. The files come after it.

The defining constraint: the store records facts the domain already has. A table, collection, or document that appears because the ORM made it easy is a model designed by a tool, and the invariants then live in application code that forgets them.

## Name the facts

List the entities and the invariants that must hold even when no request is running. Uniqueness, required relationships, amounts that cannot go negative, a state that cannot skip a step. An invariant that is only checked in one handler is a comment. Prefer a constraint the store enforces.

Call the Skill tool with "resolve-conventions" and use the store the project already has. Do not introduce a second database, ORM, or migration tool to get a cleaner shape.

When the model stores a credential, personal data, or a fact that decides who may do what, call the Skill tool with "security-hardening" before the shape is settled. Authorization designed after the tables exist is a retrofit through every query.

## Shape the store

After you know which kind of store the project uses, read one companion. Do not open both.

- Relational (tables, rows, foreign keys): [relational.md](relational.md)
- Document (collections, embedded or referenced documents): [document.md](document.md)

State what is denormalized and why. A copy that exists for a read path needs a named owner for how it stays true. A copy with no owner becomes a second source of truth.

Write the evolution note for this change in expand, migrate, contract form: what is added while the old shape still works, what moves, what is deleted later and who deletes it. That note is for a shape something already depends on. The first design of a model nothing calls yet is this skill. Retiring a shape callers still use is `migration`, and this skill does not start that work.

Name which operations need the moment-0 signals (a failure log, a correlation id, a span across the store call, rate, errors, and duration). Do not emit telemetry from the schema. The operation that uses the model gets those signals when `create` or `api-design` writes it.

## Then write the files

Call the Skill tool with "create" for the repository module, the schema file, and the migration the project expects. Call the Skill tool with "api-design" only when this change also adds or changes a consumer-facing contract. A model with no new external contract does not need a new API style.

## Rules

- **Invariants before columns.** If you cannot say what must always be true, you are not ready to name fields.
- **One source of truth.** Denormalize only with a reason and an owner.
- **Match the project's store.** The next migration looks like the last one.
- **The smallest shape that holds today's invariants.** Extra tables for imagined reports are a model for a product you do not have.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "The ORM will pick the keys" | The ORM picks what is convenient to declare, not what the domain is required to keep true |
| "We will normalize once we know the reads" | A shape you ship is a shape something will depend on. Changing it later is a migration, which is the expensive version of deciding now |
| "Store the rest as JSON so we stay flexible" | An untyped bag is flexible until the first invariant lives in it, and then every reader parses a different version |

## When this does not apply

A column or field that follows an existing entity's pattern, and a value that is not persisted, do not need a new model. Follow the entity that is already there.

The shape survives where the rule yields. On a small addition, still name the invariant it relies on, so a later change does not drop it.

## Before you hand it over

Check the decision for the three gaps that show up in the first real write: an invariant enforced only in one handler, a denormalized copy with nobody keeping it true, and an evolution note that deletes the old shape in the same step that callers still need it.
