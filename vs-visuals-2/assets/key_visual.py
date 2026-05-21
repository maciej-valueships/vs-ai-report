"""
Valueships key visual — reusable matplotlib renderer.

The "key visual" is the flowing-line graphic that gives every Valueships asset
its recognizable signature: concentric organic shapes drawn as thin pink lines,
cropped so part of the pattern falls off the canvas, anchored in corners.

Usage:
    import matplotlib.pyplot as plt
    from key_visual import draw_key_visual_corner

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.set_aspect('equal'); ax.axis('off')

    # One corner — minimal
    draw_key_visual_corner(ax, corner='topleft')

    # Two corners — most common pattern for social visuals
    draw_key_visual_corner(ax, corner='topleft')
    draw_key_visual_corner(ax, corner='bottomright')

    # ... your content ...

The function assumes axes use a coordinate space where (0,0) is bottom-left
and (100,100) is top-right. If your space is different, pass scale= to adjust.
"""

import numpy as np


PINK = '#FF005E'
WHITE = '#FFFFFF'


def draw_key_visual_corner(
    ax,
    corner='topleft',
    color=PINK,
    n_lines=22,
    scale=1.0,
    alpha_start=0.85,
    alpha_end=0.30,
    line_width=0.7,
    z_order=1,
):
    """Draw the Valueships flowing-line key visual anchored to one corner.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to draw on. Expected to span (0,0) to (100,100). Use ``scale``
        to adapt to other coordinate spaces.
    corner : str
        One of 'topleft', 'topright', 'bottomleft', 'bottomright'.
    color : str
        Stroke color. Default brand pink. Use white on pink/dark backgrounds.
    n_lines : int
        Number of concentric lines. 18–26 looks right; fewer feels sparse,
        more becomes cluttered.
    scale : float
        Multiplier for the size of the key visual. 1.0 ≈ 50% of canvas occupied
        by the lines. Use 0.6 for a quieter version, 1.4 for a hero cover.
    alpha_start : float
        Opacity of the innermost (smallest) line. 0.0–1.0.
    alpha_end : float
        Opacity of the outermost (largest) line. 0.0–1.0.
    line_width : float
        Stroke width in points.
    z_order : int
        Matplotlib z-order. Keep low (1 or below) so the key visual sits
        behind content.
    """

    # Anchor each corner slightly outside the canvas so the pattern feels
    # like it's entering from off-screen, matching the brand book's "trimmed"
    # quality.
    anchors = {
        'topleft':     (-4, 104),
        'topright':    (104, 104),
        'bottomleft':  (-4, -4),
        'bottomright': (104, -4),
    }
    if corner not in anchors:
        raise ValueError(f"corner must be one of {list(anchors.keys())}")
    cx, cy = anchors[corner]

    # Each corner uses a different arc segment so the lines flow into the
    # canvas from the right direction.
    theta_ranges = {
        'topleft':     (-np.pi/2 - 0.15,  0.15),
        'topright':    (np.pi + 0.15,     1.5*np.pi - 0.15),
        'bottomleft':  (0 - 0.15,         np.pi/2 + 0.15),
        'bottomright': (np.pi/2 - 0.15,   np.pi + 0.15),
    }
    theta = np.linspace(*theta_ranges[corner], 140)

    for i in range(n_lines):
        t = i / (n_lines - 1) if n_lines > 1 else 0
        alpha = alpha_start - (alpha_start - alpha_end) * t

        # Radius grows linearly outward from the anchor.
        r = (4 + i * 1.6) * scale

        # Asymmetric wobble — gives the lines their organic, non-circular feel.
        # The phase shifts by line index, so adjacent lines don't sit parallel.
        wobble = (1
                  + 0.12 * np.sin(theta * 2.5 + i * 0.5)
                  + 0.06 * np.cos(theta * 4   - i * 0.3))

        x = cx + r * wobble * np.cos(theta)
        y = cy + r * wobble * np.sin(theta)

        ax.plot(x, y, color=color, lw=line_width, alpha=alpha,
                solid_capstyle='round', zorder=z_order)


def draw_key_visual_full_bleed(ax, color=PINK, **kwargs):
    """Cover the full canvas with the key visual.

    Useful for hero covers, deck title slides, or report front pages.
    Combines two diagonal corners at full scale.
    """
    draw_key_visual_corner(ax, corner='topleft', color=color, scale=1.4, **kwargs)
    draw_key_visual_corner(ax, corner='bottomright', color=color, scale=1.4, **kwargs)


# ─── Self-test ───
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Example 1: single corner
    ax = axes[0]
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_facecolor(WHITE)
    draw_key_visual_corner(ax, corner='topleft')
    ax.text(50, 50, 'Single corner\n(quiet)', ha='center', va='center',
            fontsize=20, fontfamily='Lato', fontweight='medium', color='#080808')

    # Example 2: two diagonal corners (most common for social)
    ax = axes[1]
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_facecolor(WHITE)
    draw_key_visual_corner(ax, corner='topleft')
    draw_key_visual_corner(ax, corner='bottomright')
    ax.text(50, 50, 'Two corners\n(social default)', ha='center', va='center',
            fontsize=20, fontfamily='Lato', fontweight='medium', color='#080808')

    plt.tight_layout()
    plt.savefig('key_visual_examples.png', dpi=150, bbox_inches='tight',
                facecolor=WHITE)
    print('Saved key_visual_examples.png')
