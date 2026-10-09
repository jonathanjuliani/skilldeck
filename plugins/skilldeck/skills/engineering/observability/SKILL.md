---
name: observability
description: Instrument a JS/TS backend, React web app, or React Native app so questions about production can be answered, covering structured logging, metrics, tracing, error tracking, and alerting on symptoms. Use when adding telemetry, shipping something that runs in production, or setting up alerts. Not for diagnosing a local failure whose cause is unknown, which is debug, not for a live production incident, which is mitigate-incident, not for diagnosing and fixing a specific slow path you can already measure, which is perf-audit, and not for the rollout and rollback mechanics of a deploy, which is ship-flow.
---

# Observability

Decide what a running system needs to emit so the questions that will be asked of it can be answered. Instrumentation is added while the code is written, because the moment you need it is the moment you cannot add it.

The defining constraint: instrument for a question, never for coverage. "Log everything" produces a haystack nobody searches and a bill nobody wants. Start from the question you will be asked at three in the morning, which is nearly always "is it broken, for whom, since when, and what changed", and emit exactly what answers it.

## Start from the questions

Before adding a line of telemetry, write down what you will need to know. For most services the list is short and stable:

- Is this working right now, and for what share of requests?
- When did it stop, and what shipped near then?
- Which users or tenants are affected, and how badly?
- Where in the path is the time or the failure going?

Each question implies its own instrument. A question nobody will ask implies nothing, and that is the telemetry to leave out.

## The three signals, and what each is for

- **Logs** answer "what happened in this specific case". Structured, one event per line, machine-parseable fields rather than interpolated prose, because a message you have to write a regex against is a message you will not query. Carry a correlation id so one request can be reassembled across services.
- **Metrics** answer "what is happening in aggregate". For a request-serving system the useful default is rate, errors and duration, tracked per route or operation, with duration as a distribution rather than an average. An average latency hides exactly the users having the worst time.
- **Traces** answer "where did the time go in this path". Most valuable across service and datastore boundaries, which is where the surprises live. A trace with no spans around the database is usually a trace missing its answer.

Errors deserve their own channel. An error tracker that groups occurrences, keeps a stack trace, and carries release and user context turns a wall of log lines into a ranked list of distinct problems.

## Alert on symptoms, not causes

Alert on what a user can feel: elevated error rate, latency past the budget, a queue that is not draining, a job that did not run. Do not alert on causes, because a cause that is not currently hurting anyone is a dashboard entry, not a page.

Every alert needs a human action. An alert that fires and is routinely ignored is worse than no alert, since it trains the team to ignore the next one too, and the next one is the real one. Where an alert has no action, either delete it or write the runbook line that gives it one.

After you know the surface, read [surfaces.md](surfaces.md) for what to emit there. On frontend, field measurements that are over budget belong to perf-audit: call the Skill tool with "perf-audit" when the question is a number you can already measure.

## Moment-0 baseline

When a skill is creating a production path, it calls this one so the signals land in that same change, not after the first failure. Apply this minimum, and skip anything the project already emits for that path. `debug` only backfills a path that already shipped without it. Do not send the work back to the skill that called you.

- **Backend operation.** A correlation id on the request. One structured log on the failure path (operation, error, correlation id, no secrets or personal data). One span across the handler and the datastore or external call. One aggregate signal for that operation: rate, errors, and duration.
- **React or React Native surface.** Error tracking on the failure a user can hit. The client call carries the same correlation id as the server when one exists. React Native also gets crash reporting on that surface. A timing number you can already measure belongs to `perf-audit`, not to a new metric.

A question nobody will ask still implies nothing. Do not add a log per function, a span per line, or a metric labelled by user id.

## Rules

- **Instrument as you build.** Telemetry added after an incident is telemetry that was missing during it.
- **One correlation id, threaded everywhere.** Signals you cannot join are three separate partial stories.
- **Never log a secret or a credential, and never log personal data by default.** Redact at the point of logging rather than by remembering. Call the Skill tool with "security-hardening" for what counts as sensitive here.
- **Sample deliberately, and say so.** High-volume telemetry gets sampled, but keep errors unsampled: the rare event is the one worth having.
- **Cardinality has a cost.** A user id as a metric label will produce a bill and a slow query. Ids belong in logs and traces, not in metric dimensions.
- **The tools come from the project.** Resolve the logger, the metrics client and the tracer rather than introducing a parallel stack. Call the Skill tool with "resolve-conventions".

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "We will add logging if it becomes a problem" | It becomes a problem at the exact moment you cannot deploy calmly. The instrumentation has to predate the incident |
| "The logs are already there, we just need to search them" | Unstructured logs are text, not data. If nobody can write the query in under a minute, nobody will write it |
| "Alert on it so we know" | Knowing is not an action. An alert with no response is noise that erodes the ones that matter |

## When this does not apply

A local script, a prototype, and a library that runs inside someone else's process do not need this. A library should expose hooks and stay out of the host's telemetry decisions rather than shipping its own logger.

The shape survives where the rule yields. On something that may later go to production, say what is not instrumented, so whoever promotes it knows what they will be blind to.

## Before you hand it over

Check the change for the three gaps that surface during the first incident: a failure path that emits nothing, a log line carrying something sensitive, and a new operation with no way to tell whether it is working in aggregate.

Then call the Skill tool with "verify-before-done", because instrumentation is uniquely easy to declare finished without running: the code compiles, the logger is imported, and nobody finds out the field was never populated until the incident it was added for.
