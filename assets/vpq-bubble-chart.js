/**
 * Valueships AVI Pricing Quadrant™ — interactive bubble chart
 * X: AVI (%)  ·  Y: Revenue attribution (0–100)  ·  bubble size: value $/FTE/yr
 */
(function initVpqChart() {
  function run() {
    const root = document.getElementById("vs-vpq-chart");
    if (!root) return;

    const AVI_THRESHOLD = 15;
    const ATTR_THRESHOLD = 55;
    const X_MIN = 0;
    const X_MAX = 32;
    const Y_MIN = 0;
    const Y_MAX = 100;
    const clipId = "vs-vpq-clip-" + Math.random().toString(36).slice(2, 9);

    const ZONES = {
      outcome: { label: "Outcome zone ★", color: "#FF005E", capture: "30–50 %" },
      effort: { label: "Effort zone", color: "#FF669D", capture: "10–25 %" },
      premium: { label: "Premium zone", color: "#0F155B", capture: "10–20 %" },
      subscription: { label: "Subscription zone", color: "#5A5A5C", capture: "5–10 %" },
    };

    const SECTORS = [
      { id: "finance-bo", name: "Finance back-office", avi: 28.6, attr: 88, value: 22920, zone: "outcome", model: "Outcome / gainsharing" },
      { id: "mkt-creative", name: "Marketing creative", avi: 25.5, attr: 76, value: 22950, zone: "outcome", model: "Outcome / gainsharing" },
      { id: "mfg-lh", name: "Mfg lighthouses", avi: 24.8, attr: 82, value: 17325, zone: "outcome", model: "Outcome / gainsharing" },
      { id: "legal-doc", name: "Legal doc review", avi: 24.6, attr: 74, value: 49100, zone: "outcome", model: "Outcome / gainsharing" },
      { id: "software", name: "Software development", avi: 21.6, attr: 38, value: 28080, zone: "effort", model: "Credits / consumption" },
      { id: "consulting", name: "Consulting", avi: 20.5, attr: 42, value: 36900, zone: "effort", model: "Credits / consumption" },
      { id: "tmt-it", name: "TMT IT", avi: 17.8, attr: 40, value: 21360, zone: "effort", model: "Credits / consumption" },
      { id: "sales", name: "Sales (conversion unit)", avi: 15.6, attr: 92, value: 17160, zone: "outcome", model: "Outcome / gainsharing" },
      { id: "finserv", name: "FinServ overall", avi: 15.6, attr: 44, value: 18720, zone: "effort", model: "Credits / consumption" },
      { id: "healthcare", name: "Healthcare (scribes)", avi: 15.5, attr: 36, value: 38750, zone: "effort", model: "Credits / consumption" },
      { id: "cs", name: "Customer service", avi: 13.4, attr: 68, value: 8040, zone: "premium", model: "Per-seat + outcome bonus" },
      { id: "retail", name: "Consumer & retail", avi: 13.2, attr: 72, value: 9240, zone: "premium", model: "Per-seat + outcome bonus" },
      { id: "aec", name: "AEC / construction", avi: 12.2, attr: 32, value: 11590, zone: "subscription", model: "Per-seat + usage cap" },
      { id: "mfg-avg", name: "Mfg (average plant)", avi: 9.9, attr: 28, value: 6930, zone: "subscription", model: "Per-seat + usage cap" },
      { id: "government", name: "Government", avi: 9.3, attr: 18, value: 8370, zone: "subscription", model: "Per-seat + usage cap" },
      { id: "legal-sr", name: "Legal senior advisory", avi: 8.6, attr: 58, value: 30100, zone: "premium", model: "Per-seat + outcome bonus" },
      { id: "education", name: "Education", avi: 7.4, attr: 22, value: 5180, zone: "subscription", model: "Per-seat + usage cap" },
    ];

    const W = 720;
    const H = 480;
    const pad = { top: 28, right: 24, bottom: 52, left: 56 };
    const plotW = W - pad.left - pad.right;
    const plotH = H - pad.top - pad.bottom;

    const xScale = (avi) => pad.left + ((avi - X_MIN) / (X_MAX - X_MIN)) * plotW;
    const yScale = (attr) => pad.top + plotH - ((attr - Y_MIN) / (Y_MAX - Y_MIN)) * plotH;
    const xThresh = xScale(AVI_THRESHOLD);
    const yThresh = yScale(ATTR_THRESHOLD);

    const maxVal = Math.max(...SECTORS.map((s) => s.value));
    const minVal = Math.min(...SECTORS.map((s) => s.value));
    const rScale = (v) => 9 + ((v - minVal) / (maxVal - minVal)) * 16;

    const fmtMoney = (n) => (n >= 1000 ? "$" + Math.round(n / 1000) + "K" : "$" + n);

    const esc = (s) =>
      String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/"/g, "&quot;");

    const ticksX = [0, 5, 10, 15, 20, 25, 30]
      .map((v) => {
        const x = xScale(v);
        return (
          '<line class="vs-vpq-chart__tick" x1="' + x + '" y1="' + (pad.top + plotH) + '" x2="' + x + '" y2="' + (pad.top + plotH + 5) + '"/>' +
          '<text class="vs-vpq-chart__tick-label" x="' + x + '" y="' + (pad.top + plotH + 20) + '" text-anchor="middle">' + v + "</text>"
        );
      })
      .join("");

    const ticksY = [0, 25, 50, 75, 100]
      .map((v) => {
        const y = yScale(v);
        return (
          '<line class="vs-vpq-chart__tick" x1="' + (pad.left - 5) + '" y1="' + y + '" x2="' + pad.left + '" y2="' + y + '"/>' +
          '<text class="vs-vpq-chart__tick-label" x="' + (pad.left - 10) + '" y="' + (y + 4) + '" text-anchor="end">' + v + "</text>"
        );
      })
      .join("");

    const bubblesSvg = SECTORS.map((s) => {
      const cx = xScale(s.avi);
      const cy = yScale(s.attr);
      const r = rScale(s.value);
      const z = ZONES[s.zone];
      const fillOp = s.zone === "subscription" ? 0.5 : 0.92;
      const shortName = s.name.length > 22 ? s.name.slice(0, 20) + "\u2026" : s.name;
      return (
        '<g class="vs-vpq-chart__bubble" data-id="' + esc(s.id) + '" data-zone="' + esc(s.zone) + '" tabindex="0" role="button" ' +
        'aria-label="' + esc(s.name) + ': AVI ' + s.avi + '%, attribution ' + s.attr + '">' +
        '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="' + z.color + '" fill-opacity="' + fillOp + '" stroke="' + z.color + '" stroke-width="2.5"/>' +
        '<text class="vs-vpq-chart__bubble-name" x="' + cx + '" y="' + (cy - r - 5) + '" text-anchor="middle">' + esc(shortName) + "</text>" +
        '<text class="vs-vpq-chart__bubble-label" x="' + cx + '" y="' + (cy + r + 12) + '" text-anchor="middle">' + s.avi + "%</text>" +
        "</g>"
      );
    }).join("");

    const legendHtml = Object.entries(ZONES)
      .map(
        ([key, z]) =>
          '<button type="button" class="vs-vpq-chart__legend-btn" data-zone="' + key + '">' +
          '<span class="vs-vpq-chart__legend-dot" style="background:' + z.color + '"></span>' + z.label + "</button>"
      )
      .join("");

    root.innerHTML =
      '<figure class="vs-vpq-chart__figure">' +
      '<svg class="vs-vpq-chart__svg" viewBox="0 0 ' + W + " " + H + '" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vs-vpq-chart-title">' +
      '<title id="vs-vpq-chart-title">AVI Pricing Quadrant: 17 sectors by AVI and revenue attribution</title>' +
      "<defs><clipPath id=\"" + clipId + '"><rect x="' + pad.left + '" y="' + pad.top + '" width="' + plotW + '" height="' + plotH + '"/></clipPath></defs>' +
      '<g clip-path="url(#' + clipId + ')">' +
      '<rect x="' + pad.left + '" y="' + pad.top + '" width="' + (xThresh - pad.left) + '" height="' + (yThresh - pad.top) + '" fill="#DEDFF5" opacity="0.35"/>' +
      '<rect x="' + xThresh + '" y="' + pad.top + '" width="' + (pad.left + plotW - xThresh) + '" height="' + (yThresh - pad.top) + '" fill="#FF005E" opacity="0.1"/>' +
      '<rect x="' + pad.left + '" y="' + yThresh + '" width="' + (xThresh - pad.left) + '" height="' + (pad.top + plotH - yThresh) + '" fill="#f0f0f2"/>' +
      '<rect x="' + xThresh + '" y="' + yThresh + '" width="' + (pad.left + plotW - xThresh) + '" height="' + (pad.top + plotH - yThresh) + '" fill="#FFF0F5"/>' +
      "</g>" +
      '<line class="vs-vpq-chart__thresh" x1="' + xThresh + '" y1="' + pad.top + '" x2="' + xThresh + '" y2="' + (pad.top + plotH) + '"/>' +
      '<line class="vs-vpq-chart__thresh" x1="' + pad.left + '" y1="' + yThresh + '" x2="' + (pad.left + plotW) + '" y2="' + yThresh + '"/>' +
      '<text class="vs-vpq-chart__quad-label" x="' + (pad.left + 8) + '" y="' + (pad.top + 16) + '">Premium</text>' +
      '<text class="vs-vpq-chart__quad-label vs-vpq-chart__quad-label--outcome" x="' + (pad.left + plotW - 8) + '" y="' + (pad.top + 16) + '" text-anchor="end">Outcome \u2605</text>' +
      '<text class="vs-vpq-chart__quad-label" x="' + (pad.left + 8) + '" y="' + (pad.top + plotH - 8) + '">Subscription</text>' +
      '<text class="vs-vpq-chart__quad-label" x="' + (pad.left + plotW - 8) + '" y="' + (pad.top + plotH - 8) + '" text-anchor="end">Effort</text>' +
      '<g class="vs-vpq-chart__ticks-x">' + ticksX + "</g>" +
      '<g class="vs-vpq-chart__ticks-y">' + ticksY + "</g>" +
      '<line class="vs-vpq-chart__axis" x1="' + pad.left + '" y1="' + (pad.top + plotH) + '" x2="' + (pad.left + plotW) + '" y2="' + (pad.top + plotH) + '"/>' +
      '<line class="vs-vpq-chart__axis" x1="' + pad.left + '" y1="' + pad.top + '" x2="' + pad.left + '" y2="' + (pad.top + plotH) + '"/>' +
      '<g class="vs-vpq-chart__bubbles">' + bubblesSvg + "</g>" +
      '<text class="vs-vpq-chart__axis-title" x="' + (pad.left + plotW / 2) + '" y="' + (H - 12) + '" text-anchor="middle">AI Value Index (AVI) % \u2192</text>' +
      '<text class="vs-vpq-chart__axis-title" transform="rotate(-90)" x="' + -(pad.top + plotH / 2) + '" y="14" text-anchor="middle">Revenue attribution score \u2192</text>' +
      "</svg>" +
      '<aside class="vs-vpq-chart__detail" id="vs-vpq-detail-root">' +
      '<p class="vs-vpq-chart__detail-hint">Click a bubble to inspect a sector \u00b7 ' + SECTORS.length + " sectors</p>" +
      "</aside>" +
      '<div class="vs-vpq-chart__legend" id="vs-vpq-legend-root">' + legendHtml + '</div>' +
      '<p class="vs-vpq-chart__note">Bubble size = value $/FTE/yr. Attribution = expert judgment (0\u2013100). Thresholds: AVI \u2265 ' + AVI_THRESHOLD + '%, attribution \u2265 ' + ATTR_THRESHOLD + '.</p>' +
      '</figure>';

    const detail = root.querySelector('#vs-vpq-detail-root');
    const legend = root.querySelector("#vs-vpq-legend-root");
    const svg = root.querySelector(".vs-vpq-chart__svg");

    let selected = null;

    function showDetail(s) {
      const z = ZONES[s.zone];
      detail.innerHTML =
        '<p class="vs-vpq-chart__detail-zone" style="color:' + z.color + '">' + z.label + "</p>" +
        '<h4 class="vs-vpq-chart__detail-name">' + esc(s.name) + "</h4>" +
        '<dl class="vs-vpq-chart__detail-dl">' +
        "<dt>AVI</dt><dd>" + s.avi.toFixed(1) + "%</dd>" +
        "<dt>Attribution</dt><dd>" + s.attr + "/100</dd>" +
        "<dt>Value / FTE</dt><dd>" + fmtMoney(s.value) + "/yr</dd>" +
        "<dt>Pricing model</dt><dd>" + esc(s.model) + "</dd>" +
        "<dt>Capture band</dt><dd>" + z.capture + "</dd>" +
        "</dl>";
    }

    function clearDetail() {
      detail.innerHTML =
        '<p class="vs-vpq-chart__detail-hint">Click a bubble to inspect a sector \u00b7 ' + SECTORS.length + " sectors</p>";
    }

    root.querySelectorAll(".vs-vpq-chart__bubble").forEach((g) => {
      g.addEventListener("click", (e) => {
        e.stopPropagation();
        const id = g.getAttribute("data-id");
        const s = SECTORS.find((x) => x.id === id);
        if (!s) return;
        root.querySelectorAll(".vs-vpq-chart__bubble--active").forEach((el) => el.classList.remove("vs-vpq-chart__bubble--active"));
        if (selected === id) {
          selected = null;
          clearDetail();
          return;
        }
        selected = id;
        g.classList.add("vs-vpq-chart__bubble--active");
        showDetail(s);
      });
      g.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          g.click();
        }
      });
    });

    if (svg) {
      svg.addEventListener("click", (e) => {
        if (e.target.closest && e.target.closest(".vs-vpq-chart__bubble")) return;
        selected = null;
        root.querySelectorAll(".vs-vpq-chart__bubble--active").forEach((el) => el.classList.remove("vs-vpq-chart__bubble--active"));
        clearDetail();
      });
    }

    legend.querySelectorAll(".vs-vpq-chart__legend-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const zone = btn.getAttribute("data-zone");
        const off = btn.classList.toggle("vs-vpq-chart__legend-btn--off");
        root.querySelectorAll(".vs-vpq-chart__bubble").forEach((g) => {
          if (g.getAttribute("data-zone") === zone) g.style.opacity = off ? "0.12" : "1";
        });
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
