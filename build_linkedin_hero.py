"""Build a 1200x1200 LinkedIn hero social for 'Demystifying the Value of AI'.
Uses the Valueships brand_palette and key_visual modules from vs-visuals."""

import sys, pathlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

# Load vs-visuals brand modules
VS_PATH = pathlib.Path("/sessions/busy-tender-heisenberg/mnt/outputs/vs-visuals/vs-visuals-2/assets")
sys.path.insert(0, str(VS_PATH))
from brand_palette import VS, apply_valueships_style
from key_visual import draw_key_visual_corner

# Try to set Lato font; fall back to system sans gracefully
import matplotlib as mpl
try:
    apply_valueships_style()
except Exception:
    pass
mpl.rcParams.update({
    'font.family': ['Lato', 'DejaVu Sans', 'sans-serif'],
})

# ─── HERO 1 — "0.09%" vs Electric 2.82% ──────────────────────────
fig, ax = plt.subplots(figsize=(12, 12), dpi=120)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_aspect('equal'); ax.axis('off')
fig.patch.set_facecolor(VS.WHITE); ax.set_facecolor(VS.WHITE)

# Key visual in two corners
draw_key_visual_corner(ax, corner='topleft', color=VS.PINK, scale=1.0, alpha_start=0.85, alpha_end=0.25)
draw_key_visual_corner(ax, corner='bottomright', color=VS.PINK, scale=1.0, alpha_start=0.85, alpha_end=0.25)

# Kicker tag (pink pill)
ax.add_patch(Rectangle((9, 87), 28, 4.5, facecolor=VS.PINK, edgecolor='none', zorder=4))
ax.text(23, 89.25, 'AI VALUE RESEARCH · MAY 2026',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=VS.WHITE, family='Lato', zorder=5)

# Hero number — 0.09%
ax.text(50, 70, '0.09%',
        ha='center', va='center',
        fontsize=110, fontweight='black',
        color=VS.PINK, family='Lato', zorder=5)

# Caption under the hero number
ax.text(50, 60.5, "Acemoglu's MIT estimate of LLM-era AI productivity, per year",
        ha='center', va='center', fontsize=14, color=VS.INK_SOFT,
        family='Lato', style='italic', zorder=5)

# Divider
ax.plot([18, 82], [55, 55], color=VS.PINK, linewidth=1.2, alpha=0.6, zorder=4)

# Headline
ax.text(50, 47, 'AI is not yet',
        ha='center', va='center', fontsize=38, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)
ax.text(50, 40.5, 'an electric-scale revolution.',
        ha='center', va='center', fontsize=38, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)

# Comparison line — small grid of waves
comparisons = [
    ('Steam', '0.78%'),
    ('Electric', '2.82%'),
    ('ICT revival', '2.26%'),
    ('LLM-era AI', '0.09%'),
]
x_positions = [18, 38, 58, 78]
y_label = 28
y_value = 22
for x, (label, value) in zip(x_positions, comparisons):
    is_ai = label == 'LLM-era AI'
    color = VS.PINK if is_ai else VS.BLACK
    weight = 'black' if is_ai else 'bold'
    # value
    ax.text(x, y_value, value,
            ha='center', va='center', fontsize=18,
            fontweight=weight, color=color, family='Lato', zorder=5)
    # label
    ax.text(x, y_label, label,
            ha='center', va='center', fontsize=10.5,
            color=VS.INK_SOFT if not is_ai else VS.PINK,
            family='Lato', fontweight='bold' if is_ai else 'normal',
            zorder=5)

# Bottom tagline (pink bold)
ax.text(50, 12.5, 'Gross AI looks like a revolution.',
        ha='center', va='center', fontsize=15, fontweight='black',
        color=VS.PINK, family='Lato', zorder=5)
ax.text(50, 8.5, 'Net AI inside unrestructured organisations',
        ha='center', va='center', fontsize=14, color=VS.BLACK,
        family='Lato', zorder=5)
ax.text(50, 5.5, 'looks like a productivity tool.',
        ha='center', va='center', fontsize=14, color=VS.BLACK,
        family='Lato', zorder=5)

# Logo (simplified) — bottom-left corner
arrow = Polygon([
    (6.5, 1.7),    # tip
    (5.6, 0.3),    # bottom-left
    (6.5, 0.8),    # inner notch
    (7.4, 0.3),    # bottom-right
], closed=True, facecolor=VS.PINK, edgecolor='none', zorder=10)
ax.add_patch(arrow)
ax.text(8.4, 1.0, 'Valueships',
        ha='left', va='center', fontsize=12, fontweight='bold',
        color=VS.BLACK, family='Lato', zorder=10)

plt.tight_layout()
out1 = "/sessions/busy-tender-heisenberg/mnt/artefakty marketingowe - desk research/demystifying-ai-linkedin-hero-1.png"
plt.savefig(out1, dpi=120, bbox_inches='tight', facecolor=VS.WHITE, pad_inches=0)
plt.close()
print(f"Saved: {out1}")


# ─── HERO 2 — "$725B vs 0.09%" ─────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 12), dpi=120)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_aspect('equal'); ax.axis('off')
fig.patch.set_facecolor(VS.WHITE); ax.set_facecolor(VS.WHITE)

draw_key_visual_corner(ax, corner='topleft', color=VS.PINK, scale=1.0)
draw_key_visual_corner(ax, corner='bottomright', color=VS.PINK, scale=1.0)

# Kicker
ax.add_patch(Rectangle((9, 87), 32, 4.5, facecolor=VS.PINK, edgecolor='none', zorder=4))
ax.text(25, 89.25, 'THE MATH DOESN\'T ADD UP',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=VS.WHITE, family='Lato', zorder=5)

# Two-column layout
# Left — $725B
ax.text(28, 75, '$725B',
        ha='center', va='center', fontsize=72, fontweight='black',
        color=VS.PINK, family='Lato', zorder=5)
ax.text(28, 65, 'Big Tech AI CapEx in 2026',
        ha='center', va='center', fontsize=12.5, color=VS.INK_SOFT,
        family='Lato', style='italic', zorder=5)
ax.text(28, 61, '($1 trillion projected 2027)',
        ha='center', va='center', fontsize=10.5, color=VS.INK_SOFT,
        family='Lato', style='italic', zorder=5)

# vs
ax.text(50, 73, 'vs',
        ha='center', va='center', fontsize=22, fontweight='black',
        color=VS.PINK, family='Lato', zorder=5)
# divider line through the middle
ax.plot([42, 58], [70, 70], color=VS.PINK, linewidth=1.5, alpha=0.6, zorder=4)

# Right — 0.09%
ax.text(72, 75, '0.09%',
        ha='center', va='center', fontsize=72, fontweight='black',
        color=VS.DARK_BLUE, family='Lato', zorder=5)
ax.text(72, 65, "Annual productivity uplift",
        ha='center', va='center', fontsize=12.5, color=VS.INK_SOFT,
        family='Lato', style='italic', zorder=5)
ax.text(72, 61, "(Acemoglu MIT, 10-year view)",
        ha='center', va='center', fontsize=10.5, color=VS.INK_SOFT,
        family='Lato', style='italic', zorder=5)

# Divider
ax.plot([18, 82], [53, 53], color=VS.PINK, linewidth=1.2, alpha=0.6, zorder=4)

# Question
ax.text(50, 46, 'A $7.6 trillion infrastructure build',
        ha='center', va='center', fontsize=22, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)
ax.text(50, 40.5, 'against a 0.1% productivity signal.',
        ha='center', va='center', fontsize=22, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)

# Body context
ax.text(50, 30, 'Bain projects $2T of new AI revenue needed by 2030.',
        ha='center', va='center', fontsize=14, color=VS.BLACK,
        family='Lato', zorder=5)
ax.text(50, 26, 'Combined AI app revenue today: under $50B.',
        ha='center', va='center', fontsize=14, color=VS.BLACK,
        family='Lato', zorder=5)
ax.text(50, 21, 'That is a 40× revenue gap.',
        ha='center', va='center', fontsize=16, fontweight='black',
        color=VS.PINK, family='Lato', zorder=5)

# Bottom tagline
ax.text(50, 11.5, 'Demystifying the Value of AI',
        ha='center', va='center', fontsize=15, fontweight='black',
        color=VS.BLACK, family='Lato', zorder=5)
ax.text(50, 7.5, 'Valueships research · May 2026',
        ha='center', va='center', fontsize=11, color=VS.INK_SOFT,
        family='Lato', zorder=5)

# Logo
arrow = Polygon([
    (6.5, 1.7),
    (5.6, 0.3),
    (6.5, 0.8),
    (7.4, 0.3),
], closed=True, facecolor=VS.PINK, edgecolor='none', zorder=10)
ax.add_patch(arrow)
ax.text(8.4, 1.0, 'Valueships',
        ha='left', va='center', fontsize=12, fontweight='bold',
        color=VS.BLACK, family='Lato', zorder=10)

plt.tight_layout()
out2 = "/sessions/busy-tender-heisenberg/mnt/artefakty marketingowe - desk research/demystifying-ai-linkedin-hero-2.png"
plt.savefig(out2, dpi=120, bbox_inches='tight', facecolor=VS.WHITE, pad_inches=0)
plt.close()
print(f"Saved: {out2}")


# ─── HERO 3 — AVI sector heatmap teaser ─────────────────────────
fig, ax = plt.subplots(figsize=(12, 12), dpi=120)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_aspect('equal'); ax.axis('off')
fig.patch.set_facecolor(VS.WHITE); ax.set_facecolor(VS.WHITE)

draw_key_visual_corner(ax, corner='topleft', color=VS.PINK, scale=1.0)

# Kicker
ax.add_patch(Rectangle((9, 87), 36, 4.5, facecolor=VS.PINK, edgecolor='none', zorder=4))
ax.text(27, 89.25, 'THE AI VALUE INDEX (AVI) BY SECTOR',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=VS.WHITE, family='Lato', zorder=5)

# Title
ax.text(9, 80, 'How much value does AI',
        ha='left', va='center', fontsize=30, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)
ax.text(9, 74, 'actually create — by sector?',
        ha='left', va='center', fontsize=30, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)

# Subtitle
ax.text(9, 67, 'Valueships AI Value Index (AVI) = Revenue Impact + Cost Savings, normalised.',
        ha='left', va='center', fontsize=12, style='italic',
        color=VS.INK_SOFT, family='Lato', zorder=5)

# Horizontal bars — top 8 sectors by AVI
sectors = [
    ('Finance back-office', 28.6, VS.PINK),
    ('Marketing creative',  25.5, VS.PINK),
    ('Manufacturing lighthouses', 24.8, VS.PINK),
    ('Legal doc review',    24.6, VS.PINK),
    ('Software development', 21.6, VS.PINK_60),
    ('Consulting',          20.5, VS.PINK_60),
    ('TMT IT',              17.8, VS.PINK_60),
    ('Customer service',    13.4, VS.PINK_40),
    ('Government',           9.3, VS.PINK_20),
    ('Education',            7.4, VS.PINK_20),
]
bar_x_start = 32
bar_x_max   = 88
y_top = 60
y_step = 4.6
max_avi = 30
for i, (name, avi, color) in enumerate(sectors):
    y = y_top - i * y_step
    bar_w = (avi / max_avi) * (bar_x_max - bar_x_start)
    # bar
    ax.add_patch(Rectangle((bar_x_start, y - 1.6), bar_w, 3.2, facecolor=color, edgecolor='none', zorder=4))
    # sector name (left)
    ax.text(bar_x_start - 2, y, name,
            ha='right', va='center', fontsize=11, color=VS.BLACK,
            family='Lato', fontweight='bold', zorder=5)
    # value label (right of bar)
    ax.text(bar_x_start + bar_w + 1.5, y, f'{avi:.1f}%',
            ha='left', va='center', fontsize=12,
            fontweight='black',
            color=VS.PINK if avi >= 25 else VS.BLACK,
            family='Lato', zorder=5)

# Bottom note
ax.text(50, 12, 'Median AVI across 17 sectors: ~15%.',
        ha='center', va='center', fontsize=14, fontweight='medium',
        color=VS.BLACK, family='Lato', zorder=5)
ax.text(50, 8, 'Only 4 sectors clear the 25% threshold for outcome-based pricing.',
        ha='center', va='center', fontsize=12, color=VS.INK_SOFT,
        family='Lato', style='italic', zorder=5)

# Logo
arrow = Polygon([
    (6.5, 1.7),
    (5.6, 0.3),
    (6.5, 0.8),
    (7.4, 0.3),
], closed=True, facecolor=VS.PINK, edgecolor='none', zorder=10)
ax.add_patch(arrow)
ax.text(8.4, 1.0, 'Valueships',
        ha='left', va='center', fontsize=12, fontweight='bold',
        color=VS.BLACK, family='Lato', zorder=10)

plt.tight_layout()
out3 = "/sessions/busy-tender-heisenberg/mnt/artefakty marketingowe - desk research/demystifying-ai-linkedin-hero-3.png"
plt.savefig(out3, dpi=120, bbox_inches='tight', facecolor=VS.WHITE, pad_inches=0)
plt.close()
print(f"Saved: {out3}")
