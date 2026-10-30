# Idempotency

Read this when a mutation can be retried by a client or the network. Skip it for a read, and for a PUT or DELETE that is already idempotent because it names the resource.

The key names one user attempt, not one HTTP call. A new key on every retry is how the same attempt runs twice.

- **The client generates the key once per attempt.** Reuse it on every retry of that attempt, including a timeout where the client does not know whether the server finished. A new attempt, after the user changes what they are submitting, gets a new key. Generating the key inside the request function makes every retry a new attempt.
- **Scope is the key, the caller, and the endpoint.** Say how long the record is kept. After it expires, the same key is a new request, so the window has to outlast any retry the client will still make.
- **Store the request fingerprint and the full response.** A replay with the same body returns the stored response, including the status. The same key with a different body is a conflict (409 unless the project already documents another code). Do not run the mutation again.
- **The same key in flight at once is one execution.** The second request waits, or receives a conflict that means in progress. Enforce that with a unique index or a lock. A check-then-insert lets both through.
- **The record of the key and the side effect commit together.** A key written after the effect, or an effect with no key record, is a duplicate waiting to happen. When the effect is a call to another system, record the attempt, commit, then call out. A timeout leaves the outcome unknown, not failed: query by the same key before any retry, then record what the query found.
- **The usual header is `Idempotency-Key`.** Document it on the contract. A project that already names a different header keeps that header.
- **PUT by id and DELETE by id do not need a key.** Repeating them is the same operation. A POST that creates, charges, or sends does.
