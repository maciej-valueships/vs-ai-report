/**
 * Productivity vs information speed (log scale) — from speed-normalized chart data.
 */
(function () {
  const canvas = document.getElementById("vs-productivity-speed-chart");
  if (!canvas || typeof Chart === "undefined") return;

  const pink = "#FF005E";
  const pinkLight = "#FF669D";
  const blue = "#0F155B";
  const gray = "#5A5A5C";

  const eras = [
    { x: 0, y: 0.3, label: "Agrarian", ai: false },
    { x: 2, y: 0.78, label: "First industrial", ai: false },
    { x: 5, y: 2.82, label: "Electric", ai: false },
    { x: 8, y: 1.38, label: "ICT baseline", ai: false },
    { x: 9, y: 2.26, label: "ICT revival", ai: false },
    { x: 11, y: 0.09, label: "LLM-era AI", ai: true },
  ];

  const nonAi = eras.filter((e) => !e.ai);
  const xs = nonAi.map((e) => e.x);
  const ys = nonAi.map((e) => e.y);
  const n = xs.length;
  const sx = xs.reduce((a, b) => a + b, 0);
  const sy = ys.reduce((a, b) => a + b, 0);
  const sxx = xs.reduce((a, b) => a + b * b, 0);
  const sxy = xs.reduce((a, xi, i) => a + xi * ys[i], 0);
  const slope = (n * sxy - sx * sy) / (n * sxx - sx * sx);
  const intercept = (sy - slope * sx) / n;

  const trendLine = [];
  for (let x = 0; x <= 11; x += 0.5) {
    trendLine.push({ x, y: slope * x + intercept });
  }

  Chart.defaults.font.family = "'Roboto', system-ui, sans-serif";
  Chart.defaults.color = gray;

  new Chart(canvas, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: "Expected trend (excl. AI)",
          data: trendLine,
          type: "line",
          borderColor: "rgba(255, 0, 94, 0.45)",
          borderDash: [6, 4],
          borderWidth: 2,
          pointRadius: 0,
          tension: 0,
        },
        {
          label: "Historical eras",
          data: eras.filter((e) => !e.ai),
          backgroundColor: pinkLight,
          borderColor: "#fff",
          borderWidth: 2,
          pointRadius: 9,
          pointHoverRadius: 12,
        },
        {
          label: "LLM-era AI",
          data: eras.filter((e) => e.ai),
          backgroundColor: blue,
          borderColor: "#fff",
          borderWidth: 3,
          pointRadius: 11,
          pointHoverRadius: 14,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: "bottom",
          labels: { boxWidth: 14, padding: 14, font: { size: 12 } },
        },
        tooltip: {
          callbacks: {
            label(ctx) {
              const p = ctx.raw;
              const e = eras.find((r) => r.x === p.x && r.y === p.y);
              const name = e ? e.label : "";
              return ` ${name}: ${p.y.toFixed(2)}%/yr productivity`;
            },
          },
        },
      },
      scales: {
        x: {
          type: "linear",
          min: -0.3,
          max: 11.5,
          title: {
            display: true,
            text: "Information speed (log₁₀ scale)",
            font: { weight: "600", size: 13 },
          },
          ticks: {
            callback(v) {
              const map = { 0: "1×", 2: "100×", 5: "100K×", 8: "100M×", 9: "1B×", 11: "100B×" };
              return map[v] !== undefined ? map[v] : "";
            },
            font: { size: 11 },
          },
          grid: { color: "rgba(232, 232, 236, 0.9)" },
        },
        y: {
          min: 0,
          max: 3.2,
          title: {
            display: true,
            text: "Annual productivity gain (%/yr)",
            font: { weight: "600", size: 13 },
          },
          ticks: {
            callback: (v) => `${v}%`,
            font: { size: 11 },
          },
          grid: { color: "rgba(232, 232, 236, 0.9)" },
        },
      },
    },
  });
})();
