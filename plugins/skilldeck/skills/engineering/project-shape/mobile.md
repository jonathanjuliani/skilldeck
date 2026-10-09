# Mobile structure (React Native)

Organize a React Native app by feature, the same way as web, with the platform differences that matter: navigation, native boundaries, and platform-specific files.

## Feature-first layout (Expo Router shown)

```text
src/
  features/
    <feature>/
      components/
      hooks/
      api/
      <feature>.schema.ts
      <feature>.types.ts
      index.ts
  components/             # shared UI primitives
  hooks/
  lib/                   # helpers, native-safe
app/                     # Expo Router routes (file-based); thin, compose features
assets/
```

With React Navigation instead of Expo Router, replace `app/` with a `navigation/` folder holding navigators and route types, and keep it just as thin.

## Principles

- **Reuse the web mental model.** Feature-first, colocation, server state via a query library, validation at boundaries: all identical to the frontend guidance. Do not invent a separate architecture for mobile.
- **Navigation is thin and typed.** Route files or navigators compose features and pass typed params. Feature logic never lives in a screen wrapper.
- **Isolate the native boundary.** Anything touching native modules, permissions, or device APIs lives behind a small typed wrapper in `lib/`, so the rest of the app stays testable and platform-agnostic.
- **Platform-specific code via file extensions.** Use `.ios.tsx` / `.android.tsx` / `.native.tsx` for genuine platform differences, kept next to the shared file, rather than `Platform.OS` branches scattered through a component.
- **Styling shares the web model where possible.** If the project uses a Tailwind-for-RN approach (resolved via resolve-conventions), the class mental model matches web; otherwise colocate `StyleSheet` with its component.
- **Expo vs bare.** Default to Expo (managed workflow, OTA, prebuild escape hatch). Recommend bare only when a required native module is not supported, and note that tradeoff explicitly.

## Shared code with a web app

If a web and mobile app share logic (domain types, validation, API clients, server-state hooks), that shared code is the signal for a monorepo package. Keep UI components separate per platform; share the non-visual core. See [monorepo.md](monorepo.md).
