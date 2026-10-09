# Document shape

Read this after the project store is a document or collection store. Skip it for relational tables.

- **A document is a fact you read together.** Embed what is always loaded with the parent and has no life of its own. Reference what is loaded alone, shared, or growing without a bound.
- **Identity is on the document.** The id is stable across updates. A field that changes is not an id.
- **Uniqueness still needs an index the store enforces.** A check in the application loses to two concurrent writes.
- **Unbounded arrays are a relationship.** Comments, events, and history that grow forever do not belong inside the parent document. They get their own collection and a reference.
- **A version field is for readers, not for hope.** If old documents must stay readable, say which fields were added and what a missing field means. Do not require every reader to guess.
- **Evolution stays expand, then migrate, then contract.** Write the new field while readers still accept the old one. Backfill. Switch readers. Remove the old field in a later change, with an owner.

The driver and the collection conventions come from the project. This page decides what is embedded, what is referenced, and what must stay unique.
