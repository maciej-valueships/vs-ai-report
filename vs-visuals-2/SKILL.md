---
name: vs-visuals
description: VS Visuals — Valueships visual identity and brand guidelines. Use whenever creating ANY Valueships-branded output — LinkedIn posts, social images, presentations, slide decks, pitch decks, proposals (LOPs), case studies, infographics, charts, dashboards, reports, blog headers, web mockups, or email signatures. Trigger on phrases like "Valueships visual", "Valueships post", "Valueships deck", "VS visuals", "our brand", "on-brand", "make it on-brand", "brand book", "brand guidelines", "brand colors", "brand fonts", "Valueships logo", "Valueships pink", "key visual", or any request for an image/visual/graphic aligned with Valueships. Also trigger when redesigning an existing visual to match Valueships, or when the user uploads a Valueships document and asks for derived visuals. Consult this skill BEFORE picking colors, fonts, or layouts for any Valueships-facing output — don't guess at the brand.
---

# VS Visuals — Valueships Brand Skill

This skill captures the Valueships visual identity from the official brand book. Use it for **any** Valueships-branded output — LinkedIn images, decks, reports, proposals, case studies, charts, web mockups. The goal is to produce work that looks like it came out of Valueships itself, not a generic template.

## The brand at a glance

**Tagline / purpose:** Valueships makes companies healthier and more profitable. Pricing and monetization are the lens.

**Visual personality:** Confident, modern, decisive. Lots of white space. Pink is loud and dominant — but used with discipline, not chaos. Dark blue appears sparingly as an accent. Black for text. Clean sans-serif typography. The "key visual" — flowing concentric lines — gives every asset a recognizable Valueships fingerprint.

## Non-negotiables

These rules come straight from the brand book. Treat them as hard constraints.

1. **Pink `#FF005E` is the primary color and must dominate.** It carries the brand. If a Valueships asset has no pink in it, it is off-brand. Use it for hero numbers, key callouts, accent strips, logo arrow, dividers, primary buttons, and the key visual.
2. **Dark blue `#0F155B` is a restrained accent.** Brand book is explicit: the ratio of pink to blue is roughly **9:1**. Blue is for "accentuating the primary color style" — never as a primary color, never as a background, never as a headline color. Examples of valid use: a single final-outcome callout, one icon, a small background shape.
3. **Backgrounds are white.** Pink can be used as a full-bleed background only for hero covers (e.g. the brand book's own cover), not for body content. Default to white.
4. **Logo proportions are sacred.** Never stretch, recolor (outside approved versions), rotate, or distort the logo. Maintain protective field (see `references/logo.md`).
5. **Fonts are Lato and Roboto only.** Lato for headers and ad-style typography. Roboto for body and captions. No substitutions — both are free from Google Fonts.
6. **The key visual is the flowing-line shape.** Cropped/enlarged so its original form is half-hidden, anchored in corners or edges. See `references/key-visual.md`.

If a request would break one of these rules, push back and offer an on-brand alternative.

## Core specs (quick reference)

### Colors
```
PRIMARY (dominant, ~90% of color use)
Pink              #FF005E   — hero numbers, callouts, arrows, accents, logo arrow
Pink secondary    #FF4D8E   — softer pink for gradients, secondary highlights
Pink tint         #FFD1E0   — soft fills for badges, callout backgrounds
Pink wash         #FFF0F5   — near-white pink for full-bleed soft sections

SECONDARY (accent, ~10% of color use, 9:1 ratio to pink)
Dark blue         #0F155B   — single accent moments, never dominant
Dark blue shades  fade toward #DEDFF5 via opacity for soft fills

NEUTRALS
Black             #080808   — primary text
Soft grey         #5A5A5C   — captions, secondary text, italics
Line grey         #E8E8EC   — dividers, card outlines
White             #FFFFFF   — backgrounds
```

Full color system with tints, ratios, and usage rules: see `references/colors.md`.

### Typography
```
HEADERS — Lato
H1   Lato Medium     60pt / line-height 130%
H2   Lato Regular    48pt / 120%
H3   Lato Regular    32pt / 120%
H4   Lato Regular    24pt / 120%
H5   Lato Bold       20pt / 120%
H6   Lato Bold       16pt / 130%
Hero callouts: Lato Black / ExtraBold at 70–90pt

BODY — Roboto
Body              Roboto Regular   16pt / 140%
Body-button       Roboto Semibold  16pt / 140%
Body-small        Roboto Regular   14pt / 140%
Body-small-button Roboto Semibold  14pt / 140%
Caption           Roboto Regular   12pt / 140%
```

Full typography system: see `references/typography.md`.

### Logo
- Wordmark "Valueships" with pink/dark arrow icon (sygnet) pointing up to the left of the text.
- Full-color versions for light and dark backgrounds. Achromatic (black on white / white on black) versions exist for constrained contexts.
- Protective field: minimum 0.5x of the logo height on all sides (full x for placement near other logos).

Full logo guidelines, lockups, do's-and-don'ts: see `references/logo.md`.

### Key Visual
The Valueships "key visual" is a flowing line drawing — concentric organic shapes that scale from a small inner kernel outward to a large external boundary. Used cropped and enlarged so part of it falls off-canvas, giving each design a distinctive trimmed feel. Always in brand pink (with occasional dark-blue variant for special cases). Placed in corners or edges — never centered as a primary subject.

Full key visual rules and rendering code: see `references/key-visual.md`.

## Applying the brand: workflow

When asked to produce any Valueships visual, follow this sequence:

### 1. Identify the deliverable type
Match the request to one of the patterns below. If unclear, ask the user — but try to infer first from the request.

- **LinkedIn / social image** → square 1:1 (1200×1200 or 1800×1800), white background, hero number/headline in pink, key visual anchored in 1–2 corners, Lato Black for hero
- **Slide / deck** → 16:9, white background, lots of whitespace, pink for accents/headlines, Lato for titles, Roboto for body
- **Report cover or hero section** → can use full pink background with white text and white-line key visual (brand book cover style)
- **Report body page or proposal page (LOP)** → white background, generous margins, pink accents only on dividers/headers/callouts, Roboto body
- **Chart / data viz** → white background, pink as primary series color, dark blue as second series, neutrals (grey) for context. Never use more than 3 colors plus neutrals.
- **Web mockup / landing** → white background, pink CTAs and accent shapes, Lato H1 ~60pt, Roboto body 16pt

### 2. Compose with pink leading
Sketch the layout asking: *where does the pink land?* The eye should land on pink first. If you've designed something where blue or black is more prominent than pink, the brand ratio is broken.

### 3. Add the key visual
Almost every Valueships asset benefits from the flowing-line key visual in at least one corner. For LinkedIn-format visuals, two corners (typically top-left and bottom-right, or top-right alone) works well. For deck slides, one corner is usually enough.

### 4. Set typography
Headers in Lato (Black/Bold for hero, Medium for H1, Regular for H2-H4). Body in Roboto Regular. Captions in Roboto 12pt with `INK_SOFT` grey.

### 5. Place the logo
Logo lives in the footer (visuals/decks) or the header (documents/slides). Maintain protective field. Use the right version for the background (pink-on-white, white-on-pink, or achromatic).

### 6. Verify before delivery
Mental checklist:
- [ ] Pink dominates (9:1 ratio with dark blue or higher)?
- [ ] White background or approved pink hero?
- [ ] Lato + Roboto only?
- [ ] Key visual present (flowing lines, cropped, in pink)?
- [ ] Logo present, undistorted, with protective field?
- [ ] No off-brand colors (no red-orange, no green, no purple, no teal)?

## Code snippets

For Python/matplotlib-based output (charts, social images, infographics), use the reusable snippets in `assets/`:

- `assets/brand_palette.py` — Python constants for all brand colors, ready to import
- `assets/key_visual.py` — drop-in function `draw_key_visual_corner(ax, corner='topleft')` that renders the flowing-line key visual in any matplotlib axes
- `assets/setup_fonts.sh` — one-line shell command to install Lato + Roboto on Ubuntu/Debian (used by Claude's code execution environment)
- `assets/linkedin_example.py` — complete working example of an on-brand LinkedIn visual, fork and modify

For HTML/CSS-based output (web mockups, email templates, slides via reveal.js), see `references/web-css.md` for ready-to-paste CSS variables and font imports.

## What to do when a request conflicts with the brand

You will sometimes get requests like "make it teal" or "use Arial" or "put the logo upside down." When that happens:

1. Acknowledge the request without being preachy.
2. Explain the brand constraint in one short line ("Brand pink is the primary — teal would feel off-brand").
3. Offer the closest on-brand alternative ("I can give it a softer pink wash for that calmer feel — want me to try that?").
4. If the user insists, comply but note that the result will be off-brand. Don't lecture.

Brand consistency compounds. One off-brand asset weakens every future one. Hold the line politely.

## When you don't have something

If a request asks for an asset type not covered here (e.g. video lower-thirds, motion graphics, merch), apply first principles from the rules above — pink dominant, Lato + Roboto, white background, key visual where it fits, 9:1 pink-to-blue — and produce the best on-brand interpretation you can. Flag to the user that this is an extrapolation, not a brand-book-codified pattern.

## Reference files

Read these in addition to this SKILL.md when the task calls for it:

- `references/colors.md` — full color system, when to use each shade, gradient rules, accessibility notes
- `references/typography.md` — full typography hierarchy, sizing for different formats, web vs print
- `references/key-visual.md` — key visual anatomy, variants (concentric, ribbon, oval, gradient triangle), placement rules
- `references/logo.md` — logo system, lockups, protective field, do's and don'ts, when to use achromatic
- `references/web-css.md` — ready-to-paste CSS variables, font imports, common component styles
- `references/checklist.md` — pre-delivery checklist for any Valueships visual
