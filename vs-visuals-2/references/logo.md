# Valueships Logo — Full Reference

## Anatomy

The logo has two parts:

1. **Icon (sygnet)** — an upward-pointing arrow with a subtle 3D gradient. Symbolizes growth, increase, and the directional value Valueships delivers.
2. **Logotype** — the wordmark "Valueships" set in a clean geometric sans-serif.

Together they form the primary lockup. The icon sits to the left of the wordmark, baseline-aligned with the lowercase characters, and the icon top extends slightly above the cap height of the wordmark.

## Approved versions

### Full color (default)
- Pink arrow + black wordmark on **light backgrounds** (white, pale pink, off-white)
- Pink arrow + white wordmark on **dark backgrounds** (pink, dark blue, black)

### Achromatic
For situations where color reproduction isn't reliable (fax, single-color print, embossed materials) or where the brand pink would clash:
- Black arrow + black wordmark on **light backgrounds**
- White arrow + white wordmark on **dark backgrounds**

That's the entire approved set. No other colorings.

## Protective field

Per brand book page 10:

- **Minimum protective field (`0.5x`):** Half the height of the icon and typography (ascender to baseline, no descender). No other elements may sit closer than this distance to the logo on any side.
- **Full protective field (`x`):** Full logo height. In this larger zone, **no other logotypes** (e.g. co-brand marks, partner logos) may appear.

In practice: give the logo at least the equivalent of one capital "V" of breathing room on every side, and even more from other competing marks.

## Sizing

- **Minimum digital size:** 80px wide. Below this, the arrow detail starts to break down and the wordmark becomes hard to read.
- **Minimum print size:** 20mm wide.
- **Maximum size:** No fixed maximum, but the logo should never compete with the primary content. On most assets it lives in a corner at a discreet scale.

## Placement

- **LinkedIn / social visuals:** Footer area, centered or aligned with key content. Discreet but legible.
- **Slide deck:** Bottom-right corner of each slide, or top-left on the title slide. Same position on every slide for consistency.
- **Document / report:** Top of the first page, then bottom-left or bottom-right of subsequent pages as a running footer.
- **Web header:** Top-left, anchored to the start of the navigation.
- **Email signature:** Below the sign-off text, left-aligned.

## What you absolutely cannot do

These are direct interpretations of the brand book's prohibition on "operations distorting and violating its original form":

- ❌ Don't stretch or squash the logo horizontally or vertically.
- ❌ Don't rotate the logo.
- ❌ Don't change the proportions between icon and wordmark.
- ❌ Don't recolor the arrow to anything other than approved colors.
- ❌ Don't recolor the wordmark to anything other than approved colors.
- ❌ Don't apply drop shadows, glows, bevels, or other effects.
- ❌ Don't outline the logo or convert it to a stroke-only version.
- ❌ Don't crop the logo or remove the icon.
- ❌ Don't place the logo on a low-contrast background where it can't be read.
- ❌ Don't recreate or redraw the logo — always use the official vector file.
- ❌ Don't compose the wordmark in a different typeface.

## Building a logo lockup in code (matplotlib)

For programmatic outputs where embedding the vector logo isn't practical, you can construct a simplified version that respects the brand:

```python
from matplotlib.patches import Polygon

# Pink arrow icon (simplified geometric form)
arrow_x, arrow_y = 41, 4  # anchor point in your coordinate space
arrow = Polygon([
    (arrow_x, arrow_y + 1.6),         # tip
    (arrow_x - 0.9, arrow_y - 0.4),   # bottom-left
    (arrow_x, arrow_y + 0.1),         # inner notch (gives the V-shape)
    (arrow_x + 0.9, arrow_y - 0.4),   # bottom-right
], closed=True, facecolor='#FF005E', edgecolor='none')
ax.add_patch(arrow)

# Wordmark
ax.text(arrow_x + 1.3, arrow_y + 0.5, 'Valueships',
        fontsize=11.5, ha='left', va='center', color='#080808',
        fontfamily='Lato', fontweight='bold')
```

This is acceptable as a logo *stand-in* in code-generated assets. For final deliverables, polished decks, and anything client-facing, always use the official vector logo file.

## Co-branding (Valueships + partner logos)

When placing the Valueships logo alongside a client or partner logo:

- Separate the two logos with at least the full protective field (`x`) of the larger logo.
- Match optical weight, not pixel size — adjust until both feel equally present.
- Default order: Valueships first (left or top) on internal materials; partner first (left or top) on co-authored client materials.
- Use a thin pink vertical line (`#FF005E`, 0.5pt, full logo height) as the divider if a separator is needed.

## File formats

For production work, request the official files in:
- `.svg` (web, infinite scaling)
- `.pdf` (print, layout software)
- `.png` with transparent background, at 1x, 2x, 3x densities (raster fallback)

If you don't have these files, ask before delivering anything client-facing.
