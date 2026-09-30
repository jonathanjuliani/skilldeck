<!-- jon-skills:routing:begin -->
## Skill routing

Which skill to reach for, by the moment it comes up. Each entry fires **once per task, not once per message**: if it has already run for the work in hand, it does not run again. This list routes only, and the skill itself carries the method, so open it rather than acting on the line here.

| Moment | Reach for |
| --- | --- |
| First turn of a non-trivial task, before any code | `align-first`. If nobody answers, proceed under the stated assumption rather than waiting |
| A choice of package manager, test runner, linter, validation or naming comes up | `resolve-conventions` |
| Deciding where a new package, module or folder belongs | `project-shape` |
| A new or changed surface, before components or styling | `design-brief` |
| About to install or choose a library | `dependency-choice` |
| Writing a new unit with its own folder, wiring or public surface | `create` |
| Restructuring existing code without changing what it does | `refactor` |
| Retiring a dependency, API or pattern the code still uses | `migration` |
| Deciding what to test and at which seam | `testing-strategy` |
| Before saying anything is done, fixed, passing, green or ready | `verify-before-done` |

Anything not listed is still available; these are the moments that recur often enough to be worth naming.
<!-- jon-skills:routing:end -->
