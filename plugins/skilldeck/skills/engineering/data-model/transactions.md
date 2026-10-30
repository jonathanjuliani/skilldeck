# Transactions

Read this when one operation writes more than one row, or two writers can touch the same row. Skip it for a single-row insert nobody else is racing.

- **One database transaction is enough when every write is local and short.** Work that calls another system, or that must survive a crash between steps, is a state machine across records, not a longer transaction. Record the intent, commit, then call out. A timed-out call is unknown until you query it by the same idempotency key. Do not retry it blind.
- **Prefer a conditional write over read-then-write.** `UPDATE stock SET qty = qty - :n WHERE id = :id AND qty >= :n`, then check that a row changed. Two writers that both read the same quantity and both write will oversell. An optimistic `version` column is the same rule: update only where the version you read is still current, and retry the loser with the same idempotency key.
- **Name the anomaly you cannot accept, then pick the isolation that stops it.** The project's engine wins where its behavior differs.

| Level | Still allows | Stops |
| --- | --- | --- |
| Read committed | lost update, write skew, phantom | dirty read |
| Repeatable read or snapshot | write skew on PostgreSQL | lost update on PostgreSQL, which aborts the second writer |
| Serializable | none of the above | all of them, and the cost is retries |

- **Lock a row when the next statement depends on the value you just read and a conditional write is not enough.** `SELECT ... FOR UPDATE`. `SKIP LOCKED` is for a queue, where the next worker should take a different row instead of waiting.
- **Retry a serialization failure a bounded number of times, with the same idempotency key.** A new key on that retry is a second effect.
- **Keep the transaction short.** No network call, no user wait, and no external provider inside it.

## When the store is SQLite

SQLite has a single writer. Use WAL, and begin a writing transaction immediately (`BEGIN IMMEDIATE`) so the lock is taken at the start rather than at the first write. Skip this note on any other store.
