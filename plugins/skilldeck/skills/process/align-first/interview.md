# When one pass is not enough

Read this only when the pass failed to land: the restatement came back wrong, a branch has no default safe enough to proceed under, or the cost of guessing wrong is a rewrite rather than an edit. A pass that landed is the normal outcome and needs nothing further.

Then work the branches one question at a time:

- **One question per turn, never a list.** A list gets answered in aggregate, which is how the branch that mattered comes back unanswered.
- **Carry your recommended answer with every question.** The person should be able to accept rather than compose, because reading a proposal is cheaper than authoring a decision.
- **Read before you ask.** Anything the codebase, the tracker, or the conversation can answer is not a question, and resolving it yourself is the work.
- **Walk branches in dependency order.** A parent's answer routinely deletes its children, so asking a child first spends a question on something that was about to become irrelevant.

## What keeps it from running forever

**The branch list is the budget.** Declare the branches as a numbered list before asking anything, then walk that list and stop. The bound comes from the work rather than from an arbitrary quota. A new question may join the list only when an answer actually opened it, and only if you name which answer opened it. A branch that appears from nowhere is the interview generating its own fuel.

**Only branches are askable.** The definition from step 3 of the pass holds unchanged: a branch produces materially different work, and everything else is an assumption you resolve and list. This is what keeps the interview on what matters instead of drifting into naming, preferences, and edge cases. The format makes each question feel individually justified, so the filter matters more here than in the pass, not less.

**Every question names what prompted it**: a line in the request, a file you read, a screen that exists, a constraint in the config. A question that cannot name its grounding is usually about a system that is not there, which is what a hallucination looks like from the inside of an interview.

**Three stops, any one of which ends it:**

- The declared list is exhausted.
- Two consecutive answers leave the restated reading unchanged. Diminishing returns you can observe, rather than a judgement about whether more questions would help, which is the judgement that never converges.
- The person says stop, redirects, or answers something other than what was asked. Their attention is the budget being spent, and calling time on it is theirs to do.

**Never re-ask a closed branch.** Answered explicitly or answered by implication, it is closed. Re-raising it is the signature of a loop and the fastest way to lose the format.

**It ends in the same artifact as the pass**: the reading, the assumptions, what is still open and the default you are proceeding under. Whatever a stop leaves unresolved becomes a stated assumption under step 5 of the pass and the work continues. An interview with an ending but no terminal state is one the work never restarts from.

For a standalone stress-test session rather than an escalation from a pass, `mattpocock/skills` ships `grill-me` and `grill-with-docs`, which are the reference implementations of the relentless version.
