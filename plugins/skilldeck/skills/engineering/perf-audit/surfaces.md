# Where the costs usually are, by surface

Read this after you know the surface. The loop in the skill still applies; this is the lookup for where the dominant cost usually sits and how to measure it, not a substitute for measuring.

- **Frontend (React web):** unnecessary re-renders (unstable props/context, missing memoization where it pays), oversized JS bundle (code-split routes, drop heavy deps, tree-shake), unoptimized images and fonts, waterfall network requests, layout thrash. Measure with the browser profiler, a Lighthouse/Web Vitals run, and the bundle analyzer.
- **Mobile (React Native):** unvirtualized long lists (use a virtualized list), heavy work on the JS thread blocking interactions, bridge chatter, large startup bundle, unoptimized images. Measure with the RN profiler and device traces, on a real device, not only the simulator.
- **Backend (Node/TS):** N+1 queries and missing indexes (usually the biggest win), synchronous or blocking work on the event loop, missing caching, unbounded concurrency, oversized payloads. Measure with request timing, DB query logs and explain plans, and a flame graph for CPU.
