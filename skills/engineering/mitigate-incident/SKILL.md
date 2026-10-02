---
name: mitigate-incident
description: Stabilize a degraded production system before explaining it. Use when the user reports an outage, a production error spike, a failed production deploy, or asks to mitigate or page. Stop the bleeding, then diagnose, communicate, and apply the smallest mitigation. Not for adding telemetry so the next incident is visible, which is observability, not for a planned rollback of a deploy you still control, which is ship-flow, not for a local failure whose cause is unknown, which is debug, and not for a measured slow path, which is perf-audit.
---

# Mitigate incident

Get a production system that is hurting users back to a tolerable state, then explain what happened. The output is a mitigation that is in effect, a status someone can paste, and a note of what was still invisible.

The defining constraint: mitigation before explanation. A clear root-cause write-up of a system that is still failing is the failure mode of this skill.

## Stop the bleeding

Say the severity and the user impact in one line: who is affected, since when, and what they cannot do. If you cannot say that yet, the first action is to find it, not to theorize.

Then take the smallest action that reduces harm: roll back, turn a flag off, or disable the path. Call the Skill tool with "ship-flow" for how this project rolls back or flags a change. Do that before the root cause is known. A mitigation you can undo beats a clever fix you cannot.

Confirm with the user before you change a shared production environment. Leave credentials to them.

## Then learn what the signals say

Call the Skill tool with "observability" and build a timeline from evidence: the symptom, the deploy or config change nearest to it, and which users or tenants are in it. Recent deploys count as evidence. A theory with no timestamp does not.

If the incident is a trust-boundary breach (data exposed, an auth check bypassed, a secret in a log or a client), call the Skill tool with "security-hardening" for the control that should have held. Containment still comes first.

Name any moment-0 signal that was missing and made this slow: no correlation id, no failure log, no span across the failing boundary, no rate, errors, and duration for the operation. Adding it waits until the system is stable. Record it so the next change to that path includes it. Do not hold the mitigation for better traces.

## Tell people, then close

Write a status the user can paste: impact, what you did, what you are watching, and what is still unknown. Update it when those facts change. Do not write a novel.

When the user-visible harm has stopped, tell the user to run `/retro`. That skill is user-invoked, so do not call it yourself. The retro is where the lasting change is chosen. This skill stops at a stable system and a record of what was missing.

## Rules

- **Harm first, cause second.** An unexplained rollback that restores users beats a confirmed diagnosis that does not.
- **The smallest mitigation.** One flag, one rollback, or one disabled path. A rewrite during an incident is a second incident.
- **Evidence, then theory.** Timestamps and deploys before mechanisms.
- **Say what you could not see.** A missing signal named now is the one the next change can add.

## Excuses that do not hold

| Excuse | Why it fails |
| --- | --- |
| "I should understand it before I roll back" | Users are paying for the understanding. Roll back, then understand |
| "I will add the logs as part of the fix" | New telemetry does not mitigate the current impact, and a rushed instrumentation change is another deploy |
| "The status can wait until we know the cause" | People make decisions on silence. A status that says what is unknown is still a status |

## When this does not apply

A local test failure, a slow path you can already measure, and a deploy you are still planning do not need this skill. A prototype nobody else is using does not either.

The shape survives where the rule yields. If you are not in an incident, say so, and do not borrow the incident's permission to skip a review.

## Before you hand it over

Check three things: users are no longer taking the hit you named, the status matches what you actually did, and any missing baseline signal is written down for the next change.

Then call the Skill tool with "verify-before-done" on the mitigation, not on the explanation. The claim is that the user-visible symptom eased, and only a fresh check of that symptom supports it.
