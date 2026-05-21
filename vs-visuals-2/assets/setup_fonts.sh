#!/usr/bin/env bash
#
# Install Valueships brand fonts (Lato + Roboto) on Ubuntu/Debian systems.
# Used by Claude's code execution environment when generating brand assets.
#
# Run once at the start of an asset-generation script:
#   bash setup_fonts.sh
#
# Or inline from Python:
#   import subprocess
#   subprocess.run(['bash', 'assets/setup_fonts.sh'], check=False)

set -e

echo "Installing Valueships brand fonts..."

if command -v apt-get >/dev/null 2>&1; then
    apt-get install -y fonts-lato fonts-roboto >/dev/null 2>&1
    fc-cache -f >/dev/null 2>&1
    echo "✓ Lato + Roboto installed via apt"
elif command -v brew >/dev/null 2>&1; then
    # macOS
    brew install --cask font-lato font-roboto 2>/dev/null || true
    echo "✓ Lato + Roboto installed via Homebrew"
else
    echo "⚠ Could not detect package manager."
    echo "  Install Lato + Roboto manually from https://fonts.google.com"
    exit 1
fi

# Verify
if fc-list 2>/dev/null | grep -qi "lato"; then
    echo "✓ Lato available"
else
    echo "⚠ Lato not detected after install"
fi

if fc-list 2>/dev/null | grep -qi "roboto"; then
    echo "✓ Roboto available"
else
    echo "⚠ Roboto not detected after install"
fi

# Clear matplotlib's cached font list so it picks up the new fonts on next run.
if [ -d "$HOME/.cache/matplotlib" ]; then
    rm -rf "$HOME/.cache/matplotlib"
    echo "✓ Matplotlib font cache cleared"
fi

echo "Done."
