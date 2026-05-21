"""
Valueships LinkedIn visual — complete working example.

This is a reference implementation showing how to compose a fully on-brand
LinkedIn visual using the Valueships brand skill. Copy and modify the content,
keep the structure.

Renders a 1:1 square (1200×1200 final) suitable for LinkedIn feed.

Run:
    python linkedin_example.py
    # Outputs: linkedin_example.png

Requires:
    pip install matplotlib
    bash setup_fonts.sh  # installs Lato + Roboto on Ubuntu/Debian
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

from brand_palette import VS
from key_visual import draw_key_visual_corner


# ─── Content (the only thing you usually edit) ─────────────────────────────
KICKER = 'PRICING AUDIT  ·  $6M ARR SaaS  ·  HEALTHCARE'
HERO_NUMBER = '$70,000'
HERO_LINE = 'left on the table.'
SUBHEAD = 'On 1 in 3 deals. Every quarter. Same product, same sales team.'
SECTION_TITLE = 'Three deals closed. Three completely different value stories.'
BOTTOM_TITLE = 'The fix: extract pricing signal from data you already have.'

CARDS = [
    {'title': 'Dental group',     'sub': '12 locations',
     'pain': '"Front-desk staff spend\n3 hrs/day on insurance\nverification"',
     'paid': '$55K', 'wtp': '$75K',  'gap': '$20K'},
    {'title': 'Specialty clinic', 'sub': 'multi-site chain',
     'pain': '"2 malpractice cases\nlast year from\nincomplete records"',
     'paid': '$60K', 'wtp': '$95K',  'gap': '$35K'},
    {'title': 'Urgent care',      'sub': '30 locations',
     'pain': '"HIPAA audit finding\ncost us $280K\nin remediation"',
     'paid': '$52K', 'wtp': '$120K', 'gap': '$68K'},
]

PIPELINE = [
    ('Sales calls',    VS.PINK,      VS.WHITE),
    ('AI agent',       VS.PINK,      VS.WHITE),
    ('WTP signal',     VS.PINK,      VS.WHITE),
    ('+23% deal size', VS.DARK_BLUE, VS.WHITE),   # single dark-blue accent (9:1 rule)
]


# ─── Render ────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 12), dpi=100)
ax.set_xlim(0, 100); ax.set_ylim(0, 100)
ax.set_aspect('equal'); ax.axis('off')
fig.patch.set_facecolor(VS.WHITE)

# Key visual — two diagonal corners, the social default
draw_key_visual_corner(ax, corner='topleft')
draw_key_visual_corner(ax, corner='bottomright')

# Kicker tag
kicker = FancyBboxPatch((22, 93), 56, 4.4,
                        boxstyle="round,pad=0.3,rounding_size=2.2",
                        linewidth=0, facecolor=VS.PINK, zorder=3)
ax.add_patch(kicker)
ax.text(50, 95.2, KICKER, fontsize=10, ha='center', va='center',
        color=VS.WHITE, fontfamily='Lato', fontweight='bold', zorder=4)

# Hero number — Lato Black, brand pink
ax.text(50, 82.5, HERO_NUMBER, fontsize=82, ha='center', va='center',
        color=VS.PINK, fontfamily='Lato', fontweight='black', zorder=3)

# Headline — Lato Medium (size carries emphasis per brand book)
ax.text(50, 74, HERO_LINE, fontsize=32, ha='center', va='center',
        color=VS.BLACK, fontfamily='Lato', fontweight='medium', zorder=3)

# Subhead — Roboto italic
ax.text(50, 69.5, SUBHEAD, fontsize=13.5, ha='center', va='center',
        color=VS.INK_SOFT, fontfamily='Roboto', style='italic', zorder=3)

# Pink divider — brand signature
ax.plot([12, 88], [64.8, 64.8], color=VS.PINK, lw=1, alpha=0.6, zorder=3)

# Section title
ax.text(50, 61.5, SECTION_TITLE, fontsize=13.5, ha='center', va='center',
        color=VS.BLACK, fontfamily='Lato', fontweight='bold', zorder=3)

# ─── Three deal cards ───
card_top, card_h, card_w, gap = 58, 28, 27, 1.5
start_x = (100 - (3 * card_w + 2 * gap)) / 2

for i, d in enumerate(CARDS):
    x0 = start_x + i * (card_w + gap)
    y0 = card_top - card_h
    cx = x0 + card_w / 2

    # Card body
    ax.add_patch(FancyBboxPatch((x0, y0), card_w, card_h,
                                boxstyle="round,pad=0.2,rounding_size=0.8",
                                linewidth=1, facecolor=VS.WHITE,
                                edgecolor=VS.LINE, zorder=3))

    # Pink top stripe — brand signature
    ax.add_patch(FancyBboxPatch((x0, card_top - 0.6), card_w, 0.6,
                                boxstyle="round,pad=0,rounding_size=0",
                                linewidth=0, facecolor=VS.PINK, zorder=4))

    # Title + subtitle
    ax.text(cx, card_top - 3.2, d['title'], fontsize=13, ha='center', va='center',
            color=VS.BLACK, fontfamily='Lato', fontweight='bold', zorder=4)
    ax.text(cx, card_top - 5.7, d['sub'], fontsize=9.5, ha='center', va='center',
            color=VS.INK_SOFT, fontfamily='Roboto', style='italic', zorder=4)

    # Quote marks + body
    ax.text(cx, card_top - 9.8, '“ ”', fontsize=15, ha='center', va='center',
            color=VS.PINK, fontweight='bold', alpha=0.35, zorder=4)
    ax.text(cx, card_top - 13.4, d['pain'], fontsize=9.3, ha='center', va='center',
            color=VS.INK_SOFT, fontfamily='Roboto', zorder=4)

    # In-card divider
    ax.plot([x0 + 3, x0 + card_w - 3], [card_top - 18.5, card_top - 18.5],
            color=VS.LINE, lw=0.8, zorder=4)

    # Paid → WTP comparison
    ax.text(x0 + 7, card_top - 21, 'Paid', fontsize=8.5, ha='center', va='center',
            color=VS.INK_SOFT, fontfamily='Roboto', zorder=4)
    ax.text(x0 + 7, card_top - 23.7, d['paid'], fontsize=14.5, ha='center', va='center',
            color=VS.BLACK, fontfamily='Lato', fontweight='bold', zorder=4)
    ax.annotate('', xy=(x0 + card_w - 10.5, card_top - 23.7),
                xytext=(x0 + 11, card_top - 23.7),
                arrowprops=dict(arrowstyle='->', color=VS.PINK, lw=2), zorder=4)
    ax.text(x0 + card_w - 7, card_top - 21, 'WTP', fontsize=8.5, ha='center', va='center',
            color=VS.PINK, fontfamily='Roboto', fontweight='bold', zorder=4)
    ax.text(x0 + card_w - 7, card_top - 23.7, d['wtp'], fontsize=14.5, ha='center', va='center',
            color=VS.PINK, fontfamily='Lato', fontweight='bold', zorder=4)

    # Gap badge — pink tint
    ax.add_patch(FancyBboxPatch((x0 + card_w/2 - 5.5, card_top - 27.4), 11, 2.8,
                                boxstyle="round,pad=0.15,rounding_size=0.6",
                                linewidth=0, facecolor=VS.PINK_20, zorder=4))
    ax.text(cx, card_top - 26, f"−{d['gap']} gap", fontsize=9.5,
            ha='center', va='center', color=VS.PINK,
            fontfamily='Lato', fontweight='bold', zorder=5)

# ─── Bottom: pipeline ───
ax.plot([12, 88], [24, 24], color=VS.PINK, lw=1, alpha=0.6, zorder=3)
ax.text(50, 20.8, BOTTOM_TITLE, fontsize=13, ha='center', va='center',
        color=VS.BLACK, fontfamily='Lato', fontweight='bold', zorder=3)

y_pipe, seg_w = 13, 15
total_w = len(PIPELINE) * seg_w + (len(PIPELINE) - 1) * 3
start = (100 - total_w) / 2
for i, (label, color, txt_color) in enumerate(PIPELINE):
    x0 = start + i * (seg_w + 3)
    ax.add_patch(FancyBboxPatch((x0, y_pipe - 2.6), seg_w, 5.2,
                                boxstyle="round,pad=0.15,rounding_size=0.7",
                                linewidth=0, facecolor=color, zorder=3))
    ax.text(x0 + seg_w/2, y_pipe, label, fontsize=11, ha='center', va='center',
            color=txt_color, fontfamily='Lato', fontweight='bold', zorder=4)
    if i < len(PIPELINE) - 1:
        ax.annotate('', xy=(x0 + seg_w + 2.7, y_pipe),
                    xytext=(x0 + seg_w + 0.3, y_pipe),
                    arrowprops=dict(arrowstyle='->', color=VS.BLACK, lw=1.4),
                    zorder=4)

# ─── Logo footer ───
ax.add_patch(Polygon([(41, 5.6), (40.1, 3.6), (41, 4.1), (41.9, 3.6)],
                     closed=True, facecolor=VS.PINK, edgecolor='none', zorder=4))
ax.text(42.3, 4.5, 'Valueships', fontsize=11.5, ha='left', va='center',
        color=VS.BLACK, fontfamily='Lato', fontweight='bold', zorder=4)
ax.text(55, 4.5, '·  pricing that reflects value', fontsize=9.5,
        ha='left', va='center', color=VS.INK_SOFT, fontfamily='Roboto', zorder=4)

plt.savefig('linkedin_example.png', dpi=150, bbox_inches='tight',
            facecolor=VS.WHITE, edgecolor='none', pad_inches=0.3)
print('Saved linkedin_example.png')
