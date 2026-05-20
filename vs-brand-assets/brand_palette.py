"""
Valueships brand palette — Python constants.

Import this module in any matplotlib / Pillow / Python visualization script that
produces a Valueships-branded asset.

Usage:
    from brand_palette import VS

    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, 'Hello', color=VS.PINK)
    ax.set_facecolor(VS.WHITE)

The VS namespace mirrors the brand book exactly. See references/colors.md for
the full color system documentation and the 9:1 pink-to-blue rule.
"""


class VS:
    # ─── PRIMARY (dominant, ~90% of color use) ───
    PINK         = '#FF005E'   # brand pink, the hero
    PINK_80      = '#FF337E'   # softer pink, hover states
    PINK_60      = '#FF669D'   # secondary accents
    PINK_40      = '#FF99BD'   # decorative fills
    PINK_20      = '#FFD1E0'   # badge backgrounds, soft callouts
    PINK_5       = '#FFF0F5'   # near-white wash, soft sections
    PINK_LIGHT   = PINK_60     # alias

    # ─── SECONDARY (accent only, ~10% of color use) ───
    DARK_BLUE    = '#0F155B'   # brand secondary, the single accent
    DARK_BLUE_80 = '#3F4480'   # softer accent
    DARK_BLUE_40 = '#9BA0BD'   # faded accent
    DARK_BLUE_20 = '#DEDFF5'   # very soft blue tint

    # ─── NEUTRALS ───
    BLACK        = '#080808'   # body text
    INK_SOFT     = '#5A5A5C'   # captions, secondary text
    GREY_MID     = '#9A9A9D'   # disabled, less-important metadata
    LINE         = '#E8E8EC'   # dividers, card borders
    OFF_WHITE    = '#F7F7F8'   # subtle backgrounds
    WHITE        = '#FFFFFF'   # default background

    # ─── SEMANTIC ALIASES ───
    # Use these when you want to express intent rather than color
    PRIMARY      = PINK
    SECONDARY    = DARK_BLUE
    TEXT         = BLACK
    TEXT_MUTED   = INK_SOFT
    BG           = WHITE
    BORDER       = LINE


# ─── Pink shade ramp (useful for gradients, ordinal scales) ───
PINK_RAMP = [
    '#FF005E',  # 100
    '#FF337E',  # 80
    '#FF669D',  # 60
    '#FF99BD',  # 40
    '#FFD1E0',  # 20
    '#FFF0F5',  # 5
]

# ─── Chart-safe palette (for multi-series data viz) ───
# Use pink as primary, dark blue as secondary, then neutrals.
# Avoid going beyond 4 series — if you need more, group the data instead.
CHART_PALETTE = [
    VS.PINK,        # series 1
    VS.DARK_BLUE,   # series 2
    VS.INK_SOFT,    # series 3
    VS.GREY_MID,    # series 4
]


# ─── Matplotlib rcParams helper ───
def apply_valueships_style():
    """Apply Valueships defaults to matplotlib's global style.

    Call once at the top of a script to set fonts, colors, and grid style
    consistent with the brand. Individual elements can still be overridden.
    """
    import matplotlib as mpl
    mpl.rcParams.update({
        'font.family': 'Lato',
        'font.size': 12,
        'axes.titlesize': 16,
        'axes.titleweight': 'medium',
        'axes.labelsize': 12,
        'axes.labelcolor': VS.BLACK,
        'axes.edgecolor': VS.LINE,
        'axes.linewidth': 0.8,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.facecolor': VS.WHITE,
        'figure.facecolor': VS.WHITE,
        'xtick.color': VS.INK_SOFT,
        'ytick.color': VS.INK_SOFT,
        'grid.color': VS.LINE,
        'grid.linewidth': 0.6,
        'lines.linewidth': 2,
        'lines.color': VS.PINK,
        'axes.prop_cycle': mpl.cycler(color=CHART_PALETTE),
    })


if __name__ == '__main__':
    # Quick verification: print the palette as a swatch grid
    import matplotlib.pyplot as plt
    apply_valueships_style()

    swatches = [
        ('PINK', VS.PINK), ('PINK_80', VS.PINK_80), ('PINK_60', VS.PINK_60),
        ('PINK_40', VS.PINK_40), ('PINK_20', VS.PINK_20), ('PINK_5', VS.PINK_5),
        ('DARK_BLUE', VS.DARK_BLUE), ('DARK_BLUE_40', VS.DARK_BLUE_40),
        ('BLACK', VS.BLACK), ('INK_SOFT', VS.INK_SOFT),
        ('LINE', VS.LINE), ('WHITE', VS.WHITE),
    ]
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (name, hex_) in enumerate(swatches):
        col, row = i % 4, i // 4
        ax.add_patch(plt.Rectangle((col, -row), 0.9, 0.9, facecolor=hex_, edgecolor=VS.LINE))
        text_color = VS.WHITE if hex_ in (VS.PINK, VS.PINK_80, VS.DARK_BLUE, VS.BLACK) else VS.BLACK
        ax.text(col + 0.45, -row + 0.55, name, ha='center', va='center', fontsize=9,
                color=text_color, fontweight='bold')
        ax.text(col + 0.45, -row + 0.30, hex_, ha='center', va='center', fontsize=8,
                color=text_color)
    ax.set_xlim(-0.1, 4); ax.set_ylim(-3, 1)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig('palette_swatches.png', dpi=150, bbox_inches='tight')
    print('Saved palette_swatches.png')
