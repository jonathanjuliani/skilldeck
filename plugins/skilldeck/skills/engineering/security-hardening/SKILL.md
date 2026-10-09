---
name: security-hardening
description: Find where untrusted data or untrusted actors reach something that matters in a JS/TS backend, React web app, or React Native app, and put the right control there. Use when adding authentication or authorization, handling user input, storing or logging sensitive data, integrating an external service, reviewing code for vulnerabilities, or hardening before a launch. Not for shaping the contract a payload arrives through, which is api-design, and not for judging the supply-chain risk of a package you are about to add, which is dependency-choice.
---

# Security hardening

Locate the points where a system extends trust, then justify or control each one. This skill is about boundaries and the assumptions crossing them, not about running a scanner and closing tickets.

The defining constraint: the question is never "is this code secure", which has no answer, but "what does this code trust, and what makes that trust justified". Every real vulnerability is a place where trust was extended without anyone deciding to extend it. Find those, and the controls become obvious.

## Classify the trust

Sort every input into one of three tiers, and know which tier you are in at all times:

- **Untrusted.** Anything that crossed a network or a user: request bodies, params, query strings, headers, cookies, uploaded files, webhook payloads, third-party API responses, and anything read back from a client. Data does not become trusted by having been stored; a value a user wrote into your database is still theirs.
- **Validated.** Untrusted data that has passed through a schema at the boundary and come out typed. Validation converts, it does not merely check. Call the Skill tool with "api-design" for how the boundary is shaped.
- **Trusted.** Values your own code produced, and configuration you control. This is the only tier that may reach logic without a guard.

Most vulnerabilities are a tier confusion: something untrusted was read as though it were trusted, usually because it arrived by a path nobody was thinking about.

When you have classified the trust and need the ranked catalog of what actually goes wrong, read [threats.md](threats.md). Do not load it to invent a scan list before you have a boundary. For a package you are about to add, call the Skill tool with "dependency-choice" rather than duplicating that judgement here.

After you know whether the change is backend, React web, or React Native, read [surfaces.md](surfaces.md) for the controls that apply there. Skip it until the surface is known.

## Rules

- **Server-side or it did not happen.** A control the client enforces is a hint. Duplicate it in the UI for feedback, never for protection.
- **Validate at the edge, once, into a type.** Re-checking the same value in five places means nobody knows where the boundary is.
- **Deny by default.** New routes, new fields, new permissions start closed and open deliberately.
- **Least privilege everywhere.** Tokens, database roles, cloud credentials, and CI secrets get the narrowest scope that works, and an expiry where one is possible.
- **Never invent cryptography.** Use the platform primitive or a maintained library for hashing, signing, and encryption, and use it in the mode its documentation prescribes.
- **A finding is not a fix.** Naming a risk without either closing it or recording it as an accepted, owned decision leaves the system exactly as exposed as before.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "It is internal, nobody outside can reach it" | Internal is a network claim, not a trust claim, and it stops being true the first time something is exposed for an integration. Access control is what makes it internal |
| "The UI does not show that button to those users" | The UI is not the enforcement layer. The request can be made without the UI, and eventually will be |
| "We will add auth before launch" | Authorization designed after the data model is a retrofit through every query. It is cheaper now and it is never cheaper later |
| "The data is already in our database, so it is ours" | A value a user wrote is untrusted no matter how long it has been stored. Stored input is still input |

## When this does not apply

A local script, a prototype nobody will deploy, and a pure refactor of code whose boundaries do not move do not need this pass. Reach for it when something crosses a trust boundary: a new input, a new caller, a new integration, a new place data comes to rest.

The shape survives where the rule yields. On a prototype that may later ship, say which controls you deliberately skipped, so that decision is visible to whoever promotes it rather than being discovered later.

## Before you hand it over

Check the change for the three findings that most often survive a security pass: an endpoint that authenticates but never authorizes the specific object, a value that reaches a query or a command without going through a schema first, and something sensitive that is now in a log, an error response, or a client bundle.

A control nobody tested is a control nobody will notice the removal of, and access checks are removed by accident more often than they are defeated. Pin the negative cases: the wrong user denied, the malformed input rejected. Call the Skill tool with "testing-strategy" for where those sit.

Then call the Skill tool with "verify-before-done", because "hardened" is a claim about paths you did not take, and only the tests you ran say anything about those.
