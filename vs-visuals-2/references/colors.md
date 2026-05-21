# Valueships Colors — Full Reference

The Valueships color system is intentionally narrow. Three core colors, plus controlled tints and shades. This narrowness is what makes Valueships visuals recognizable across every touchpoint.

## The three core colors

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| **PINK** (primary) | `#FF005E` | rgb(255, 0, 94) | Dominant brand color. Used in nearly every visual. Hero numbers, headlines, accents, dividers, arrows, logo icon, CTAs. |
| **DARK BLUE** (secondary) | `#0F155B` | rgb(15, 21, 91) | Accentuates the primary. Used sparingly. Single-outcome callouts, one icon, background shapes. |
| **BLACK** (neutral) | `#080808` | rgb(8, 8, 8) | Body text, primary content. |

## The 9:1 rule

Pink and dark blue are not equal partners. The brand book is explicit:

> "The ratio of PINK to BLUE could be expressed as 9:1."

This means: for every blue element in a layout, you should have roughly nine pink elements (or one large pink element matched by a small blue accent). Blue exists to make pink pop — it is never the lead.

**Concrete examples of the 9:1 rule in action:**
- A LinkedIn visual with a pink hero number, pink kicker tag, three pink card accents, pink arrows, pink dividers, pink logo icon — and a single dark-blue "+23% deal size" callout at the bottom. ✓ On-brand.
- A deck slide where the headline, subhead, and three icons are all pink, with one dark-blue stat callout. ✓ On-brand.
- A chart where Pink is series A, Dark Blue is series B at roughly equal visual weight. ✗ Off-brand — blue is competing for attention.
- A poster where the background is dark blue with pink accents. ✗ Off-brand — blue is the dominant carrier.

## Pink shades (for opacity/saturation grading)

The brand book shows pink gradients from full saturation to near-white. Use these for soft fills, gradients, and tint-based hierarchy:

| Name | Hex | When to use |
|------|-----|-------------|
| Pink 100 | `#FF005E` | Full brand pink. Hero. Primary CTAs. Logo icon. |
| Pink 80 | `#FF337E` | Softer hero alternative. Hover states. |
| Pink 60 | `#FF669D` | Secondary accents. Light backgrounds for white text. |
| Pink 40 | `#FF99BD` | Soft fills, decorative shapes. |
| Pink 20 | `#FFD1E0` | Badge backgrounds, soft callout fills, gentle highlights. |
| Pink 5  | `#FFF0F5` | Near-white wash. Section backgrounds. Subtle alternating rows. |

These are derived from the pink palette shown on brandbook page 23. You can also generate them programmatically using opacity (e.g. `rgba(255, 0, 94, 0.2)` for Pink 20).

## Dark blue shades

Similarly graded. Used very rarely — most projects will only ever use Dark Blue 100.

| Name | Hex | When to use |
|------|-----|-------------|
| Dark Blue 100 | `#0F155B` | The single accent moment. |
| Dark Blue 80  | `#3F4480` | Softer accent. Rare. |
| Dark Blue 40  | `#9BA0BD` | Faded accent for subtle decoration. |
| Dark Blue 20  | `#DEDFF5` | Very soft tint, e.g. chart gridlines if you absolutely need blue. |

## Neutrals (extended)

The brand book formally lists only black, but professional asset production needs a richer neutral set. These derived neutrals are safe to use:

| Name | Hex | When to use |
|------|-----|-------------|
| Black | `#080808` | Body text, primary content, headlines on light. |
| Ink soft | `#5A5A5C` | Captions, secondary text, italicized subheads, helper text. |
| Mid grey | `#9A9A9D` | Disabled states, less important metadata. |
| Line grey | `#E8E8EC` | Dividers, card borders, table rules. |
| Off-white | `#F7F7F8` | Subtle section backgrounds (use sparingly — white is usually better). |
| White | `#FFFFFF` | Backgrounds, text on pink/dark blue. |

## Gradients

The brand book uses pink gradients in the key visual and the logo icon (the arrow has a subtle gradient). Recommended gradients:

- **Pink fade:** `#FF005E → #FF669D` (vertical or 45° diagonal). Used for hero shapes and key-visual fills.
- **Pink to transparent:** `#FF005E → rgba(255,0,94,0)`. Used for fade-out edges of the key visual.
- **Brand cover gradient:** `#FF005E → #FF1F75`. The very subtle gradient seen on the brand book cover.

Avoid:
- Pink-to-blue gradients (visually competes, looks unrelated).
- Pink-to-orange or pink-to-red (washes out brand recognition).
- Any rainbow or multi-stop gradient.

## Accessibility

- **Pink on white:** Contrast ratio ~3.5:1. Passes WCAG AA for large text (18pt+ or 14pt bold). Does **not** pass for body text. **Use pink only for headlines, hero numbers, and ≥14pt bold UI elements.** For body copy, use black on white.
- **White on pink:** Contrast ratio ~3.5:1. Same rule: large text only.
- **Black on white:** 19:1, passes everything. Use for body.
- **Dark blue on white:** ~15:1, passes everything. Safe for any text size — but reserve for accent-only use per the 9:1 rule.

If you need pink for small text on a light background, increase weight to bold and size to ≥14pt, or switch to black with a pink underline/accent mark.

## Common color mistakes to avoid

| Mistake | Why it's off-brand | Correction |
|---------|-------------------|------------|
| Body copy in pink | Fails accessibility, dilutes the impact of pink for hero use | Body in black, pink reserved for headlines and accents |
| Pink-to-blue gradient | Treats blue as a partner, breaks the 9:1 hierarchy | Pink-to-pale-pink gradient instead |
| Charcoal grey background | Brand uses white. Grey backgrounds change the feel completely. | Use white. If you need contrast, use pink 5 (`#FFF0F5`). |
| Adding a third "accent" color (green, orange, etc.) | Brand system is intentionally three colors only | Use a pink shade or a neutral grey instead |
| Logo recolored to match background | Logo proportions and colors are fixed | Use the approved logo variant (full color, achromatic, or inverted) |
| Pure red (#FF0000) instead of brand pink | Brand pink is magenta-leaning, not pure red | Always `#FF005E` |
