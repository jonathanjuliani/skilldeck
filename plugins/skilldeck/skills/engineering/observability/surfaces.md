# What to emit, by surface

Read this after you know the surface. Skip it until then. The questions and the three signals in the skill still decide *what* to add; this is what that looks like on each surface.

- **Backend.** Rate, errors and duration per operation. Structured logs with a correlation id. Traces across service and datastore calls. Health that reflects dependencies, not just that the process is alive.
- **Frontend, React.** Real user monitoring for the field measurements, not lab numbers, because your machine is not the user's. Error tracking with source maps uploaded, so a stack trace is readable. Track the failures a user actually experiences: a form that would not submit, a route that would not load. Call the Skill tool with "perf-audit" for the budgets these measurements are checked against.
- **Mobile, React Native.** Crash reporting first, since a crash is invisible otherwise. Startup time and screen transitions. Telemetry has to survive being offline, so buffer and send later rather than dropping.
