# Controls by surface

Read this after you know whether the change is backend, React web, or React Native. Skip it until the surface is known.

- **Backend.** Authorization per object, parameterized data access, rate limiting on anything expensive or guessable, validated environment, no secret in a log, least privilege on the database and cloud credentials.
- **Frontend, React.** Nothing secret reaches the bundle, and no authorization decision is made only in the client. Treat the UI as a convenience over the server's rules. Sanitize any raw HTML, and keep tokens out of URLs and out of storage that other scripts can read.
- **Mobile, React Native.** The bundle ships to the device and can be read, so it holds no secret. Credentials belong in the platform keychain or keystore, never in async storage. Certificate handling stays strict; disabling validation for a staging environment has a way of shipping.
