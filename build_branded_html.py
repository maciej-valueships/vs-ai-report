#!/usr/bin/env python3
"""Build Valueships-branded HTML from demystifying-the-value-of-ai.md.

SOURCE OF TRUTH: demystifying-the-value-of-ai.md only.
Do not edit HTML by hand — run: python3 build_branded_html.py

Outputs:
  - demystifying-the-value-of-ai.html      — local preview
  - demystifying-ai-shareable.html         — upload this file to CMS
"""

from __future__ import annotations

import html as html_lib
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "demystifying-the-value-of-ai.md"
OUT_PATH = ROOT / "demystifying-the-value-of-ai.html"
CMS_OUT_PATH = ROOT / "demystifying-ai-shareable.html"
INDEX_PATH = ROOT / "index.html"
ASSETS_DIR = ROOT / "assets"
REFERENCES_TXT_PATH = ASSETS_DIR / "demystifying-ai-references.txt"
CITE_MARKER_RE = re.compile(r"\[@([0-9,@\s]+)\]")
LOGO_COVER = "assets/vs-logo-footer.png"
HERO_IMAGE = "assets/hero-factory.png"
VPQ_CHART_JS = ASSETS_DIR / "vpq-bubble-chart.js"
CAPEX_CHART_JS = ASSETS_DIR / "capex-productivity-chart.js"
AVI_SECTOR_CHART_JS = ASSETS_DIR / "avi-sector-chart.js"
SPEED_CHART_JS = ASSETS_DIR / "productivity-speed-chart.js"
SOCIAL_CARDS_HTML = ROOT / "vs-social-cards.html"
CHART_JS_CDN = (
    '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.9/dist/chart.umd.min.js" '
    'crossorigin="anonymous"></script>'
)

# Contact CTA — Valueships lead form (https://www.valueships.com/contact)
CONTACT_CTA_URL = "https://www.valueships.com/contact"

KEYVIS_COVER = """<svg class="vs-keyvis-cover" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g fill="none" stroke="#FFFFFF" stroke-width="1.4" opacity="0.65">
    <path d="M -30 -30 Q 90 150, 240 -30"/><path d="M -30 0 Q 105 180,270 -30"/>
    <path d="M -30 30 Q 120 210,300 -30"/><path d="M -30 60 Q 135 240,330 0"/>
    <path d="M -30 90 Q 150 270,360 30"/><path d="M -30 120 Q 165 300,390 60"/>
    <path d="M -30 150 Q 180 330,420 90"/><path d="M -30 180 Q 195 360,450 120"/>
  </g>
  <g fill="none" stroke="#FFFFFF" stroke-width="1.4" opacity="0.65" transform="rotate(180 300 300)">
    <path d="M -30 -30 Q 90 150, 240 -30"/><path d="M -30 0 Q 105 180,270 -30"/>
    <path d="M -30 30 Q 120 210,300 -30"/><path d="M -30 60 Q 135 240,330 0"/>
    <path d="M -30 90 Q 150 270,360 30"/><path d="M -30 120 Q 165 300,390 60"/>
    <path d="M -30 150 Q 180 330,420 90"/><path d="M -30 180 Q 195 360,450 120"/>
  </g>
</svg>"""

BODY_KV_TL = """<svg class="vs-keyvis vs-keyvis--tl" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g fill="none" stroke="#FF005E" stroke-width="0.9" opacity="0.75">
    <path d="M -10 -10 Q 30 50, 80 -10"/><path d="M -10 0 Q 35 60, 90 -10"/>
    <path d="M -10 10 Q 40 70, 100 -10"/><path d="M -10 20 Q 45 80, 110 0"/>
    <path d="M -10 30 Q 50 90, 120 10"/><path d="M -10 40 Q 55 100,130 20"/>
    <path d="M -10 50 Q 60 110,140 30"/><path d="M -10 60 Q 65 120,150 40"/>
    <path d="M -10 70 Q 70 130,160 50"/><path d="M -10 80 Q 75 140,170 60"/>
  </g>
</svg>"""

BODY_KV_BR = """<svg class="vs-keyvis vs-keyvis--br" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g fill="none" stroke="#FF005E" stroke-width="0.9" opacity="0.75">
    <path d="M -10 -10 Q 30 50, 80 -10"/><path d="M -10 0 Q 35 60, 90 -10"/>
    <path d="M -10 10 Q 40 70, 100 -10"/><path d="M -10 20 Q 45 80, 110 0"/>
    <path d="M -10 30 Q 50 90, 120 10"/><path d="M -10 40 Q 55 100,130 20"/>
    <path d="M -10 50 Q 60 110,140 30"/><path d="M -10 60 Q 65 120,150 40"/>
    <path d="M -10 70 Q 70 130,160 50"/><path d="M -10 80 Q 75 140,170 60"/>
  </g>
</svg>"""

EARLY_SCROLL_GUARD_SCRIPT = """(function () {
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  var hash = location.hash;
  if (!hash || hash === '#') {
    window.scrollTo(0, 0);
  } else {
    /* Block the browser's default hash jump; main script scrolls after layout. */
    window.scrollTo(0, 0);
  }
})();"""

CHROME_LAYOUT_SCRIPT = """(function () {
  var chrome = document.getElementById('vs-chrome');
  var nav = document.querySelector('.vs-topnav');
  var cover = document.getElementById('cover');
  var sectionNav = document.getElementById('vs-section-nav');
  var spacer = document.getElementById('vs-chrome-spacer');
  var mql = window.matchMedia('(max-width: 960px)');
  if (!chrome || !nav || !cover) return;

  var coverVisible = true;

  function mobileNav() {
    return mql.matches;
  }

  function updateChromeHeight() {
    var mobile = mobileNav();
    document.body.classList.toggle('vs-nav-mobile', mobile);
    document.body.classList.toggle('vs-nav-desktop', !mobile);
    var h = mobile ? chrome.offsetHeight : 0;
    document.documentElement.style.setProperty('--vs-chrome-h', h + 'px');
    if (spacer) {
      var pad =
        mobile && document.body.classList.contains('has-section-nav-bar');
      spacer.style.height = pad ? h + 'px' : '0px';
    }
    window.dispatchEvent(new CustomEvent('vs-layout-chrome'));
  }

  function setCoverMode(onCover) {
    coverVisible = onCover;
    nav.classList.toggle('vs-topnav--cover', onCover);
    if (sectionNav) {
      var showBar = mobileNav() && !onCover;
      sectionNav.hidden = !showBar;
      document.body.classList.toggle('has-section-nav-bar', showBar);
    } else {
      document.body.classList.toggle('has-section-nav-bar', mobileNav() && !onCover);
    }
    updateChromeHeight();
  }

  var obs = new IntersectionObserver(
    function (entries) {
      setCoverMode(entries[0].isIntersecting);
    },
    { threshold: 0 }
  );
  obs.observe(cover);

  if (mql.addEventListener) {
    mql.addEventListener('change', function () {
      setCoverMode(coverVisible);
    });
  } else if (mql.addListener) {
    mql.addListener(function () {
      setCoverMode(coverVisible);
    });
  }

  window.addEventListener('resize', updateChromeHeight, { passive: true });
  if (window.ResizeObserver) {
    new ResizeObserver(updateChromeHeight).observe(chrome);
  }
  updateChromeHeight();
})();"""

NAV_COVER_SCRIPT = CHROME_LAYOUT_SCRIPT

TOC_SCROLL_SPY_SCRIPT = """(function () {
  const toc = document.getElementById('vs-toc');
  const article = document.getElementById('vs-report');
  const sectionNav = document.getElementById('vs-section-nav');
  const sectionNavSub = document.getElementById('vs-section-nav-sub');
  if (!toc || !article) return;

  function stickyOffset() {
    var root = document.documentElement;
    var h = parseFloat(getComputedStyle(root).getPropertyValue('--vs-chrome-h')) || 60;
    return h + 12;
  }

  const CITE_OFFSET = 88;
  const REFS_TOC_ID = 'avi-references';
  const headings = article.querySelectorAll(
    'h2.vs-section-title[id], h3.vs-subsection[id]'
  );
  const sections = [];
  headings.forEach(function (el) {
    const link = toc.querySelector('a[href="#' + el.id + '"]');
    if (link) sections.push({ id: el.id, el: el, link: link });
  });
  if (!sections.length) return;

  const allLinks = toc.querySelectorAll('a[href^="#"]');
  var lastActiveId = null;
  var suppressSpyUntil = 0;
  var pageReady = false;
  var anchoredId = null;

  function readHashId() {
    var raw = (location.hash || '').slice(1);
    if (!raw) return null;
    try {
      return decodeURIComponent(raw);
    } catch (e) {
      return raw;
    }
  }

  function scrollTocToLink(link) {
    if (!link) return;
    var pad = 10;
    var linkTop = link.offsetTop;
    var linkBottom = linkTop + link.offsetHeight;
    var viewTop = toc.scrollTop;
    var viewBottom = viewTop + toc.clientHeight;
    if (linkTop < viewTop + pad) {
      toc.scrollTop = linkTop - pad;
    } else if (linkBottom > viewBottom - pad) {
      toc.scrollTop = linkBottom - toc.clientHeight + pad;
    }
  }

  function chapterIdForHeadingId(id) {
    var el = document.getElementById(id);
    if (!el) return id;
    if (el.classList.contains('vs-section-title')) return id;
    var chapterId = sections.length ? sections[0].id : id;
    var found = false;
    headings.forEach(function (h) {
      if (h.id === id) {
        found = true;
        return;
      }
      if (!found && h.classList.contains('vs-section-title')) {
        chapterId = h.id;
      }
    });
    return chapterId;
  }

  function subsectionLabel(id) {
    var el = document.getElementById(id);
    if (!el || el.classList.contains('vs-section-title')) return '';
    return el.textContent.trim().replace(/\\s+/g, ' ');
  }

  function scrollPillIntoView(pill) {
    if (!pill || !pill.parentElement) return;
    var track = pill.parentElement;
    var pad = 12;
    var left = pill.offsetLeft - pad;
    var right = pill.offsetLeft + pill.offsetWidth + pad;
    if (left < track.scrollLeft) {
      track.scrollLeft = left;
    } else if (right > track.scrollLeft + track.clientWidth) {
      track.scrollLeft = right - track.clientWidth;
    }
  }

  function setSectionNav(activeId) {
    if (!sectionNav) return;
    var chapterId = chapterIdForHeadingId(activeId);
    sectionNav.querySelectorAll('.vs-section-nav__pill').forEach(function (pill) {
      var on = pill.getAttribute('href') === '#' + chapterId;
      pill.classList.toggle('is-active', on);
      if (on) pill.setAttribute('aria-current', 'true');
      else pill.removeAttribute('aria-current');
    });
    var activePill = sectionNav.querySelector('.vs-section-nav__pill.is-active');
    scrollPillIntoView(activePill);
    if (sectionNavSub) {
      var sub =
        activeId && activeId !== chapterId ? subsectionLabel(activeId) : '';
      sectionNavSub.textContent = sub;
      sectionNavSub.hidden = !sub;
    }
  }

  function setActive(id, syncToc) {
    if (id === lastActiveId) return;
    lastActiveId = id;
    allLinks.forEach(function (a) {
      var on = a.getAttribute('href') === '#' + id;
      a.classList.toggle('is-active', on);
      if (on) a.setAttribute('aria-current', 'location');
      else a.removeAttribute('aria-current');
    });
    toc.querySelectorAll('.vs-toc__chapter').forEach(function (li) {
      var subOn = li.querySelector('.vs-toc__subs a.is-active');
      var chOn = li.querySelector(':scope > a.is-active');
      li.classList.toggle('has-active', !!(subOn || chOn));
    });
    setSectionNav(id);
    if (syncToc !== false) scrollTocToLink(toc.querySelector('a.is-active'));
  }

  function tocIdForTarget(id) {
    if (/^ref-\\d+$/.test(id)) return REFS_TOC_ID;
    if (toc.querySelector('a[href="#' + id + '"]')) return id;
    return null;
  }

  function scrollToY(y) {
    window.scrollTo({ top: Math.max(0, y), behavior: 'auto' });
  }

  function scrollToEl(el, offset) {
    if (!el) return;
    var y = el.getBoundingClientRect().top + window.scrollY - offset;
    scrollToY(y);
  }

  function scrollToSection(id, updateHash) {
    var target = document.getElementById(id);
    if (!target) return;
    suppressSpyUntil = Date.now() + 900;
    scrollToEl(target, stickyOffset());
    var tocId = tocIdForTarget(id) || id;
    setActive(tocId, true);
    if (updateHash !== false) {
      anchoredId = id;
      if (history.replaceState) history.replaceState(null, '', '#' + id);
      else location.hash = id;
    }
  }

  function scrollToRef(id) {
    var target = document.getElementById(id);
    if (!target) return;
    suppressSpyUntil = Date.now() + 900;
    setActive(REFS_TOC_ID, false);
    scrollToEl(target, CITE_OFFSET);
    anchoredId = id;
    if (history.replaceState) history.replaceState(null, '', '#' + id);
    else location.hash = id;
  }

  function maybeReleaseHash() {
    if (Date.now() < suppressSpyUntil || !anchoredId) return;
    var el = document.getElementById(anchoredId);
    if (!el) {
      anchoredId = null;
      return;
    }
    var rect = el.getBoundingClientRect();
    if (rect.bottom < 48 || rect.top > window.innerHeight * 0.4) {
      anchoredId = null;
      if (location.hash && history.replaceState) {
        history.replaceState(null, '', location.pathname + location.search);
      }
    }
  }

  function computeActive() {
    if (Date.now() < suppressSpyUntil) return;
    if (!pageReady && !location.hash) return;
    var active = sections[0].id;
    var bestTop = -Infinity;
    sections.forEach(function (s) {
      var top = s.el.getBoundingClientRect().top;
      if (top <= stickyOffset() && top > bestTop) active = s.id;
    });
    if (pageReady) {
      var nearBottom =
        window.innerHeight + window.scrollY >=
        document.documentElement.scrollHeight - 12;
      if (nearBottom) active = sections[sections.length - 1].id;
    }
    setActive(active, false);
  }

  function handleInitialRoute() {
    pageReady = true;
    var hash = readHashId();
    if (!hash) {
      window.scrollTo(0, 0);
      anchoredId = null;
      computeActive();
      return;
    }
    var target = document.getElementById(hash);
    if (!target) {
      window.scrollTo(0, 0);
      anchoredId = null;
      if (history.replaceState) {
        history.replaceState(null, '', location.pathname + location.search);
      }
      computeActive();
      return;
    }
    anchoredId = hash;
    suppressSpyUntil = Date.now() + 1500;
    if (/^ref-\\d+$/.test(hash)) scrollToRef(hash);
    else scrollToSection(hash, false);
  }

  var ticking = false;
  window.addEventListener(
    'scroll',
    function () {
      maybeReleaseHash();
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        computeActive();
        ticking = false;
      });
    },
    { passive: true }
  );
  window.addEventListener('resize', computeActive, { passive: true });

  article.addEventListener('click', function (e) {
    var link = e.target.closest('a.vs-cite-link');
    if (!link || !article.contains(link)) return;
    var href = link.getAttribute('href');
    if (!href || href.charAt(0) !== '#') return;
    var id = href.slice(1);
    if (!/^ref-\\d+$/.test(id)) return;
    if (e.defaultPrevented || e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    scrollToRef(id);
  });

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a || e.defaultPrevented || e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.classList.contains('vs-cite-link')) return;
    var id = (a.getAttribute('href') || '').slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    if (id === 'cover') {
      suppressSpyUntil = Date.now() + 900;
      scrollToY(0);
      anchoredId = null;
      if (history.replaceState) {
        history.replaceState(null, '', location.pathname + location.search);
      }
      return;
    }
    var keepHash = !a.classList.contains('vs-jump-no-hash');
    scrollToSection(id, keepHash);
  });

  window.addEventListener('hashchange', function () {
    var id = readHashId();
    if (!id) {
      anchoredId = null;
      return;
    }
    var tocId = tocIdForTarget(id);
    if (tocId) {
      suppressSpyUntil = Date.now() + 600;
      setActive(tocId, false);
    }
    if (document.getElementById(id)) anchoredId = id;
  });

  window.addEventListener('vs-layout-chrome', function () {
    computeActive();
  });

  if (document.readyState === 'complete') {
    handleInitialRoute();
  } else {
    window.addEventListener('load', handleInitialRoute, { once: true });
  }
})();"""

READING_NAV_SCRIPT = """(function () {
  var article = document.getElementById('vs-report');
  var bar = document.getElementById('vs-read-nav');
  var backBtn = document.getElementById('vs-read-nav-back');
  var currentEl = document.getElementById('vs-read-nav-current');
  var trailEl = document.getElementById('vs-read-nav-trail');
  if (!article || !bar || !backBtn) return;

  var stack = [];
  var suppressPush = false;
  var SECTION_OFFSET = 96;

  function nearestSectionId() {
    var headings = article.querySelectorAll(
      'h2.vs-section-title[id], h3.vs-subsection[id]'
    );
    if (!headings.length) return null;
    var active = headings[0].id;
    var bestTop = -Infinity;
    headings.forEach(function (h) {
      var top = h.getBoundingClientRect().top;
      if (top <= SECTION_OFFSET && top > bestTop) {
        bestTop = top;
        active = h.id;
      }
    });
    return active;
  }

  function labelForId(id) {
    if (!id) return 'Report';
    if (/^ref-\\d+$/.test(id)) {
      return 'Reference ' + id.replace('ref-', '');
    }
    var h = document.getElementById(id);
    if (h && h.textContent) {
      return h.textContent.trim().replace(/\\s+/g, ' ').slice(0, 72);
    }
    var tocA = document.querySelector('#vs-toc a[href="#' + id + '"]');
    if (tocA) {
      return tocA.textContent.replace(/^[\\d.a-z]+\\s*/i, '').trim().slice(0, 72);
    }
    return id;
  }

  function currentViewLabel() {
    var hash = (location.hash || '').slice(1);
    if (hash && document.getElementById(hash)) {
      return labelForId(hash);
    }
    return labelForId(nearestSectionId());
  }

  function pushReturnPoint(link) {
    if (suppressPush) return;
    var href = link.getAttribute('href') || '';
    if (!href || href.charAt(0) !== '#') return;
    var targetId = href.slice(1);
    if (!targetId || targetId === 'cover') return;
    var citeSup = link.closest('sup.vs-cite');
    var citeId = citeSup && citeSup.id ? citeSup.id : null;
    var sectionId = nearestSectionId();
    stack.push({
      scrollY: window.scrollY,
      sectionId: sectionId,
      label: labelForId(sectionId),
      citeId: citeId,
      targetId: targetId,
    });
    updateBar();
  }

  function flashCite(citeId) {
    if (!citeId) return;
    var el = document.getElementById(citeId);
    if (!el) return;
    el.classList.add('vs-cite--flash');
    setTimeout(function () {
      el.classList.remove('vs-cite--flash');
    }, 2200);
  }

  function restorePoint(pt) {
    suppressPush = true;
    window.scrollTo({ top: Math.max(0, pt.scrollY), behavior: 'smooth' });
    setTimeout(function () {
      suppressPush = false;
      updateBar();
      flashCite(pt.citeId);
    }, 450);
  }

  function popBack() {
    var pt = stack.pop();
    if (!pt) {
      updateBar();
      return;
    }
    restorePoint(pt);
  }

  function updateBar() {
    var hasStack = stack.length > 0;
    bar.hidden = !hasStack;
    document.body.classList.toggle('has-read-nav', hasStack);
    window.dispatchEvent(new CustomEvent('vs-layout-chrome'));
    if (!hasStack) return;

    var top = stack[stack.length - 1];
    backBtn.textContent = '← Back to ' + top.label;
    backBtn.setAttribute('aria-label', 'Return to ' + top.label);
    currentEl.textContent = 'Viewing: ' + currentViewLabel();

    if (!trailEl) return;
    trailEl.innerHTML = '';
    var recent = stack.slice(-3).reverse();
    recent.forEach(function (pt, idx) {
      if (idx > 0) {
        var sep = document.createElement('span');
        sep.className = 'vs-read-nav__trail-sep';
        sep.textContent = '·';
        trailEl.appendChild(sep);
      }
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'vs-read-nav__trail-link';
      btn.textContent = pt.label;
      btn.addEventListener('click', function () {
        var i = stack.indexOf(pt);
        if (i === -1) return;
        var point = stack[i];
        stack.length = i;
        restorePoint(point);
      });
      trailEl.appendChild(btn);
    });
  }

  document.addEventListener(
    'click',
    function (e) {
      if (suppressPush || e.defaultPrevented || e.button !== 0) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      if (e.target.closest('#vs-read-nav')) return;
      var link = e.target.closest('#vs-report a[href^="#"]');
      if (!link || !article.contains(link)) return;
      if (link.classList.contains('vs-jump-no-hash')) return;
      pushReturnPoint(link);
    },
    true
  );

  backBtn.addEventListener('click', function () {
    popBack();
  });

  window.addEventListener('hashchange', function () {
    setTimeout(updateBar, 80);
  });
  window.addEventListener(
    'scroll',
    function () {
      if (!stack.length) return;
      if (window.vsReadNavScrollTick) return;
      window.vsReadNavScrollTick = true;
      requestAnimationFrame(function () {
        updateBar();
        window.vsReadNavScrollTick = false;
      });
    },
    { passive: true }
  );

  updateBar();
})();"""

READ_NAV_HTML = """
<nav class="vs-read-nav" id="vs-read-nav" aria-label="Reading trail" hidden>
  <div class="vs-read-nav__inner">
    <button type="button" class="vs-read-nav__back" id="vs-read-nav-back">← Back</button>
    <span class="vs-read-nav__current" id="vs-read-nav-current"></span>
    <div class="vs-read-nav__trail" id="vs-read-nav-trail"></div>
  </div>
</nav>
"""

SECTION_NAV_CSS = """
/* Horizontal section menu — ≤960px only (desktop uses sidebar TOC) */
.vs-section-nav {
  position: relative;
  z-index: 1;
  background: var(--vs-white);
  border-bottom: 1px solid var(--vs-line);
  box-shadow: 0 2px 10px rgba(8, 8, 8, 0.06);
}
.vs-section-nav[hidden] { display: none !important; }
.vs-section-nav__inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: var(--vs-section-nav-h);
}
.vs-section-nav__sub {
  flex: 0 1 220px;
  min-width: 0;
  font-size: 12px;
  font-weight: 600;
  color: var(--vs-ink-soft);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.vs-section-nav__sub[hidden] { display: none; }
.vs-section-nav__track {
  flex: 1;
  min-width: 0;
  display: flex;
  align-items: stretch;
  gap: 6px;
  overflow-x: auto;
  overflow-y: hidden;
  padding: 8px 0;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
  scrollbar-color: var(--vs-pink-40) transparent;
}
.vs-section-nav__track::-webkit-scrollbar { height: 4px; }
.vs-section-nav__track::-webkit-scrollbar-thumb {
  background: var(--vs-pink-40);
  border-radius: 4px;
}
.vs-section-nav__pill {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid var(--vs-line);
  background: var(--vs-white);
  font-family: var(--vs-font-display);
  font-size: 12px;
  font-weight: 600;
  line-height: 1.2;
  color: var(--vs-ink-soft);
  text-decoration: none !important;
  border-bottom: none !important;
  white-space: nowrap;
  transition: background 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}
.vs-section-nav__pill:hover {
  border-color: var(--vs-pink-60);
  color: var(--vs-blue);
  background: var(--vs-pink-5);
}
.vs-section-nav__pill.is-active {
  border-color: var(--vs-pink);
  background: var(--vs-pink);
  color: var(--vs-white);
}
.vs-section-nav__pill-num {
  font-weight: 900;
  font-variant-numeric: tabular-nums;
}
.vs-section-nav__pill.is-active .vs-section-nav__pill-num {
  color: var(--vs-white);
}
@media (max-width: 960px) {
  .vs-section-nav__inner { padding: 0 16px; }
  .vs-section-nav__sub {
    flex: 0 1 38%;
    max-width: 42%;
    font-size: 11px;
  }
}
@media (max-width: 520px) {
  .vs-section-nav__inner { padding: 0 10px; gap: 6px; }
  .vs-section-nav__sub { flex: 0 1 34%; max-width: 40%; font-size: 10px; }
  .vs-section-nav__pill-label { display: none; }
  .vs-section-nav__pill { padding: 6px 9px; }
}
"""

REF_URL_RE = re.compile(r"https?://[^\s<>\"']+")

MACRO_GRID_CSS = """
.vs-macro-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
  margin: 28px 0 32px;
}
@media (max-width: 720px) {
  .vs-macro-grid { grid-template-columns: 1fr; }
}
.vs-macro-card {
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 18px 20px;
  border: 1px solid var(--vs-line);
  border-radius: 8px;
  background: var(--vs-white);
  box-shadow: 0 2px 12px rgba(15, 21, 91, 0.06);
}
.vs-macro-card--wide { grid-column: 1 / -1; }
.vs-macro-card__icon { color: var(--vs-pink); margin: 0 0 10px; }
.vs-macro-card__icon svg { width: 28px; height: 28px; display: block; }
.vs-macro-card__source {
  font-family: var(--vs-font-display);
  font-weight: 700;
  font-size: 14px;
  color: var(--vs-blue);
  margin: 0 0 6px;
}
.vs-macro-card__scope, .vs-macro-card__signal {
  font-size: 14px;
  margin: 0 0 8px;
}
.vs-macro-card__implication {
  font-size: 13px;
  margin: auto 0 0;
  color: var(--vs-ink-soft);
  border-top: 1px solid var(--vs-line);
  padding-top: 10px;
}
.vs-pull {
  font-size: 18px;
  border-left-width: 5px;
}
.vs-macro-card__source a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 2px;
}
.vs-macro-card__source a:hover { color: var(--vs-pink); }
.vs-ladder {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 24px 0 28px;
  padding: 0;
  list-style: none;
}
.vs-ladder__row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 16px;
  border: 1px solid var(--vs-line);
  border-radius: 8px;
  background: var(--vs-white);
}
.vs-ladder__row--ai {
  border-color: var(--vs-pink);
  background: linear-gradient(90deg, rgba(255, 0, 94, 0.06), transparent);
}
.vs-ladder__icon { font-size: 1.5rem; line-height: 1; flex-shrink: 0; }
.vs-ladder__body {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 4px 16px;
  flex: 1;
  align-items: baseline;
}
.vs-ladder__wave { grid-column: 1; color: var(--vs-blue); }
.vs-ladder__period {
  grid-column: 1;
  font-size: 13px;
  color: var(--vs-ink-soft);
}
.vs-ladder__pct {
  grid-column: 2;
  grid-row: 1 / span 2;
  font-family: var(--vs-font-display);
  font-weight: 700;
  font-size: 1.1rem;
  color: var(--vs-pink);
  align-self: center;
}
.vs-ladder__item {
  border: 1px solid var(--vs-line);
  border-radius: 8px;
  background: var(--vs-white);
  overflow: hidden;
}
.vs-ladder__item--ai {
  border-color: var(--vs-pink);
  background: linear-gradient(90deg, rgba(255, 0, 94, 0.06), var(--vs-white) 40%);
}
.vs-ladder__item > summary.vs-ladder__row {
  list-style: none;
  cursor: pointer;
  border: none;
  border-radius: 0;
  background: transparent;
  margin: 0;
}
.vs-ladder__item > summary.vs-ladder__row::-webkit-details-marker { display: none; }
.vs-ladder__item > summary.vs-ladder__row::marker { content: ""; }
.vs-ladder__item > summary.vs-ladder__row::after {
  content: "";
  width: 9px;
  height: 9px;
  margin-left: auto;
  align-self: center;
  border-right: 2px solid var(--vs-pink);
  border-bottom: 2px solid var(--vs-pink);
  transform: rotate(45deg);
  transition: transform 0.2s ease;
  flex-shrink: 0;
}
.vs-ladder__item[open] > summary.vs-ladder__row::after {
  transform: rotate(-135deg);
  margin-top: 4px;
}
.vs-ladder__expand {
  padding: 0 16px 16px 52px;
  border-top: 1px solid var(--vs-line);
  font-size: 14px;
  line-height: 1.55;
  color: var(--vs-ink-soft);
}
.vs-ladder__expand p { margin: 0 0 10px; }
.vs-ladder__expand p:last-child { margin-bottom: 0; }
.vs-ladder__expand strong { color: var(--vs-ink); font-weight: 600; }
.vs-ladder__expand dl {
  margin: 10px 0 0;
  display: grid;
  gap: 8px;
}
.vs-ladder__expand dt {
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--vs-blue);
}
.vs-ladder__expand dd { margin: 0; }
.vs-ladder__expand a { color: var(--vs-blue); }
.vs-ladder__expand a:hover { color: var(--vs-pink); }
.vs-ladder__hint {
  font-size: 12px;
  color: var(--vs-ink-soft);
  margin: 0 0 12px;
  font-style: italic;
}
/* Conclusion — evidence summary cards */
.vs-evidence-grid {
  display: grid;
  gap: 14px;
  margin: 24px 0 28px;
}
@media (min-width: 640px) {
  .vs-evidence-grid { grid-template-columns: repeat(2, 1fr); }
}
.vs-evidence-card {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 12px 14px;
  align-items: start;
  padding: 16px 18px;
  border: 1px solid var(--vs-line);
  border-radius: 10px;
  background: var(--vs-white);
  box-shadow: 0 2px 10px rgba(15, 21, 91, 0.05);
}
.vs-evidence-card__icon {
  grid-row: 1 / span 2;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background: linear-gradient(145deg, rgba(255, 0, 94, 0.12), rgba(15, 21, 91, 0.06));
  color: var(--vs-pink);
  flex-shrink: 0;
}
.vs-evidence-card__icon svg {
  width: 26px;
  height: 26px;
  display: block;
}
.vs-evidence-card__label {
  margin: 0;
  font-family: var(--vs-font-display);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--vs-pink);
  line-height: 1.2;
}
.vs-evidence-card__body {
  margin: 0;
  font-size: 14px;
  line-height: 1.55;
  color: var(--vs-ink-soft);
  grid-column: 2;
}
.vs-evidence-card__body strong { color: var(--vs-ink); }
.vs-evidence-card--punchline {
  grid-column: 1 / -1;
  display: block;
  border-color: var(--vs-pink);
  background: linear-gradient(135deg, rgba(255, 0, 94, 0.08) 0%, var(--vs-white) 55%);
  padding: 20px 20px 20px 72px;
  position: relative;
}
.vs-evidence-card--punchline .vs-evidence-card__icon {
  position: absolute;
  left: 18px;
  top: 20px;
  grid-row: auto;
}
.vs-evidence-card--punchline .vs-evidence-card__label {
  display: block;
  margin-bottom: 8px;
}
.vs-evidence-card--punchline .vs-evidence-card__body {
  grid-column: auto;
  font-size: 15px;
  color: var(--vs-ink);
}
.vs-subsection--evidence {
  display: flex;
  align-items: center;
  gap: 12px;
}
.vs-subsection__icon {
  display: inline-flex;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: rgba(255, 0, 94, 0.1);
  color: var(--vs-pink);
  flex-shrink: 0;
}
.vs-subsection__icon svg { width: 22px; height: 22px; }
.vs-figure {
  margin: 28px 0;
  text-align: center;
}
.vs-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: 1px solid var(--vs-line);
}
.vs-figure figcaption {
  margin-top: 10px;
  font-size: 13px;
  color: var(--vs-ink-soft);
  text-align: left;
}
.vs-figure--liebig {
  margin: 24px auto 28px;
  max-width: 720px;
}
.vs-figure--liebig img {
  display: block;
  margin: 0 auto;
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: 1px solid var(--vs-pink-20, #ffd1e0);
  box-shadow: 0 8px 28px rgba(255, 0, 94, 0.12);
}
.vs-figure--liebig-interactive {
  margin: 24px 0 32px;
  max-width: 100%;
  width: 100%;
}
.vs-figure--liebig-interactive iframe {
  display: block;
  width: 100%;
  min-height: 680px;
  height: 720px;
  border: none;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(255, 0, 94, 0.14);
  background: var(--vs-white);
}
.vs-footnotes {
  font-size: 13px;
  color: var(--vs-ink-soft);
  margin: 16px 0 24px;
  padding-left: 1.25rem;
}
.vs-footnotes--compact { margin-top: 12px; }
.vs-footnotes a { color: var(--vs-blue); }
.vs-chart-mount {
  position: relative;
  margin: 24px 0 32px;
  padding: 16px;
  border: 1px solid var(--vs-line);
  border-radius: 8px;
  background: var(--vs-white);
  min-height: 280px;
}
.vs-capex-chart-mount {
  min-height: 420px;
  padding: 20px 18px 24px;
  background: linear-gradient(180deg, #fff 0%, #fffaf8 100%);
  border-color: rgba(255, 0, 94, 0.25);
}
.vs-capex-chart-mount canvas {
  min-height: 360px;
  max-height: none;
  height: 360px !important;
}
.vs-speed-chart-mount {
  min-height: 400px;
  padding: 20px 18px 24px;
}
.vs-speed-chart-mount canvas {
  min-height: 340px;
  max-height: none;
  height: 340px !important;
}
.vs-avi-sector-chart-mount { min-height: 380px; }
.vs-chart-mount canvas { max-height: none; }
.vs-chart-hint {
  margin: 12px 0 0;
  font-size: 13px;
  color: var(--vs-ink-soft);
}
/* citation link styles live in report-styles.css (sup.vs-cite) */
.vs-expand {
  margin: 28px 0 32px;
  border: 1px solid var(--vs-line);
  border-radius: 8px;
  background: var(--vs-white);
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(15, 21, 91, 0.06);
}
.vs-expand__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px 16px;
  padding: 14px 18px;
  cursor: pointer;
  list-style: none;
  background: linear-gradient(90deg, rgba(255, 0, 94, 0.08), var(--vs-white) 55%);
  border-left: 4px solid var(--vs-pink);
  font-family: var(--vs-font-display);
  user-select: none;
}
.vs-expand__bar::-webkit-details-marker { display: none; }
.vs-expand__bar::marker { content: ""; }
.vs-expand__bar::after {
  content: "";
  width: 10px;
  height: 10px;
  margin-left: auto;
  border-right: 2px solid var(--vs-pink);
  border-bottom: 2px solid var(--vs-pink);
  transform: rotate(45deg);
  transition: transform 0.2s ease;
  flex-shrink: 0;
}
.vs-expand[open] .vs-expand__bar::after {
  transform: rotate(-135deg);
  margin-top: 6px;
}
.vs-expand__title {
  font-weight: 700;
  font-size: 15px;
  color: var(--vs-blue);
}
.vs-expand__subtitle {
  font-size: 13px;
  font-weight: 400;
  color: var(--vs-ink-soft);
  font-family: var(--vs-font-body, "Roboto", sans-serif);
}
.vs-expand__panel {
  padding: 8px 20px 24px;
  border-top: 1px solid var(--vs-line);
}
.vs-expand__panel .vs-minor { margin-top: 20px; }
.vs-expand__lead { margin: 12px 0 16px; }
.vs-expand__defense {
  margin: 20px 0 12px;
  padding: 14px 16px;
  background: rgba(15, 21, 91, 0.04);
  border-radius: 6px;
  font-size: 14px;
}
.vs-expand__more { font-size: 13px; margin: 16px 0 0; }
.vs-quote--compact { margin: 12px 0; font-size: 15px; }
.vs-article .vs-table-wrap:has(+ h3),
.vs-article h2 + .vs-table-wrap {
  margin-top: 8px;
}
.vs-article h2:has(+ .vs-table-wrap) + .vs-table-wrap table {
  font-size: 14px;
}
"""


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    meta: dict[str, str] = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip('"')
    return meta, text[end + 3 :].lstrip()


def _linkify_urls_in_plain_text(text: str) -> str:
    """Turn bare URLs in APA reference text into external links."""
    parts: list[str] = []
    pos = 0
    for match in REF_URL_RE.finditer(text):
        parts.append(html_lib.escape(text[pos : match.start()]))
        url = match.group(0).rstrip(".,;)")
        suffix = match.group(0)[len(url) :]
        parts.append(
            f'<a href="{html_lib.escape(url)}" target="_blank" rel="noopener noreferrer">'
            f"{html_lib.escape(url)}</a>"
        )
        if suffix:
            parts.append(html_lib.escape(suffix))
        pos = match.end()
    parts.append(html_lib.escape(text[pos:]))
    return "".join(parts)


def format_reference_entry(entry: str) -> str:
    """APA list item: *italics* and clickable source URLs."""
    out: list[str] = []
    pos = 0
    for match in re.finditer(r"\*([^*]+)\*", entry):
        out.append(_linkify_urls_in_plain_text(entry[pos : match.start()]))
        out.append(f"<em>{html_lib.escape(match.group(1))}</em>")
        pos = match.end()
    out.append(_linkify_urls_in_plain_text(entry[pos:]))
    return "".join(out)


def expand_citation_markers(md: str) -> str:
    """Turn [@12] or [@3,7,19] into superscript links to #ref-N."""

    def one_link(num: str) -> str:
        return (
            f'<a href="#ref-{num}" class="vs-cite-link" '
            f'title="Reference {num}">{num}</a>'
        )

    def repl(match: re.Match[str]) -> str:
        nums = re.findall(r"\d+", match.group(1))
        if not nums:
            return match.group(0)
        first_id = f' id="cite-{nums[0]}"' if len(nums) == 1 else ""
        if len(nums) == 1:
            inner = one_link(nums[0])
        elif len(nums) <= 3:
            inner = '<span class="vs-cite-sep">,</span>'.join(one_link(n) for n in nums)
        else:
            title = html_lib.escape("References " + ", ".join(nums))
            label = ",".join(nums[:3]) + "…"
            inner = (
                f'<a href="#ref-{nums[0]}" class="vs-cite-link" '
                f'title="{title}">{label}</a>'
            )
            return f'<sup class="vs-cite vs-cite--bundle"{first_id}>{inner}</sup>'
        return f'<sup class="vs-cite"{first_id}>{inner}</sup>'

    return CITE_MARKER_RE.sub(repl, md)


def prepare_references_markdown(md: str) -> tuple[str, str]:
    """Convert APA paragraphs to a numbered <ol>; return (md, plain-text download)."""
    marker = "## References (APA)"
    if marker not in md:
        return md, ""

    before, refs_block = md.split(marker, 1)
    lines = refs_block.splitlines()
    intro_lines: list[str] = []
    entries: list[str] = []
    section_titles: list[tuple[str, int]] = []  # (title, first ref num in section)

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("### "):
            section_titles.append((stripped[4:].strip(), len(entries) + 1))
        elif stripped.startswith("All references"):
            intro_lines.append(stripped)
        else:
            entries.append(stripped)

    download_lines = [
        "What is the real economic value of AI? — References (APA)",
        "Valueships · May 2026 · 74 sources",
        "",
    ]
    section_starts = {num: title for title, num in section_titles}
    ol_parts: list[str] = [
        marker,
        "",
        '<p class="vs-references-intro">'
        + (
            intro_lines[0]
            if intro_lines
            else "All references below were verified live at time of writing."
        )
        + " Superscript numbers in the report link here.</p>",
        '<p class="vs-references-download">'
        '<a class="vs-references-download__btn" href="assets/demystifying-ai-references.txt" '
        'download="demystifying-ai-references.txt">Download full reference list (.txt)</a>'
        "</p>",
        "",
    ]

    open_ol = False
    for n, entry in enumerate(entries, start=1):
        if n in section_starts:
            if open_ol:
                ol_parts.append("</ol>")
            ol_parts.append(
                f'<h3 class="vs-ref-category">{html_lib.escape(section_starts[n])}</h3>'
            )
            ol_parts.append(f'<ol class="vs-references" start="{n}">')
            open_ol = True
        ol_parts.append(
            f'<li id="ref-{n}" value="{n}">{format_reference_entry(entry)}</li>'
        )
        download_lines.append(f"{n}. {entry}")
        download_lines.append("")

    if open_ol:
        ol_parts.append("</ol>")

    return before + "\n".join(ol_parts) + "\n", "\n".join(download_lines).rstrip() + "\n"


def strip_duplicate_header(md: str) -> str:
    """Remove cover-duplicate title block (title + subtitle + pull-quote + rule)."""
    return re.sub(
        r"\A# [^\n]+\n+"
        r"## [^\n]+\n+"
        r"> \*\*[^\n]+\*\*\s*\n+"
        r"---\s*\n+",
        "",
        md,
        count=1,
    )


def wrap_tables(html: str) -> str:
    """Wrap markdown tables only; do not double-wrap HTML blocks that already use vs-table-wrap."""
    html = re.sub(
        r'<div class="vs-table-wrap">\s*<div class="vs-table-wrap">',
        r'<div class="vs-table-wrap">',
        html,
    )
    # Dedupe double table-wrap only; never swallow </div> that closes vs-expand__panel.
    html = re.sub(
        r"</table>\s*</div>\s*</div>(?!\s*</details>)",
        "</table></div>",
        html,
    )

    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"__VS_TABLE_BLOCK_{len(protected) - 1}__"

    html = re.sub(
        r'<div class="vs-table-wrap">\s*<table class="vs-table">.*?</table>\s*</div>',
        protect,
        html,
        flags=re.DOTALL,
    )

    html = re.sub(
        r"<table>",
        '<div class="vs-table-wrap"><table class="vs-table">',
        html,
    )
    html = re.sub(r"</table>(?!</div>)", "</table></div>", html)

    for i, block in enumerate(protected):
        html = html.replace(f"__VS_TABLE_BLOCK_{i}__", block)

    # Safety: restore panel </motion> stripped by older dedupe rules.
    html = re.sub(
        r'(<div class="vs-expand__panel">[\s\S]*?</table></div>)(\s*)</details>',
        r"\1\n\n</div>\2</details>",
        html,
    )

    return html

def postprocess_html(html: str) -> str:
    html = html.replace("<h2>", '<h2 class="vs-section-title">')
    html = html.replace("<h3>", '<h3 class="vs-subsection">')
    html = html.replace("<h4>", '<h4 class="vs-minor">')
    html = html.replace("<ul>", '<ul class="vs-list">')
    html = html.replace("<blockquote>", '<blockquote class="vs-quote">')
    html = re.sub(r"<hr\s*/?>", '<hr class="vs-divider" />', html)
    html = wrap_tables(html)
    html = re.sub(
        r'(<p>)(https://[^\s<]+)(</p>)',
        r'\1<a href="\2" target="_blank" rel="noopener">\2</a>\3',
        html,
    )
    html = re.sub(
        r'<blockquote class="vs-quote"><p><strong>(Inside unrestructured organisations[^<]+)</strong></p></blockquote>',
        r'<blockquote class="vs-quote vs-pull"><p><strong>\1</strong></p></blockquote>',
        html,
        count=1,
    )
    return unwrap_html_blocks(html)


def unwrap_html_blocks(html: str) -> str:
    """Strip <p> wrappers markdown adds around raw HTML blocks."""
    block_classes = (
        "vs-vpq-chart-mount",
        "vs-buyer-bars",
        "vs-pricing-gap",
        "vs-vpq-zones",
        "vs-chart-mount",
        "vs-speed-chart-mount",
        "vs-capex-chart-mount",
        "vs-ladder",
        "vs-ladder__item",
        "vs-evidence-grid",
        "vs-evidence-card",
        "vs-macro-grid",
        "vs-expand",
        "vs-social-figure",
        "vs-chapter-cta",
    )
    for cls in block_classes:
        html = re.sub(
            rf"<p>\s*(<(?:motion|details)[^>]*class=\"[^\"]*{cls}[^\"]*\")".replace(
                "motion", "div"
            ),
            r"\1",
            html,
        )
    for cls in ("vs-figure", "vs-footnotes", "vs-references-intro", "vs-references-download"):
        html = re.sub(rf"<p>\s*(<(?:figure|p|ol)[^>]*class=\"[^\"]*{cls}[^\"]*\")", r"\1", html)
    html = re.sub(
        r"(</(?:motion|figure|ol)>)\s*</p>".replace("motion", "motion"),
        r"\1",
        html,
    )
    html = re.sub(r"(</(?:div|figure|ol)>)\s*</p>", r"\1", html)
    html = re.sub(
        r'(<motion id="vs-vpq-chart"[^>]*></motion>)\s*</p>'.replace("motion", "motion"),
        r"\1",
        html,
    )
    html = re.sub(
        r'(<motion id="vs-vpq-chart"[^>]*></motion>)\s*</p>'.replace("motion", "motion"),
        r"\1",
        html,
    )
    html = re.sub(
        r'(<div id="vs-vpq-chart"[^>]*></motion>)\s*</p>'.replace("motion", "div"),
        r"\1",
        html,
    )
    html = re.sub(
        r'(<motion class="vs-buyer-bars"[^>]*>.*?</motion>)\s*</p>'.replace("motion", "div"),
        r"\1",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<div class="vs-vpq-zones">.*?</motion>)\s*</p>'.replace("motion", "motion"),
        r"\1",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(<div class="vs-vpq-zones">.*?</div>)\s*</p>',
        r"\1",
        html,
        count=1,
        flags=re.DOTALL,
    )
    return html


def md_to_html_body(md: str) -> str:
    html = markdown.markdown(
        md,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
        output_format="html5",
    )
    return postprocess_html(html)


def split_ceo_quotes(html: str) -> str:
    """Inject per-quote CEO cards after the barber section intro paragraph."""
    h3 = re.search(
        r'<h3 class="vs-subsection"[^>]*>Don[^<]*barber[^<]*</h3>',
        html,
        flags=re.IGNORECASE,
    )
    if not h3:
        return html

    pos = h3.end()
    method_note = re.match(
        r'\s*<p class="vs-method-note">.*?</p>',
        html[pos:],
        flags=re.DOTALL,
    )
    if method_note:
        pos += method_note.end()

    intro = re.match(r"\s*<p[^>]*>.*?</p>", html[pos:], flags=re.DOTALL)
    if not intro:
        return html
    insert_at = pos + intro.end()

    quotes = [
        ("Dario Amodei (Anthropic CEO), May 2025 (Axios / Fortune):", "AI could wipe out half of all entry-level white-collar jobs and spike unemployment to 20 % within one to five years.", "47"),
        ("Dario Amodei, <em>Machines of Loving Grace</em> (October 2024):", "Powerful AI — smarter than a Nobel Prize winner across most relevant fields — could come as early as 2026.", "46"),
        ("Sam Altman, <em>Reflections</em> (January 2025):", "We are now confident we know how to build AGI as we have traditionally understood it.", ""),
        ("Sam Altman, Fortune (July 2025):", "Intelligence too cheap to meter is well within grasp.", ""),
        ("Jensen Huang, Milken Institute (May 2025):", "Every job will be affected, and immediately. You're not going to lose your job to AI, but you're going to lose your job to someone who uses AI.", "52"),
        ("Jensen Huang, TechCrunch (March 2024):", "If AGI is defined as a software program performing 8 percent better than most people on a specific set of tests, AGI is within five years.", "51"),
        ("Anthropic Economic Index (March 2026):", "49 percent of jobs see Claude used for at least a quarter of their tasks.", "49"),
    ]
    cards = "".join(
        f'<blockquote class="vs-quote vs-quote--ceo"><p><strong>{who}</strong> "{said}"'
        + (
            f' <sup class="vs-cite"><a href="#ref-{num}" class="vs-cite-link">{num}</a></sup>'
            if num
            else ""
        )
        + "</p></blockquote>\n"
        for who, said, num in quotes
    )
    return html[:insert_at] + "\n" + cards + html[insert_at:]


def format_pricing_zones(html: str) -> str:
    pattern = (
        r'<blockquote class="vs-quote">\s*'
        r"(<p><strong>OUTCOME ZONE.*?</p>\s*"
        r"<p><strong>EFFORT ZONE.*?</p>\s*"
        r"<p><strong>PREMIUM ZONE.*?</p>\s*"
        r"<p><strong>SUBSCRIPTION ZONE.*?</p>)\s*"
        r"</blockquote>"
    )
    block = re.search(pattern, html, flags=re.DOTALL)
    if not block:
        return html
    parts = re.findall(r"<p>(.*?)</p>", block.group(1), flags=re.DOTALL)
    cards = "".join(f'<div class="vs-zone"><p>{p.strip()}</p></div>' for p in parts)
    return html[: block.start()] + cards + html[block.end() :]


def strip_heading_text(html_fragment: str) -> str:
    return html_lib.unescape(re.sub(r"<[^>]+>", "", html_fragment)).strip()


def heading_slug(text: str, max_len: int = 48) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:max_len]


def sub_letter(index: int) -> str:
    if index < 26:
        return chr(ord("a") + index)
    return f"a{chr(ord('a') + index - 26)}"


HEADING_PATTERN = re.compile(
    r'<h2 class="vs-section-title"(?: id="[^"]*")?>(.*?)</h2>|'
    r'<h3 class="vs-subsection"(?: id="[^"]*")?>(.*?)</h3>',
    re.DOTALL,
)


def short_section_label(title: str, max_len: int = 26) -> str:
    t = re.sub(r"\s+", " ", title).strip()
    if len(t) <= max_len:
        return t
    return t[: max_len - 1].rstrip() + "…"


def build_section_nav_html(chapters: list[dict]) -> str:
    """Horizontal sticky chapter pills (built from TOC chapter list)."""
    if not chapters:
        return ""
    pills: list[str] = []
    for ch in chapters:
        num = html_lib.escape(ch["num"])
        title = html_lib.escape(ch["title"])
        short = html_lib.escape(short_section_label(ch["title"]))
        cid = html_lib.escape(ch["id"])
        pills.append(
            f'<a class="vs-section-nav__pill" href="#{cid}" '
            f'title="{title}">'
            f'<span class="vs-section-nav__pill-num">{num}</span>'
            f'<span class="vs-section-nav__pill-label">{short}</span></a>'
        )
    return (
        '<nav class="vs-section-nav" id="vs-section-nav" '
        'aria-label="Report sections" hidden>\n'
        '  <div class="vs-section-nav__inner">\n'
        '    <span class="vs-section-nav__sub" id="vs-section-nav-sub" hidden></span>\n'
        '    <div class="vs-section-nav__track" id="vs-section-nav-track" role="navigation">\n'
        f'      {"".join(pills)}\n'
        "    </div>\n"
        "  </div>\n"
        "</nav>\n"
    )


def build_toc(html: str) -> tuple[str, str, str]:
    """Numbered chapter TOC (1, 2, …) with lettered sub-sections (1a, 1b, …)."""
    chapter_num = 0
    sub_index = 0
    toc_chapters: list[dict] = []
    out: list[str] = []
    pos = 0

    for match in HEADING_PATTERN.finditer(html):
        out.append(html[pos : match.start()])
        if match.group(1) is not None:
            chapter_num += 1
            sub_index = 0
            raw = match.group(1)
            title = strip_heading_text(raw)
            slug = heading_slug(title)
            if "methodology" in slug and "how-this-report" in slug:
                sid = "avi-methodology-appendix"
            elif "references" in slug and "apa" in slug:
                sid = "avi-references"
            else:
                sid = f"ch-{chapter_num}-{slug}"
            out.append(f'<h2 class="vs-section-title" id="{sid}">{raw}</h2>')
            toc_chapters.append(
                {"num": str(chapter_num), "title": title, "id": sid, "subs": []}
            )
        elif match.group(2) is not None and toc_chapters:
            raw = match.group(2)
            title = strip_heading_text(raw)
            slug = heading_slug(title)
            letter = sub_letter(sub_index)
            sub_index += 1
            num_label = f"{chapter_num}{letter}"
            sid = f"ch-{chapter_num}{letter}-{slug}"
            out.append(f'<h3 class="vs-subsection" id="{sid}">{raw}</h3>')
            toc_chapters[-1]["subs"].append(
                {"num": num_label, "title": title, "id": sid}
            )
        elif match.group(2) is not None:
            out.append(match.group(0))
        pos = match.end()

    out.append(html[pos:])
    html = "".join(out)

    if not toc_chapters:
        return html, "", ""

    items: list[str] = []
    for ch in toc_chapters:
        num = html_lib.escape(ch["num"])
        title = html_lib.escape(ch["title"])
        cid = html_lib.escape(ch["id"])
        block = (
            f'<li class="vs-toc__chapter">'
            f'<a href="#{cid}"><span class="vs-toc__num">{num}</span> {title}</a>'
        )
        if ch["subs"]:
            subs = "\n".join(
                f'<li><a href="#{html_lib.escape(s["id"])}">'
                f'<span class="vs-toc__num">{html_lib.escape(s["num"])}</span> '
                f'{html_lib.escape(s["title"])}</a></li>'
                for s in ch["subs"]
            )
            block += f'<ol class="vs-toc__subs">{subs}</ol>'
        block += "</li>"
        items.append(block)

    nav = (
        '<nav class="vs-toc" id="vs-toc" aria-label="Table of contents">'
        '<p class="vs-toc__label">Contents</p>'
        f'<ol class="vs-toc__chapters">{"".join(items)}</ol>'
        "</nav>"
    )
    section_nav = build_section_nav_html(toc_chapters)
    return html, nav, section_nav


SOCIAL_CARD_MARKER = re.compile(r"<!--\s*VS-SOCIAL-CARD:(hero1|hero2|hero3|speed)\s*-->")

SOCIAL_CARD_CAPTIONS: dict[str, str] = {
    "hero1": "",
    "hero2": (
        "Shareable visual — hyperscaler CapEx vs measured productivity. "
        "Source: Valueships <em>Demystifying the Value of AI</em> (2026)."
    ),
    "hero3": (
        "Shareable visual — AI Value Index (AVI) by sector. "
        "Median ~15%; four sectors above 25%. "
        "Source: Valueships <em>Demystifying the Value of AI</em> (2026)."
    ),
    "speed": (
        "Shareable visual — productivity vs information speed (log scale). "
        "LLM-era AI sits ~2 pp/yr below the historical trend. "
        "Source: Valueships <em>Demystifying the Value of AI</em> (2026)."
    ),
}

SOCIAL_FIGURE_CSS = """
/* In-article social cards — full article rail (not narrow square thumbnails) */
.vs-article .vs-social-figure {
  margin: 2rem 0 2.75rem;
  max-width: 100%;
  width: 100%;
  padding: 0;
  border: none;
}
.vs-article .vs-social-figure .vs-card {
  width: 100%;
  margin: 0;
  aspect-ratio: 2.15 / 1;
  max-height: min(56vw, 440px);
}
.vs-article .vs-social-figure--hero1 .vs-card__hero-num {
  font-size: clamp(52px, 12cqi, 110px);
  margin: 10px 0 8px;
}
.vs-article .vs-social-figure--hero1 .vs-card__headline {
  font-size: clamp(20px, 3.6cqi, 36px);
  margin-bottom: 16px;
}
.vs-article .vs-social-figure--hero1 .vs-card__comparison {
  width: 92%;
}
.vs-social-figure figcaption {
  margin-top: 12px;
  font-family: var(--vs-font-body);
  font-size: 13px;
  line-height: 1.45;
  color: var(--vs-ink-soft);
  text-align: left;
}
/* Ladder + charts share the same rail as body copy */
.vs-article > .vs-ladder,
.vs-article > .vs-chart-mount,
.vs-article > .vs-figure {
  max-width: 100%;
  width: 100%;
}
.vs-quote--pull {
  margin: 28px 0 32px;
  padding: 20px 28px;
  border-left: 5px solid var(--vs-pink);
  background: var(--vs-pink-5);
  font-family: var(--vs-font-display);
  font-size: clamp(18px, 2vw, 22px);
  line-height: 1.45;
}
.vs-quote--pull p { margin: 0; }
"""


def load_social_card_styles() -> str:
    """Card CSS extracted from vs-social-cards.html (single source of truth)."""
    if not SOCIAL_CARDS_HTML.is_file():
        return ""
    text = SOCIAL_CARDS_HTML.read_text(encoding="utf-8")
    marker = "/* ===== shared card chrome ===== */"
    if marker not in text:
        raise ValueError(f"Social cards CSS marker not found in {SOCIAL_CARDS_HTML.name}")
    start = text.index(marker)
    end = text.index("</style>", start)
    return text[start:end] + SOCIAL_FIGURE_CSS


def load_social_card_sections() -> dict[str, str]:
    """Parse the four <section class=\"vs-card vs-card--*\"> blocks."""
    if not SOCIAL_CARDS_HTML.is_file():
        return {}
    text = SOCIAL_CARDS_HTML.read_text(encoding="utf-8")
    cards: dict[str, str] = {}
    pattern = re.compile(
        r'<section class="vs-card vs-card--(hero1|hero2|hero3|speed)"[^>]*>.*?</section>',
        re.DOTALL,
    )
    for match in pattern.finditer(text):
        key = match.group(1)
        section = match.group(0)
        if key == "speed":
            section = section.replace('id="vsArrow"', 'id="vsArrow-speed-social"')
            section = section.replace("url(#vsArrow)", "url(#vsArrow-speed-social)")
        cards[key] = section
    if cards and len(cards) != 4:
        raise ValueError(
            f"Expected 4 social cards in {SOCIAL_CARDS_HTML.name}, found {len(cards)}: {sorted(cards)}"
        )
    return cards


def inject_social_cards(html: str, cards: dict[str, str]) -> str:
    """Replace <!-- VS-SOCIAL-CARD:key --> markers with figure + section HTML."""
    if not cards:
        return html

    def replace_marker(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in cards:
            raise KeyError(f"Unknown social card key: {key}")
        caption = SOCIAL_CARD_CAPTIONS.get(key, "")
        figcaption = f"<figcaption>{caption}</figcaption>\n" if caption.strip() else ""
        return (
            f'<figure class="vs-social-figure vs-social-figure--{key}" role="group">\n'
            f"{cards[key]}\n"
            f"{figcaption}"
            "</figure>"
        )

    return SOCIAL_CARD_MARKER.sub(replace_marker, html)


def anchor_special_sections(html: str) -> str:
    """Reserved for post-TOC anchor tweaks (methodology id set in build_toc)."""
    return html


CHAPTER_CTA_HTML = (
    '<div class="vs-chapter-cta" role="complementary" aria-label="Contact Valueships about pricing">\n'
    f'  <a class="vs-chapter-cta__btn" href="{html_lib.escape(CONTACT_CTA_URL, quote=True)}">'
    "Let\'s talk about your pricing!</a>\n"
    "</div>\n"
)


def inject_chapter_ctas(html: str) -> str:
    """Insert a pricing CTA after each major chapter (before the next h2). Skip References."""
    pattern = re.compile(
        r'<h2 class="vs-section-title" id="([^"]+)">',
    )
    matches = list(pattern.finditer(html))
    if not matches:
        return html

    insert_at: list[int] = []
    for i in range(len(matches) - 1):
        insert_at.append(matches[i + 1].start())

    last_id = matches[-1].group(1)
    if "references" not in last_id.lower():
        insert_at.append(len(html))

    for pos in sorted(insert_at, reverse=True):
        html = html[:pos] + CHAPTER_CTA_HTML + html[pos:]

    return html


def hero_tagline_html(tagline: str) -> str:
    if ". " in tagline:
        first, rest = tagline.split(". ", 1)
        return f"{html_lib.escape(first)}.<br>{html_lib.escape(rest)}"
    return html_lib.escape(tagline)


def cover_title_html(title: str) -> str:
    """Cover title as exactly two lines (block spans), balanced for typical cover width."""
    t = title.strip()
    lower = t.lower()
    # Balanced break — avoids a single long line that re-wraps at ~620px cover width
    if lower == "what is the real economic value of ai?":
        return (
            '<span class="vs-cover__title-line">What is the real</span>'
            '<span class="vs-cover__title-line">economic value of AI?</span>'
        )
    if " of " in lower:
        idx = lower.rfind(" of ")
        return (
            f'<span class="vs-cover__title-line">{html_lib.escape(t[:idx])}</span>'
            f'<span class="vs-cover__title-line">{html_lib.escape(t[idx + 1 :])}</span>'
        )
    return f'<span class="vs-cover__title-line">{html_lib.escape(t)}</span>'


def first_section_id(html_body: str) -> str:
    """Anchor for cover CTA — first h2 after TOC build (Foreword)."""
    match = re.search(r'<h2 class="vs-section-title" id="([^"]+)"', html_body)
    return match.group(1) if match else "report-start"


def cover_section(meta: dict[str, str], foreword_id: str = "report-start") -> str:
    title = meta.get("title", "What is the real economic value of AI?")
    subtitle = meta.get(
        "subtitle",
        "A meta research analysis of productivity reports and pricing implications",
    )
    tagline = meta.get(
        "tagline",
        "Today AI is a useful, highly effective tool, and yet it's far away from the 10x output revolution we were promised",
    )
    byline = meta.get("cover_byline", "by Maciej Wilczynski, Ph.D., Managing Partner")

    return f"""<section class="vs-cover" id="cover" aria-label="Report cover">
  <div class="vs-cover__backdrop" aria-hidden="true">
    <img src="{HERO_IMAGE}" alt="" class="vs-cover__photo" width="800" height="532">
    <div class="vs-cover__tint"></div>
  </div>
  {KEYVIS_COVER}
  <div class="vs-cover__frame">
    <div class="vs-cover__main">
      <h1 class="vs-cover__title">{cover_title_html(title)}</h1>
      <p class="vs-cover__subtitle">{html_lib.escape(subtitle)}</p>
    </div>
    <div class="vs-cover__bottom">
      <p class="vs-cover__tagline">{hero_tagline_html(tagline)}</p>
      <p class="vs-cover__meta">{html_lib.escape(byline)}</p>
    </div>
  </div>
  <a class="vs-cover__cta vs-jump-no-hash" href="#{html_lib.escape(foreword_id)}">Read the report</a>
</section>"""


def load_chart_script(path: Path, label: str) -> str:
    """Load chart JS from assets/ (same repo root as this script and the .html output)."""
    if not path.is_file():
        raise FileNotFoundError(
            f"Missing chart script: {path}\n"
            f"Expected: {ASSETS_DIR.name}/{path.name} next to {OUT_PATH.name}"
        )
    js = path.read_text(encoding="utf-8")
    return js.replace("</script>", "<\\/script>")


def cms_head_extras(meta: dict[str, str]) -> str:
    title = meta.get("title", "What is the real economic value of AI?")
    tagline = meta.get(
        "tagline",
        "Today AI is a useful, highly effective tool, and yet it's far away from the 10x output revolution we were promised",
    )
    t = html_lib.escape(title)
    d = html_lib.escape(tagline)
    return f"""<meta name="description" content="{d}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="article">
"""


def strip_preview_chrome(page: str) -> str:
    """Adjust comments for CMS publish bundle."""
    return page.replace(
        "<!-- Generated from demystifying-the-value-of-ai.md — edit the .md, then: python3 build_branded_html.py -->",
        "<!-- CMS publish bundle — generated from demystifying-the-value-of-ai.md via build_branded_html.py -->",
        1,
    )


def main() -> None:
    raw = MD_PATH.read_text(encoding="utf-8")
    meta, md_body = parse_frontmatter(raw)
    md_body = strip_duplicate_header(md_body)
    md_body, references_download = prepare_references_markdown(md_body)
    md_body = expand_citation_markers(md_body)
    if references_download:
        REFERENCES_TXT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REFERENCES_TXT_PATH.write_text(references_download, encoding="utf-8")

    vpq_chart_js = load_chart_script(VPQ_CHART_JS, "VPQ")
    capex_chart_js = load_chart_script(CAPEX_CHART_JS, "CapEx")
    avi_sector_chart_js = load_chart_script(AVI_SECTOR_CHART_JS, "AVI sector")
    speed_chart_js = load_chart_script(SPEED_CHART_JS, "Productivity speed")

    social_cards = load_social_card_sections()

    body = md_to_html_body(md_body)
    body = inject_social_cards(body, social_cards)
    body = split_ceo_quotes(body)
    body = format_pricing_zones(body)
    body, toc, section_nav = build_toc(body)
    body = anchor_special_sections(body)
    body = inject_chapter_ctas(body)

    css_path = ROOT / "report-styles.css"
    css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""
    css += MACRO_GRID_CSS
    css += SECTION_NAV_CSS
    css += load_social_card_styles()

    foreword_id = first_section_id(body)
    cover = cover_section(meta, foreword_id)
    doc_title = html_lib.escape(meta.get("title", "What is the real economic value of AI?"))

    page = f"""<!DOCTYPE html>
<!-- Generated from demystifying-the-value-of-ai.md — edit the .md, then: python3 build_branded_html.py -->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>{EARLY_SCROLL_GUARD_SCRIPT}</script>
<title>{doc_title} — Valueships</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;500;700;900&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body class="has-cover">
<div class="vs-chrome" id="vs-chrome">
<header class="vs-topnav vs-topnav--cover">
  <a href="https://www.valueships.com" class="vs-topnav__logo" target="_blank" rel="noopener noreferrer"><img src="{LOGO_COVER}" alt="Valueships" class="vs-logo-img" width="189" height="32"></a>
</header>
{READ_NAV_HTML}
{section_nav}
</div>
{cover}
<div id="vs-chrome-spacer" class="vs-chrome-spacer" aria-hidden="true"></div>
<div id="report-start" class="vs-report-start"></div>
<div class="vs-layout">{toc}
  <article class="vs-article" id="vs-report" aria-label="Report body">
{BODY_KV_TL}{BODY_KV_BR}{body}
  </article>
</div>
<footer class="vs-footer">
  <img src="{LOGO_COVER}" alt="Valueships" class="vs-footer__logo-img">
  <p class="vs-footer__brand">Engineering pricing for tech companies</p>
</footer>
<script>{NAV_COVER_SCRIPT}</script>
<script>{TOC_SCROLL_SPY_SCRIPT}</script>
<script>{READING_NAV_SCRIPT}</script>
{CHART_JS_CDN}
<script id="vs-speed-chart-bundle">
/* Productivity vs information speed — bundled from {SPEED_CHART_JS.relative_to(ROOT).as_posix()} */
{speed_chart_js}
</script>
<script id="vs-capex-chart-bundle">
/* CapEx vs productivity — bundled from {CAPEX_CHART_JS.relative_to(ROOT).as_posix()} */
{capex_chart_js}
</script>
<script id="vs-avi-sector-chart-bundle">
/* AVI by sector — bundled from {AVI_SECTOR_CHART_JS.relative_to(ROOT).as_posix()} */
{avi_sector_chart_js}
</script>
<script id="vs-vpq-chart-bundle">
/* AVI Pricing Quadrant — bundled from {VPQ_CHART_JS.relative_to(ROOT).as_posix()} */
{vpq_chart_js}
</script>
</body>
</html>"""

    OUT_PATH.write_text(page, encoding="utf-8")

    cms_page = strip_preview_chrome(page)
    cms_page = cms_page.replace(
        "<title>",
        cms_head_extras(meta) + "<title>",
        1,
    )
    CMS_OUT_PATH.write_text(cms_page, encoding="utf-8")
    INDEX_PATH.write_text(cms_page, encoding="utf-8")

    print(f"Wrote {OUT_PATH} ({len(page):,} bytes) from {MD_PATH.name}")
    print(f"Wrote {CMS_OUT_PATH} ({len(cms_page):,} bytes) — upload this file to CMS")
    print(f"Wrote {INDEX_PATH} ({len(cms_page):,} bytes) — Vercel / static host entry")


if __name__ == "__main__":
    main()
