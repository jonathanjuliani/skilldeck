<!-- skilldeck-skills:verification:begin -->
## Verification

No completion claim without fresh evidence. Before stating that anything is done, fixed, passing, green, or ready:

1. Name the command that would prove it, and run it in full, now. The project's own test, type check, lint, or build command, not a remembered result from earlier in the session.
2. Read the exit code and the failure count, not only the last line of output.
3. Check that the output answers the claim you are about to make. Passing unit tests do not establish that the reported symptom is gone.
4. Walk what the task actually asked for, item by item, against that output. A green suite is not the same as the thing you were asked for being done.
5. State the claim together with its evidence, or state the real status instead.

The tests are part of the change, not a follow-up. If nothing covers what you changed, write the test. If behavior changed, update the assertions that described the old behavior in the same change. Deleting, skipping, or loosening a failing test is not reaching green, and where it is genuinely right, say so and say why.

"Should work", "seems fixed", and a delegate's report of success are not verification. Where the check is genuinely unavailable, say what you could not verify and what it would take, rather than upgrading an assumption into a claim.

This does not apply to explaining, exploring, or answering a question, where there is no claim to prove.
<!-- skilldeck-skills:verification:end -->
