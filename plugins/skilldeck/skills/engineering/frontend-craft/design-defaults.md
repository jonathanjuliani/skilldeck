# Design defaults

Starting values for the decisions an interface needs before anyone has decided them. This is the design counterpart to the community defaults in `resolve-conventions`, and it works the same way: the project outranks it everywhere. Where a design system, a token set, or an existing screen answers one of these, that answer wins and this file is not consulted.

Snapshot date: 2026-09. The accessibility numbers are from WCAG 2.1 AA and the platform human interface guidelines, so they do not drift. Everything else is convention and should be re-checked when it matters.

## The numbers that are not preferences

These come from the standards, not from taste. They hold at every dial setting.

| Property | Requirement | Note |
| --- | --- | --- |
| Text contrast | 4.5:1 | Against its actual background, including over images and gradients |
| Large text contrast | 3:1 | From 24px, or 19px bold |
| Non-text contrast | 3:1 | Control borders, focus rings, icons carrying meaning, chart series |
| Touch target | 44x44pt iOS, 48x48dp Android | Web pointer targets 24x24px minimum, 44px where the surface is used on touch |
| Focus indicator | Visible, 3:1 against adjacent colour | Never remove an outline without replacing it |
| Text resize | Legible and usable at 200% | Avoid fixed heights on anything holding text |
| Motion | Honour `prefers-reduced-motion` | Offer a static equivalent, do not merely shorten |

## Scales

Pick a scale and hold it. Arbitrary values scattered through a codebase are the main reason an interface stops looking designed.

| Convention | Default | Rationale |
| --- | --- | --- |
| Spacing | A 4px base, used in multiples | Enough resolution without inviting arbitrary numbers |
| Type scale | A ratio around 1.2 for UI, up to 1.333 for marketing | Tighter scales suit dense interfaces, wider ones suit pages with few elements |
| Body text | 16px minimum on web, never below 14px | Smaller is a legibility problem before it is a style |
| Line length | 45 to 75 characters | Applies to prose, not to labels or table cells |
| Line height | 1.5 for body, tighter for display | Generosity here does more for readability than font choice |
| Radius | One or two values across the whole interface | Mixed radii read as inconsistency, not variety |
| Breakpoints | Set them where the content breaks | Device-named breakpoints age badly |

## Motion

| Property | Default | Note |
| --- | --- | --- |
| Interface transitions | 150 to 250ms | Below 100ms reads as instant, above 400ms reads as slow |
| Entrances and larger movement | 250 to 400ms | Longer only when the movement carries meaning |
| Easing | Ease-out for entering, ease-in for leaving | Constant linear motion looks mechanical |
| Purpose | Every animation explains a change | Motion that decorates becomes noise on the tenth viewing |

## Colour

- **Semantic before literal.** Name a token for its job (`surface`, `border`, `danger`), not its value (`gray-200`). Literal names are what make a theme change a rewrite.
- **Both themes, from the start.** Define the palette by role so a dark theme is a token swap. Retrofitting is where contrast failures come from.
- **Neutral does most of the work.** A restrained interface is largely neutrals, with colour reserved for state, action, and emphasis. Colour applied everywhere stops carrying meaning.
- **State needs more than hue.** Pair every colour-carried signal with an icon, a label, or a shape, for colour vision deficiency and for greyscale.
