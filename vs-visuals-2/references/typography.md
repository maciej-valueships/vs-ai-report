# Valueships Typography — Full Reference

Two typefaces. That's it.

- **Lato** — headers, hero callouts, advertising-style text
- **Roboto** — body, captions, longer-form reading

Both are from Google Fonts (https://fonts.google.com). Free, web-safe, and universally available. No substitutions.

## Why these two?

The brand book describes Lato as "universal, timeless typography [that] provides adequate readability." Roboto is its body-copy counterpart with similar properties. Together they give Valueships a clean, modern, geometric feel without being trendy. They will not look dated in five years.

## Lato — for headers and hero text

Available weights: Light, Regular, Medium, SemiBold, Bold, ExtraBold, Heavy, Black.

### Heading hierarchy (web/blog spec from brand book page 7)

| Level | Font | Size | Line height |
|-------|------|------|-------------|
| H1 | Lato Medium | 60pt | 130% |
| H2 | Lato Regular | 48pt | 120% |
| H3 | Lato Regular | 32pt | 120% |
| H4 | Lato Regular | 24pt | 120% |
| H5 | Lato Bold | 20pt | 120% |
| H6 | Lato Bold | 16pt | 130% |

Note the brand uses *lighter* weights for the biggest headings (H1 is Medium, not Bold). This is intentional — the size carries the emphasis, not the weight. Heavier weights kick in at H5/H6 where size is no longer doing the work.

### Hero callouts (for social/posters)

For attention-grabbing numbers and bold one-liners on social media or covers:

| Use case | Font | Size |
|----------|------|------|
| Hero number (e.g. "$70,000") | Lato Black | 70–90pt |
| Hero headline (e.g. "left on the table.") | Lato Medium | 28–34pt |
| Subhead | Lato Regular | 13–16pt |
| Kicker tag (e.g. "PRICING AUDIT · SaaS") | Lato Bold | 10–11pt, ALL CAPS, letter-spacing +0.05em |

## Roboto — for body and captions

Available weights: Light, Regular, Medium, SemiBold, Bold, ExtraBold, Heavy, Black.

### Body hierarchy (from brand book page 12)

| Style | Font | Size | Line height |
|-------|------|------|-------------|
| Body | Roboto Regular | 16pt | 140% |
| Body-button | Roboto Semibold | 16pt | 140% |
| Body-small | Roboto Regular | 14pt | 140% |
| Body-small-button | Roboto Semibold | 14pt | 140% |
| Caption | Roboto Regular | 12pt | 140% |

Notice line height is 140% throughout. Tight enough to feel set, loose enough to read comfortably. Don't compress below 130% or open beyond 150%.

## Mixing the two

The standard pattern:

- **Title / section header:** Lato (size depends on hierarchy level)
- **Lead paragraph or subhead:** Roboto Regular 16pt, possibly italic for emphasis
- **Body copy:** Roboto Regular 16pt
- **Bold inline emphasis:** Roboto Bold inline within body
- **Captions / footnotes / metadata:** Roboto Regular 12pt in `#5A5A5C` (ink soft)

Never use Lato for body copy. It works well for short bursts of text (headers, callouts, labels) but feels less natural at paragraph length. Roboto was designed for screen reading.

## Format-specific overrides

### LinkedIn / social square (1200×1200 px)

For attention-grabbing posts, the hero number is much bigger than the brand book's H1 spec would suggest. The proportion that works:

- Hero number: Lato Black, 70–85pt
- Headline below number: Lato Medium, 28–32pt
- Subhead: Roboto Italic, 13–14pt
- Card titles / inline labels: Lato Bold, 12–14pt
- Card body: Roboto Regular, 9–11pt

### Slide deck (16:9, 1920×1080)

- Slide title: Lato Medium, 44–54pt
- Section header: Lato Bold, 20–28pt
- Body bullet: Roboto Regular, 18–22pt
- Caption / source: Roboto Regular, 12–14pt in ink-soft

### Long-form report or LOP (A4 / US Letter)

- Document title: Lato Medium, 32pt
- Section heading: Lato Bold, 18pt
- Subsection: Lato Bold, 14pt
- Body: Roboto Regular, 11pt
- Caption: Roboto Regular, 9pt

## Tracking, weight, and styling

- **Letter-spacing (tracking):** Default to font-native spacing. Add `+0.05em` to `+0.1em` for all-caps labels (kicker tags, button labels, section eyebrows). Don't tighten below default.
- **Italics:** Use sparingly — for subheads, quoted material, and emphasis within body. Don't italicize headers.
- **Underlines:** Avoid in body. Reserved for hyperlinks (pink, no underline by default; underline on hover).
- **All-caps:** Only for short labels (≤6 words). Never for headlines or body.

## Web / CSS implementation

```css
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;500;700;900&family=Roboto:wght@400;500;700&display=swap');

:root {
  --font-display: 'Lato', system-ui, -apple-system, sans-serif;
  --font-body: 'Roboto', system-ui, -apple-system, sans-serif;
}

h1 { font-family: var(--font-display); font-weight: 500; font-size: 60px; line-height: 1.3; }
h2 { font-family: var(--font-display); font-weight: 400; font-size: 48px; line-height: 1.2; }
h3 { font-family: var(--font-display); font-weight: 400; font-size: 32px; line-height: 1.2; }
h4 { font-family: var(--font-display); font-weight: 400; font-size: 24px; line-height: 1.2; }
h5 { font-family: var(--font-display); font-weight: 700; font-size: 20px; line-height: 1.2; }
h6 { font-family: var(--font-display); font-weight: 700; font-size: 16px; line-height: 1.3; }

body { font-family: var(--font-body); font-weight: 400; font-size: 16px; line-height: 1.4; }
.caption { font-family: var(--font-body); font-weight: 400; font-size: 12px; line-height: 1.4; color: #5A5A5C; }
```

## Installing fonts locally (for code-generated assets)

On Ubuntu / Debian (used by Claude's code execution):

```bash
apt-get install -y fonts-lato fonts-roboto
fc-cache -f
```

On macOS: Both ship via Font Book or can be installed from Google Fonts.

On Windows: Download from fonts.google.com and install through Settings → Fonts.

## Common typography mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Body copy in Lato | Less readable than Roboto at paragraph length | Use Roboto Regular 16pt for body |
| Bold headline at H1 size | Brand uses Medium at H1 — size carries emphasis | Use Lato Medium for big headlines |
| Mixing in a third font (e.g. Inter, Open Sans) | Brand system is two fonts only | Lato + Roboto only |
| Pink body copy | Fails accessibility, dilutes pink | Black body, pink accents |
| All-caps headlines | Reserved for short labels (eyebrows, buttons) | Use sentence case or title case |
| 100% line height (no leading) | Cramped, hard to read | Use 120–140% per the spec |
