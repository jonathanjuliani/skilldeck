# Motion

A second axis next to the layout archetypes in [patterns.md](patterns.md). Archetypes answer what shape the surface is. Motion answers how much the interface moves, what kind of movement it is, and whether that movement earns its place.

Snapshot date: 2026-09. Convention drifts. The project outranks this file. Map intensity onto the motion dial from design-brief: minimal ≈ low/minimal, purposeful ≈ low-to-medium, cinematic ≈ medium-to-high. Complexity is a separate axis: simple/medium/high there is implementation difficulty, not a rename of the intensity dial.

## Intensity

| Level | What it means | When it fits |
| --- | --- | --- |
| **minimal** | Almost no motion. State changes are instant or a short fade. Scroll does not choreograph the page. | Dense tools, tables, regulated and accessibility-critical surfaces, focused checkout where motion competes with the task |
| **purposeful** | Motion explains a change: expand/collapse, route transition, success confirmation, tool feedback on a canvas. Nothing loops for atmosphere. | Product UI, settings, bookers, checkouts, most SaaS marketing that still needs to feel alive without becoming theatre |
| **cinematic** | Scroll, timeline, or ambient motion is part of the first impression. Text, imagery, and transparency often move together. | Brand-led marketing, hardware cinema, portfolios where presence is the product |

Higher is not better. Wrong motion at the wrong density reads as broken or noisy. When unsure, take the lower level.

## Complexity

How hard the motion is to build and to keep accessible, independent of how loud it is. A short fade can be cinematic in intensity if it is the first impression; a WebGL loader is high complexity even when it only explains "still working".

| Level | What it means | When it fits |
| --- | --- | --- |
| **simple** | Opacity, transform, and short state changes. CSS or a small spring. First paint still works if motion is off. | Product chrome, lists, loaders, most SaaS marketing that wants to feel alive |
| **medium** | Scroll-tied or timeline motion: pinned sections, split text, shared-element route changes, media that reveals with the page. One choreography language, not a new trick per block. | Product stories, hardware pages, studio marketing, editorial that uses scroll as structure |
| **high** | WebGL, shader, or physics-heavy motion. Scroll, media, and 3D often share one timeline. Expensive to build, to skip, and to make accessible. | Brand worlds, portfolios where presence is the product, campaign sites with a dedicated motion pass |

Match complexity to the brief, not to taste. High complexity in an operator tool is usually the wrong level, even if the reference is beautiful.

## Types

What kind of movement you are looking up. A capture can carry more than one type when the live read is distinctive for each.

| Type | What it covers |
| --- | --- |
| **loading** | Wait, progress, skeleton, and first-paint substitution. The question is whether the wait explains that work is happening, or only stalls. |
| **transition** | Route, overlay, expand/collapse, and shared-element changes. Motion should keep context so the user knows what became what. |
| **text** | Kinetic type, split reveals, variable-font morph, and headlines that change with scroll or state. |
| **image** | Media reveals, hover substitution, clip or mask, and photography or 3D that moves as evidence rather than as wallpaper. |
| **scroll** | Scroll as structure: smoothing, pinning, scrubbing a timeline, or tying layers to position. Scroll that only fades sections in is usually noise. |

## How to read a reference for motion

Ask four questions, then tag the capture:

1. **What moves?** Type, media, chrome, scroll-linked layers, cursor trails, WebGL.
2. **What does it explain?** A state change, a hierarchy, a product capability, or nothing.
3. **Can the user stop or skip it?** Pause controls, reduced-motion paths, and first paint that still works mid-animation.
4. **How hard is the craft, and which types are distinctive?** Assign complexity and types only when the live read is clear. Do not invent tags to fill the fields.

Record intensity as `motion: minimal | purposeful | cinematic` when the read is clear. Record `motion_complexity: simple | medium | high` and `motion_types` as a list of `loading`, `transition`, `text`, `image`, `scroll` when those are the reason to keep the file. Put transferable craft under Taken; put theatre and signature choreography under Rejected.

When the user asks for more motion on a surface, filter the seed by type and complexity against the brief, then open those files. Intensity still has to fit the audience: cinematic scroll on a dense table is the usual failure. The lookup table is in [references/README.md](references/README.md).

## What does not transfer

- A named hero animation or signature scroll sequence (identity).
- Ambient loops that never explain a change (noise and an accessibility debt).
- Scroll-entrance on every section at scanning density (fights the job).
- Full-viewport cinematic defaults borrowed into operator tools.
- Implementation recipes (a named library, a timeline of durations). Record the finding: "scroll position equals state", not the tool that produced it.

## Related

- Reading method: this skill's Motion step in [SKILL.md](SKILL.md).
- Dial mapping: Call the Skill tool with "design-brief".
- Build constraints: Call the Skill tool with "frontend-craft" for duration, easing, and `prefers-reduced-motion`.
