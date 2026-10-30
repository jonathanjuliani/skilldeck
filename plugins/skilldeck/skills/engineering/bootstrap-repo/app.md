# App skeleton

Read this after the project is an app, a service, or a client. Skip it for a library.

The skeleton is four things:

- A package manifest whose scripts install, test, and run the process.
- One entry the run script starts. A server listens. A web or mobile app renders one screen. Neither contains a feature.
- One test that fails if that entry cannot be loaded.
- A readme a stranger can follow without asking. Prerequisites with versions, then install, test, and run. The run path is the one the project actually has, native or a container or both, not a second path invented here. No architecture essay. When the process needs a variable that has no safe default, an example env file lists every variable and contains no real values. When there is seed data, loading it is part of run, not a step the readme forgot. No secrets committed.

`project-shape` has already classified the surface. Put the entry where that layout says, and do not invent a second one here.

Leave authentication, a database, and a sample domain out. Those are the first real unit, and they belong to `create` after this skeleton runs. If this process will serve users, the correlation-id hook and the health of the process are part of finishing the skeleton; per-operation logs and spans arrive with the operation.
