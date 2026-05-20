"""Build the Valueships speed-of-information-normalized productivity chart.
Argument: AI has the highest information bandwidth in history, yet the lowest
productivity uplift since the agrarian era. The conversion efficiency
(productivity per log-decade of information speed) collapses for AI.
"""

import sys, pathlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
import numpy as np

VS_PATH = pathlib.Path("/sessions/busy-tender-heisenberg/mnt/outputs/vs-visuals/vs-visuals-2/assets")
sys.path.insert(0, str(VS_PATH))
from brand_palette import VS, apply_valueships_style
from key_visual import draw_key_visual_corner

apply_valueships_style()
import matplotlib as mpl
mpl.rcParams.update({'font.family': ['Lato', 'DejaVu Sans', 'sans-serif']})

# ─── DATA ─────────────────────────────────────────────────────
# Information Speed Index = relative bandwidth per worker
#   Agrarian (speech, manuscript) = 1× baseline
#   First industrial (printed press, mail coach, early telegraph by 1860s) = 100×
#   Electric / 2nd industrial (telephone, radio, TV, real-time audio) = 100,000×
#   ICT baseline (digital networks, fax, internet, mobile) = 100,000,000×
#   ICT revival (broadband, web 2.0, smartphones) = 1,000,000,000×
#   LLM-era AI (Gbps fiber, 5G everywhere, AI inference at scale, agents) = 100,000,000,000×
eras = [
    {"era": "Agrarian",
     "period": "post-1600",
     "prod_pct": 0.30,
     "info_speed": 1,
     "log_info": 0,
     "color": VS.PINK_60,
     "is_ai": False},
    {"era": "First\nindustrial",
     "period": "1780-1860",
     "prod_pct": 0.78,
     "info_speed": 1e2,
     "log_info": 2,
     "color": VS.PINK_60,
     "is_ai": False},
    {"era": "Electric /\n2nd industrial",
     "period": "1920-1970",
     "prod_pct": 2.82,
     "info_speed": 1e5,
     "log_info": 5,
     "color": VS.PINK,
     "is_ai": False},
    {"era": "ICT baseline",
     "period": "1970-2015",
     "prod_pct": 1.38,
     "info_speed": 1e8,
     "log_info": 8,
     "color": VS.PINK_60,
     "is_ai": False},
    {"era": "ICT revival",
     "period": "1994-2004",
     "prod_pct": 2.26,
     "info_speed": 1e9,
     "log_info": 9,
     "color": VS.PINK,
     "is_ai": False},
    {"era": "LLM-era AI",
     "period": "2024-2034",
     "prod_pct": 0.09,
     "info_speed": 1e11,
     "log_info": 11,
     "color": VS.DARK_BLUE,   # the single accent — AI is the outlier
     "is_ai": True},
]

# Conversion efficiency: productivity points per log-decade of info speed
# For the agrarian baseline (log = 0), we use 0.30 as the absolute baseline.
# For everything else: prod / log_info_speed.
for e in eras:
    if e["log_info"] == 0:
        e["conv_eff"] = e["prod_pct"]  # baseline anchor
    else:
        e["conv_eff"] = e["prod_pct"] / e["log_info"]

# ─── FIGURE ───────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 10), dpi=120)
fig.patch.set_facecolor(VS.WHITE)

# Two-panel layout — leave clean room at top for title + bottom for tagline
gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1], wspace=0.28,
                       left=0.07, right=0.97, top=0.78, bottom=0.18)

ax_scatter = fig.add_subplot(gs[0, 0])
ax_bars    = fig.add_subplot(gs[0, 1])

# Subtle key visual ONLY in the bottom-right corner (away from text blocks)
ax_kv2 = fig.add_axes([0.80, 0, 0.20, 0.20], zorder=0)
ax_kv2.set_xlim(0, 100); ax_kv2.set_ylim(0, 100); ax_kv2.set_aspect('equal'); ax_kv2.axis('off')
draw_key_visual_corner(ax_kv2, corner='bottomright', color=VS.PINK, scale=0.55, alpha_start=0.45, alpha_end=0.10)

# ─── PANEL 1 — SCATTER (productivity vs info speed) ───────────
x = np.array([e["log_info"] for e in eras])
y = np.array([e["prod_pct"] for e in eras])

# Background gridlines
ax_scatter.set_facecolor(VS.WHITE)
ax_scatter.grid(True, axis='y', color=VS.LINE, linewidth=0.6, zorder=0)
ax_scatter.set_axisbelow(True)

# Plot a faint "expected" trend line — linear in log-info-speed
# Fit a line on the first 5 eras (excluding AI)
non_ai = [e for e in eras if not e["is_ai"]]
x_non_ai = np.array([e["log_info"] for e in non_ai])
y_non_ai = np.array([e["prod_pct"] for e in non_ai])
slope, intercept = np.polyfit(x_non_ai, y_non_ai, 1)
x_trend = np.linspace(-0.5, 12, 50)
y_trend = slope * x_trend + intercept
ax_scatter.plot(x_trend, y_trend, '--', color=VS.PINK_40, linewidth=1.3,
                alpha=0.7, zorder=2,
                label='Expected trend (excl. AI)')

# Scatter points
for e in eras:
    size = 380 if e["is_ai"] else 280
    edge = VS.WHITE
    ax_scatter.scatter(e["log_info"], e["prod_pct"],
                       s=size, c=e["color"], edgecolor=edge,
                       linewidth=2.5, zorder=5)

# Annotate each point
label_offsets = {
    "Agrarian":              ( 0.4,  0.25, 'left',  'bottom'),
    "First\nindustrial":     ( 0.4,  0.25, 'left',  'bottom'),
    "Electric /\n2nd industrial": (-0.4, 0.25, 'right', 'bottom'),
    "ICT baseline":          ( 0.3, -0.35, 'left',  'top'),
    "ICT revival":           (-0.3,  0.25, 'right', 'bottom'),
    "LLM-era AI":            (-0.4,  0.30, 'right', 'bottom'),
}
for e in eras:
    dx, dy, ha, va = label_offsets[e["era"]]
    text_color = VS.DARK_BLUE if e["is_ai"] else VS.BLACK
    weight = 'black' if e["is_ai"] else 'bold'
    ax_scatter.annotate(
        e["era"] + f"\n{e['prod_pct']:.2f}%",
        xy=(e["log_info"], e["prod_pct"]),
        xytext=(e["log_info"] + dx, e["prod_pct"] + dy),
        ha=ha, va=va, fontsize=10.5, family='Lato',
        fontweight=weight, color=text_color, zorder=6,
    )

# Highlight the AI gap with an arrow
ai_e = next(e for e in eras if e["is_ai"])
ai_expected_y = slope * ai_e["log_info"] + intercept
ax_scatter.annotate(
    '',
    xy=(ai_e["log_info"], ai_e["prod_pct"]),
    xytext=(ai_e["log_info"], ai_expected_y),
    arrowprops=dict(arrowstyle='->', color=VS.PINK, lw=2.2, alpha=0.9),
    zorder=4,
)
ax_scatter.text(ai_e["log_info"] - 0.25, (ai_expected_y + ai_e["prod_pct"]) / 2,
                f'  Gap\n  vs trend',
                ha='right', va='center', fontsize=10, family='Lato',
                color=VS.PINK, style='italic', fontweight='bold')

# Axes formatting
ax_scatter.set_xlim(-0.8, 12.2)
ax_scatter.set_ylim(-0.4, 3.5)
ax_scatter.set_xticks([0, 2, 5, 8, 9, 11])
ax_scatter.set_xticklabels(['1×', '100×', '100K×', '100M×', '1B×', '100B×'],
                            fontsize=11, family='Lato', color=VS.INK_SOFT)
ax_scatter.set_yticks([0, 1, 2, 3])
ax_scatter.set_yticklabels(['0%', '1%', '2%', '3%'],
                            fontsize=11, family='Lato', color=VS.INK_SOFT)
ax_scatter.set_xlabel('Information speed — bits/sec/worker, log scale',
                       fontsize=11, family='Lato', color=VS.INK_SOFT, labelpad=8)
ax_scatter.set_ylabel('Annual labour-productivity uplift',
                       fontsize=11.5, family='Lato', color=VS.BLACK, labelpad=10)

# Panel title
ax_scatter.set_title('Productivity by information-speed era',
                      fontsize=15, family='Lato', fontweight='medium',
                      loc='left', pad=14, color=VS.BLACK)

# Hide spines except bottom + left
for spine in ['top', 'right']:
    ax_scatter.spines[spine].set_visible(False)
ax_scatter.spines['left'].set_color(VS.LINE)
ax_scatter.spines['bottom'].set_color(VS.LINE)

# ─── PANEL 2 — CONVERSION EFFICIENCY BARS ─────────────────────
labels = [e["era"].replace('\n', ' ') for e in eras]
conv = [e["conv_eff"] for e in eras]
colors = [VS.DARK_BLUE if e["is_ai"] else VS.PINK for e in eras]

ax_bars.set_facecolor(VS.WHITE)
ax_bars.grid(True, axis='x', color=VS.LINE, linewidth=0.6, zorder=0)
ax_bars.set_axisbelow(True)

y_pos = np.arange(len(eras))
bars = ax_bars.barh(y_pos, conv, color=colors, edgecolor='none',
                     height=0.62, zorder=4)

# Value labels at end of bars
for i, (b, v, e) in enumerate(zip(bars, conv, eras)):
    text_color = VS.DARK_BLUE if e["is_ai"] else VS.BLACK
    weight = 'black' if e["is_ai"] else 'bold'
    ax_bars.text(v + 0.012, i, f'{v:.3f}',
                  va='center', ha='left', fontsize=11,
                  family='Lato', fontweight=weight, color=text_color, zorder=5)

ax_bars.set_yticks(y_pos)
ax_bars.set_yticklabels(labels, fontsize=11, family='Lato', color=VS.BLACK)
ax_bars.invert_yaxis()

ax_bars.set_xlim(0, max(conv) * 1.25)
ax_bars.set_xticks([0, 0.1, 0.2, 0.3])
ax_bars.set_xticklabels(['0', '0.1', '0.2', '0.3'],
                         fontsize=11, family='Lato', color=VS.INK_SOFT)
ax_bars.set_xlabel('Productivity gain per log-decade of info speed',
                    fontsize=11, family='Lato', color=VS.INK_SOFT, labelpad=8)
ax_bars.set_title('Conversion efficiency — info speed → productivity',
                   fontsize=15, family='Lato', fontweight='medium',
                   loc='left', pad=14, color=VS.BLACK)

for spine in ['top', 'right']:
    ax_bars.spines[spine].set_visible(False)
ax_bars.spines['left'].set_color(VS.LINE)
ax_bars.spines['bottom'].set_color(VS.LINE)

# Tick the AI label dark blue
y_labels = ax_bars.get_yticklabels()
for lbl, e in zip(y_labels, eras):
    if e["is_ai"]:
        lbl.set_color(VS.DARK_BLUE)
        lbl.set_fontweight('black')

# ─── HEADER STRIP — title, eyebrow, tagline ───────────────────
# Title block on top of the figure
fig.text(0.07, 0.94,
         'V A L U E S H I P S  ·  A I  V A L U E  R E S E A R C H  ·  M A Y  2 0 2 6',
         fontsize=10, family='Lato', fontweight='bold',
         color=VS.PINK)

fig.text(0.07, 0.89,
         'AI has the most information speed in human history.',
         fontsize=22, family='Lato', fontweight='medium', color=VS.BLACK)

fig.text(0.07, 0.85,
         'It delivers the lowest productivity since the agrarian era.',
         fontsize=22, family='Lato', fontweight='medium', color=VS.BLACK)

# Bottom-of-figure tagline + sources
fig.text(0.07, 0.06,
         'Gross AI looks like a revolution.   Net AI inside unrestructured organisations looks like a productivity tool.',
         fontsize=12, family='Lato', fontweight='black', color=VS.PINK)

fig.text(0.07, 0.025,
         'Sources: Productivity — Crafts/FRBSF (Industrial), Gordon (Electric, ICT), Acemoglu (LLM-era AI). Information-speed index: Valueships proxy, bits/sec/worker on log scale.',
         fontsize=8.5, family='Lato', color=VS.INK_SOFT, style='italic')

# Logo at bottom-right
arrow_x, arrow_y = 0.93, 0.025
fig_arrow = plt.Polygon([
    [arrow_x, arrow_y + 0.025],
    [arrow_x - 0.008, arrow_y + 0.005],
    [arrow_x, arrow_y + 0.013],
    [arrow_x + 0.008, arrow_y + 0.005],
], closed=True, facecolor=VS.PINK, edgecolor='none',
   transform=fig.transFigure, figure=fig)
fig.patches.append(fig_arrow)
fig.text(0.945, 0.025, 'Valueships',
         fontsize=11, family='Lato', fontweight='bold', color=VS.BLACK,
         va='center')

# Save
out = "/sessions/busy-tender-heisenberg/mnt/artefakty marketingowe - desk research/speed-normalized-productivity-chart.png"
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor=VS.WHITE, pad_inches=0.15)
plt.close()
print(f"Saved: {out}")

# Also save a square (1200x1200) version for LinkedIn — simpler, scatter only
fig2, ax2 = plt.subplots(figsize=(12, 12), dpi=120)
fig2.patch.set_facecolor(VS.WHITE)
ax2.set_facecolor(VS.WHITE)

# Reserve some chrome space
ax2.set_position([0.10, 0.20, 0.85, 0.58])

# Key visual corners (overlay axes)
ax_kv_a = fig2.add_axes([0, 0.78, 0.25, 0.22], zorder=0)
ax_kv_a.set_xlim(0, 100); ax_kv_a.set_ylim(0, 100); ax_kv_a.set_aspect('equal'); ax_kv_a.axis('off')
draw_key_visual_corner(ax_kv_a, corner='topleft', color=VS.PINK, scale=0.75, alpha_start=0.7, alpha_end=0.2)

ax_kv_b = fig2.add_axes([0.76, 0, 0.24, 0.22], zorder=0)
ax_kv_b.set_xlim(0, 100); ax_kv_b.set_ylim(0, 100); ax_kv_b.set_aspect('equal'); ax_kv_b.axis('off')
draw_key_visual_corner(ax_kv_b, corner='bottomright', color=VS.PINK, scale=0.75, alpha_start=0.7, alpha_end=0.2)

# Header
fig2.text(0.07, 0.93, 'V A L U E S H I P S  ·  A I  V A L U E  R E S E A R C H  ·  M A Y  2 0 2 6',
          fontsize=11, family='Lato', fontweight='bold', color=VS.PINK)
fig2.text(0.07, 0.88, 'More information speed should mean',
          fontsize=22, family='Lato', fontweight='medium', color=VS.BLACK)
fig2.text(0.07, 0.84, 'more productivity. AI breaks the pattern.',
          fontsize=22, family='Lato', fontweight='medium', color=VS.BLACK)

# Plot
ax2.grid(True, axis='y', color=VS.LINE, linewidth=0.6, zorder=0)
ax2.set_axisbelow(True)

# Trend line
ax2.plot(x_trend, y_trend, '--', color=VS.PINK_40, linewidth=1.5,
         alpha=0.8, zorder=2)

# Points
for e in eras:
    size = 480 if e["is_ai"] else 360
    ax2.scatter(e["log_info"], e["prod_pct"],
                s=size, c=e["color"], edgecolor=VS.WHITE,
                linewidth=3, zorder=5)
    text_color = VS.DARK_BLUE if e["is_ai"] else VS.BLACK
    weight = 'black' if e["is_ai"] else 'bold'
    label = e["era"].replace('\n', ' ')
    # Always place label above-right, except where it would clip
    offsets = {
        "Agrarian":               (0.35, 0.20),
        "First industrial":       (0.35, 0.20),
        "Electric / 2nd industrial": (-0.40, 0.20),
        "ICT baseline":           (0.30, -0.25),
        "ICT revival":            (-0.30, 0.20),
        "LLM-era AI":             (-0.40, 0.30),
    }
    ha_map = {"Electric / 2nd industrial": "right", "ICT revival": "right", "LLM-era AI": "right"}
    va_map = {"ICT baseline": "top"}
    dx, dy = offsets[label]
    ax2.annotate(
        f"{label}\n{e['prod_pct']:.2f}%/yr",
        xy=(e["log_info"], e["prod_pct"]),
        xytext=(e["log_info"] + dx, e["prod_pct"] + dy),
        ha=ha_map.get(label, "left"),
        va=va_map.get(label, "bottom"),
        fontsize=12, family='Lato',
        fontweight=weight, color=text_color, zorder=6,
    )

# Gap arrow for AI
ax2.annotate(
    '',
    xy=(ai_e["log_info"], ai_e["prod_pct"]),
    xytext=(ai_e["log_info"], ai_expected_y),
    arrowprops=dict(arrowstyle='->', color=VS.PINK, lw=2.5, alpha=0.9),
    zorder=4,
)
ax2.text(ai_e["log_info"] - 0.20, (ai_expected_y + ai_e["prod_pct"]) / 2 + 0.05,
         f'  Gap to trend:\n  ~2 pp/yr',
         ha='right', va='center', fontsize=11, family='Lato',
         color=VS.PINK, style='italic', fontweight='bold')

ax2.set_xlim(-0.8, 12.5)
ax2.set_ylim(-0.4, 3.5)
ax2.set_xticks([0, 2, 5, 8, 9, 11])
ax2.set_xticklabels(['1×\nagrarian', '100×\nprint+mail', '100K×\nradio+TV',
                      '100M×\ninternet', '1B×\nbroadband', '100B×\nAI + Gbps'],
                     fontsize=10.5, family='Lato', color=VS.INK_SOFT)
ax2.set_yticks([0, 1, 2, 3])
ax2.set_yticklabels(['0%', '1%', '2%', '3%'],
                     fontsize=11, family='Lato', color=VS.INK_SOFT)
ax2.set_xlabel('Information speed (bits/sec/worker, log scale)',
                fontsize=12, family='Lato', color=VS.BLACK, labelpad=10)
ax2.set_ylabel('Annual productivity gain',
                fontsize=12, family='Lato', color=VS.BLACK, labelpad=10)

for spine in ['top', 'right']:
    ax2.spines[spine].set_visible(False)
ax2.spines['left'].set_color(VS.LINE)
ax2.spines['bottom'].set_color(VS.LINE)

# Tagline
fig2.text(0.5, 0.13,
          'Gross AI looks like a revolution.',
          fontsize=15, family='Lato', fontweight='black', color=VS.PINK,
          ha='center')
fig2.text(0.5, 0.10,
          'Net AI inside unrestructured organisations',
          fontsize=13, family='Lato', color=VS.BLACK, ha='center')
fig2.text(0.5, 0.075,
          'looks like a productivity tool.',
          fontsize=13, family='Lato', color=VS.BLACK, ha='center')

# Logo
arrow2 = plt.Polygon([
    [0.075, 0.045],
    [0.067, 0.025],
    [0.075, 0.033],
    [0.083, 0.025],
], closed=True, facecolor=VS.PINK, edgecolor='none',
   transform=fig2.transFigure, figure=fig2)
fig2.patches.append(arrow2)
fig2.text(0.10, 0.034, 'Valueships',
          fontsize=13, family='Lato', fontweight='bold', color=VS.BLACK,
          va='center')

out2 = "/sessions/busy-tender-heisenberg/mnt/artefakty marketingowe - desk research/speed-normalized-productivity-linkedin.png"
plt.savefig(out2, dpi=120, bbox_inches='tight', facecolor=VS.WHITE, pad_inches=0)
plt.close()
print(f"Saved: {out2}")
