# Failure paths

Read this when the code handles a dependency that can fail, time out, or duplicate. Skip it for a pure function with no dependency, including a formatter.

- **Use a deterministic fake, not a count of calls.** The double approves, declines, or times out because of an input the test chooses. Asserting that a function was called once does not prove what was stored.
- **Inject the fault at the seam.** A flag the server already reads, or the test runner's way of failing the network. One fault at a time.
- **Assert the invariant.** Exactly one record exists. No card number in storage or in logs. The total is an integer in minor units. The call count is not the invariant.
- **Two writers at once get a test when the rule is a conditional write.** The pass is the second writer being refused. How to write that update lives in `data-model`. Do not restate it here.
- **Keep it few.** One test per failure class that matters. Not a matrix of every combination.
