# Resilient client

Read this when the client calls an API whose failure the user would notice. Skip it for a static page with no API calls.

- **Every request has a timeout.** There is no wait-forever. Abort when the timeout fires.
- **Retry only what is safe to repeat.** An idempotent request, or a request that already carries an idempotency key. Do not auto-retry a mutation that has no key. Wait with exponential backoff and full jitter: a random delay between zero and the growing cap, not a fixed delay. Cap the wait, and cap how many times you retry. Do not retry a 4xx, except 408 and 429, and honour `Retry-After` when the response sends it.
- **Three outcomes, not two.** Success, failure, and unknown. A timeout or a dropped connection is unknown: the server may have finished. Show a checking state and poll a status endpoint. Do not show an error that invites the user to repeat the action. Repeating it is how the same attempt runs twice.
- **Serve the last good read, and block the write.** Cache the read model and mark it stale when the API is down. A write that needs the server waits, with a plain message. Do not pretend a write succeeded.
- **A reload resumes an in-flight attempt.** Persist the key and the payload, and on load return to the checking state. Clear them when the outcome is terminal. Where that state lives is decided in `state-management`: session storage, with the key.
- **Online is a hint.** `navigator.onLine` does not mean the API is reachable. A failed request, or a heartbeat, is the signal.
- **Error copy is one action in plain language.** No stack trace and no status code.
- **A small client does not need a retry library.** Backoff with full jitter is a few lines. A library is a dependency decision. Call the Skill tool with "dependency-choice".
