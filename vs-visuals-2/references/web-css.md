# Valueships Web / CSS — Ready-to-Paste Snippets

Drop-in CSS for any Valueships-branded web asset, email template, or HTML mockup.

## CSS Variables (the brand system in code)

```css
:root {
  /* Brand colors */
  --vs-pink: #FF005E;
  --vs-pink-80: #FF337E;
  --vs-pink-60: #FF669D;
  --vs-pink-40: #FF99BD;
  --vs-pink-20: #FFD1E0;
  --vs-pink-5:  #FFF0F5;

  --vs-blue: #0F155B;
  --vs-blue-40: #9BA0BD;
  --vs-blue-20: #DEDFF5;

  /* Neutrals */
  --vs-black: #080808;
  --vs-ink-soft: #5A5A5C;
  --vs-grey-mid: #9A9A9D;
  --vs-line: #E8E8EC;
  --vs-off-white: #F7F7F8;
  --vs-white: #FFFFFF;

  /* Typography */
  --vs-font-display: 'Lato', system-ui, -apple-system, sans-serif;
  --vs-font-body: 'Roboto', system-ui, -apple-system, sans-serif;

  /* Spacing scale (8pt grid) */
  --vs-space-1: 4px;
  --vs-space-2: 8px;
  --vs-space-3: 16px;
  --vs-space-4: 24px;
  --vs-space-5: 32px;
  --vs-space-6: 48px;
  --vs-space-7: 64px;
  --vs-space-8: 96px;

  /* Border radius */
  --vs-radius-sm: 6px;
  --vs-radius-md: 12px;
  --vs-radius-lg: 24px;
  --vs-radius-pill: 999px;
}
```

## Font import

Add this to the `<head>` of any HTML document or at the top of your CSS:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;500;700;900&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
```

Or in CSS:

```css
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;500;700;900&family=Roboto:wght@400;500;700&display=swap');
```

## Base typography

```css
body {
  font-family: var(--vs-font-body);
  font-weight: 400;
  font-size: 16px;
  line-height: 1.4;
  color: var(--vs-black);
  background: var(--vs-white);
}

h1 { font-family: var(--vs-font-display); font-weight: 500; font-size: clamp(40px, 6vw, 60px); line-height: 1.3; margin: 0 0 var(--vs-space-4); }
h2 { font-family: var(--vs-font-display); font-weight: 400; font-size: clamp(32px, 4.5vw, 48px); line-height: 1.2; margin: 0 0 var(--vs-space-4); }
h3 { font-family: var(--vs-font-display); font-weight: 400; font-size: 32px; line-height: 1.2; margin: 0 0 var(--vs-space-3); }
h4 { font-family: var(--vs-font-display); font-weight: 400; font-size: 24px; line-height: 1.2; margin: 0 0 var(--vs-space-3); }
h5 { font-family: var(--vs-font-display); font-weight: 700; font-size: 20px; line-height: 1.2; margin: 0 0 var(--vs-space-2); }
h6 { font-family: var(--vs-font-display); font-weight: 700; font-size: 16px; line-height: 1.3; margin: 0 0 var(--vs-space-2); }

.caption { font-size: 12px; color: var(--vs-ink-soft); }
.lead { font-size: 18px; line-height: 1.5; color: var(--vs-ink-soft); }
```

## Components

### Pink CTA button

```css
.vs-btn {
  font-family: var(--vs-font-body);
  font-weight: 600;
  font-size: 16px;
  padding: 12px 24px;
  background: var(--vs-pink);
  color: var(--vs-white);
  border: none;
  border-radius: var(--vs-radius-pill);
  cursor: pointer;
  transition: background 150ms ease, transform 150ms ease;
}
.vs-btn:hover {
  background: var(--vs-pink-80);
  transform: translateY(-1px);
}

.vs-btn--secondary {
  background: transparent;
  color: var(--vs-pink);
  border: 2px solid var(--vs-pink);
}
.vs-btn--secondary:hover {
  background: var(--vs-pink-5);
}
```

### Kicker tag (eyebrow label)

```css
.vs-kicker {
  display: inline-block;
  font-family: var(--vs-font-display);
  font-weight: 700;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--vs-white);
  background: var(--vs-pink);
  padding: 6px 16px;
  border-radius: var(--vs-radius-pill);
}
```

### Card with pink accent stripe

```css
.vs-card {
  background: var(--vs-white);
  border: 1px solid var(--vs-line);
  border-radius: var(--vs-radius-md);
  padding: var(--vs-space-5);
  position: relative;
  overflow: hidden;
}
.vs-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: var(--vs-pink);
}
```

### Pink divider

```css
.vs-divider {
  border: none;
  height: 1px;
  background: var(--vs-pink);
  opacity: 0.5;
  margin: var(--vs-space-5) 0;
}
```

### Hero number

```css
.vs-hero-number {
  font-family: var(--vs-font-display);
  font-weight: 900;
  font-size: clamp(64px, 10vw, 120px);
  line-height: 1;
  color: var(--vs-pink);
  letter-spacing: -0.02em;
}
```

## Logo (CSS-only fallback)

If the SVG logo isn't available, you can build a simplified version with CSS:

```html
<div class="vs-logo">
  <span class="vs-logo__arrow" aria-hidden="true"></span>
  <span class="vs-logo__wordmark">Valueships</span>
</div>
```

```css
.vs-logo { display: inline-flex; align-items: center; gap: 8px; }
.vs-logo__arrow {
  width: 0; height: 0;
  border-left: 9px solid transparent;
  border-right: 9px solid transparent;
  border-bottom: 22px solid var(--vs-pink);
  position: relative;
}
.vs-logo__arrow::after {
  content: '';
  position: absolute;
  bottom: -22px; left: -3px;
  width: 0; height: 0;
  border-left: 3px solid transparent;
  border-right: 3px solid transparent;
  border-top: 6px solid var(--vs-white);
}
.vs-logo__wordmark {
  font-family: var(--vs-font-display);
  font-weight: 700;
  font-size: 22px;
  color: var(--vs-black);
}
```

For final/production work, always use the official SVG logo file. This CSS version is for quick mockups and email templates where SVG is awkward.

## Key visual (inline SVG)

Place this SVG in the top-left corner of any HTML asset:

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"
     style="position: absolute; top: 0; left: 0; width: 200px; height: 200px; pointer-events: none; z-index: 0;">
  <g fill="none" stroke="#FF005E" stroke-width="1" opacity="0.7">
    <path d="M -10 -10 Q 30 50, 80 -10" />
    <path d="M -10 0 Q 35 60, 90 -10" />
    <path d="M -10 10 Q 40 70, 100 -10" />
    <path d="M -10 20 Q 45 80, 110 0" />
    <path d="M -10 30 Q 50 90, 120 10" />
    <path d="M -10 40 Q 55 100, 130 20" />
    <path d="M -10 50 Q 60 110, 140 30" />
    <path d="M -10 60 Q 65 120, 150 40" />
    <path d="M -10 70 Q 70 130, 160 50" />
    <path d="M -10 80 Q 75 140, 170 60" />
  </g>
</svg>
```

Mirror this horizontally + vertically for the bottom-right corner. Set `opacity` lower (0.3–0.5) if it competes with foreground content.

## Email-safe variant

Most email clients strip external fonts and CSS variables. For email templates, use system fonts as a fallback and inline all styles:

```html
<table style="font-family: Lato, Arial, sans-serif; color: #080808;">
  <tr><td style="font-size: 32px; font-weight: 500; color: #FF005E;">$70,000</td></tr>
  <tr><td style="font-family: Roboto, Arial, sans-serif; font-size: 16px; line-height: 1.4;">
    Body copy here.
  </td></tr>
</table>
```

Pink (`#FF005E`) and Black (`#080808`) render reliably across all email clients. Avoid CSS gradients and SVGs in email — use solid-color shapes instead.

## Accessibility quick wins

- Always pair pink text with a font weight of at least 500 (Lato Medium) and a size of at least 18px for legibility.
- Body copy should be black (`#080808`) on white, never pink.
- Buttons should have a minimum 44×44px touch target on mobile.
- Test with `prefers-reduced-motion`: avoid animating the key visual; static is fine.
