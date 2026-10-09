# Library skeleton

Read this after the project is a library other packages import. Skip it for an app or service.

The skeleton is four things:

- A package manifest with a name, a main entry, and a test script. No bin, no server, no app runtime.
- One module that exports a single value the test can import.
- One test that imports that value from the public entry, not from an internal file.
- A readme of a few lines: how to install, how to test, what the public entry is.

Do not add a bundler, a documentation site, or a second package. Publish metadata waits until someone is actually publishing. That later step is `release-flow`.

A library runs inside someone else's process. It does not take a logger, a tracer, or an auth scheme of its own. Expose a hook if the host must hear about a failure, and leave the host's telemetry alone.
