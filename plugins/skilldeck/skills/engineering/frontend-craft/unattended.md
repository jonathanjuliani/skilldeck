# Unattended surfaces

Read this when the brief named an unattended or shared device: a kiosk, a ticket machine, a check-in terminal, a point of sale, an in-car screen. Skip it for a desktop or phone app a person owns.

The brief already decided the kind. This page is how to build it. Do not apply these rules to a surface the brief did not name.

- **An attract screen, and an idle reset with a visible countdown.** The reset wipes the in-progress work and anything personal, so the next person sees a clean screen. Pause the countdown while an outcome is still unknown.
- **One primary action per screen, in the same place every time.** Full screen, fixed zones, no page scroll.
- **Targets are larger than the touch floor.** The floor in [design-defaults.md](design-defaults.md) is 44px. Standing, hurried use wants 56 to 64px, with space between targets so a miss hits nothing.
- **No hover-only affordance, no system keyboard, no long-press menu on a control.** Touch does not hover. A number or a code uses an on-screen keypad. Set `touch-action: manipulation` and `overscroll-behavior: none`, and do not let a control select text.
- **Type is readable at arm's length.** Start above the 16px body floor in [design-defaults.md](design-defaults.md).
- **Controls sit where a standing person can reach them.** Accessibility law for a shared machine is the reason, not a preference. Contrast and the 44px floor still hold. This page only raises them.
- **Every failure has recovery copy for someone with nobody to ask.** One action, plain language, no status code.
