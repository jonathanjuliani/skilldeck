# App skeleton

Read this after the project is an app, a service, or a client. Skip it for a library.

The skeleton is four things:

- A package manifest whose scripts install, test, and run the process.
- One entry the run script starts. A server listens. A web or mobile app renders one screen. Neither contains a feature.
- One test that fails if that entry cannot be loaded.
- A readme of a few lines: how to install, how to test, how to run. No architecture essay.

`project-shape` has already classified the surface. Put the entry where that layout says, and do not invent a second one here.

Leave authentication, a database, and a sample domain out. Those are the first real unit, and they belong to `create` after this skeleton runs. If this process will serve users, the correlation-id hook and the health of the process are part of finishing the skeleton; per-operation logs and spans arrive with the operation.
