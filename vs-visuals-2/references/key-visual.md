# Valueships Key Visual — Full Reference

The "key visual" is the flowing-line graphic that gives every Valueships asset a recognizable signature. From the brand book:

> "The shape made [of] lines that blends from the small shape to the most external, biggest one. Through proper trimming and enlargement, Key Visuals lose their original form and create a modern design that distinguishes the brand in the eyes of the viewer."

In plain terms: concentric organic shapes drawn as thin pink lines, cropped so part of the pattern falls off the canvas, anchored in corners or along edges.

## Anatomy

Every key visual variant shares these properties:

1. **Concentric / nested lines.** A series of similar shapes nested inside one another, growing outward.
2. **Thin stroke weight.** Lines are typically 0.5–1.5pt — never thick or marker-style.
3. **Brand pink stroke.** `#FF005E` is the default. White lines are used when the key visual sits on a full-pink background (e.g. brand book cover). Dark variants (navy/grey) appear occasionally for special purposes.
4. **No fill.** Strokes only — the negative space between lines is the design.
5. **Cropped / trimmed.** The shape always extends beyond the canvas edge. You never see the "full" key visual — only a slice.
6. **Anchored to corners or edges.** Never centered as a primary subject. It's a frame element, not a focal point.

## Variants (shown across brand book pages 8, 13–21)

The brand book showcases several variants of the same flowing-line idea. Use whichever fits the composition:

### 1. Organic blob (page 8)
Closed, kidney-bean-like shape made of nested rings. Lines flow around a center point with subtle asymmetry — feels hand-drawn but precise. Best for: hero covers, large empty canvases.

### 2. Ribbon / chevron (page 14)
Lines bend at a soft angle, creating a wave or chevron form that flows from one edge to another. Pink version on the left, dark navy on the right in the brand book. Best for: dynamic compositions, deck transitions.

### 3. Elliptical / orbital (page 15)
Concentric ovals nested around a tight inner ellipse, suggesting orbits or layers. Often rendered in dark blue. Best for: technical/data-heavy contexts where the organic blob feels too soft.

### 4. Striped corner (page 16)
Tight parallel curves bending into a corner. Almost like a topographic map of a steep slope. Best for: bold corner anchors on social media images.

### 5. Wave / arc (page 17)
A single arc cropped at the bottom or top edge, showing only the curve. Quietest variant. Best for: minimal documents, LOP pages.

### 6. Paper plane outline (page 18)
Wireframe of the brand's arrow icon, scaled up dramatically and outlined. Brand-mark callback. Best for: covers, conference materials, brand-heavy contexts.

### 7. Gradient triangle (page 20)
A single tall triangular shape with pink-to-transparent gradient fill. Calmer, more architectural. Best for: cover slides, hero sections, behind-text decoration.

## Placement rules

- **Corners are home base.** Top-left, top-right, bottom-left, bottom-right. The shape should appear to enter from outside the canvas.
- **Two corners maximum** in a single asset (typically diagonal — e.g. top-left + bottom-right). More than two becomes cluttered.
- **One corner is often enough**, especially for deck slides and document pages.
- **Don't cross the content.** The key visual should occupy the margin, not the main content area. Aim for the lines to take up no more than ~20% of canvas area.
- **Behind, not in front.** The key visual is always behind text and primary content. Set its z-order to the lowest layer.
- **Match the lightness.** On white backgrounds, use pink lines. On full-pink backgrounds, use white lines. On dark backgrounds, use white or pink lines depending on contrast needs.

## Don'ts

- **Don't center it.** It's a frame, not a focal point.
- **Don't use it as a decoration on top of photos.** The visual was designed for clean white/pink backgrounds.
- **Don't make it thick or "tubular".** Lines are thin and elegant. Thick versions look like a different brand.
- **Don't fill the inside with a color.** Strokes only.
- **Don't use it at full opacity behind body text** — it competes for attention. Use 50–70% opacity if it sits behind content, or move it to a margin.
- **Don't substitute other organic shapes** (e.g. waves from a stock library). The Valueships key visual has a specific character — the asymmetric "wobble" in concentric rings, the gradual scaling outward. Stock waves don't read as Valueships.

## Rendering the key visual in code

For Python/matplotlib output, use the helper in `assets/key_visual.py`:

```python
from key_visual import draw_key_visual_corner

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_aspect('equal'); ax.axis('off')

# Place in two corners — most common pattern
draw_key_visual_corner(ax, corner='topleft', color='#FF005E')
draw_key_visual_corner(ax, corner='bottomright', color='#FF005E')

# ... your content here
```

For HTML/SVG output, an inline SVG snippet is in `assets/key_visual.svg`. Reference or paste it directly into your markup.

## Mental model

Think of the key visual like a watermark from a fine paper: it's there to tell the reader *this is from Valueships*, but it never competes with the content. If a viewer notices the key visual before the headline, you've made it too dominant. If they couldn't tell you the asset was from Valueships without the logo, you've made it too subtle. The sweet spot is felt presence — they register the brand without consciously identifying the shape.
