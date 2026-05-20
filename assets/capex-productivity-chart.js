/**
 * Interactive CapEx vs productivity — bundled into demystifying-the-value-of-ai.html
 */
(function () {
  const canvas = document.getElementById("vs-capex-chart");
  if (!canvas || typeof Chart === "undefined") return;

  const pink = "#FF005E";
  const blue = "#0F155B";
  const years = ["2022", "2024", "2025", "2026", "2027"];
  const capex = [162, 230, 448, 725, 1000];
  const productivity = [0.09, 0.09, 0.09, 0.09, 0.09];

  Chart.defaults.font.family = "'Roboto', system-ui, sans-serif";
  Chart.defaults.color = "#5A5A5C";
  Chart.defaults.font.size = 13;

  new Chart(canvas, {
    type: "line",
    data: {
      labels: years,
      datasets: [
        {
          label: "Big Tech hyperscaler CapEx ($B)",
          data: capex,
          borderColor: pink,
          backgroundColor: "rgba(255, 0, 94, 0.22)",
          fill: true,
          tension: 0.3,
          borderWidth: 3.5,
          pointRadius: 8,
          pointHoverRadius: 11,
          pointBackgroundColor: pink,
          pointBorderColor: "#fff",
          pointBorderWidth: 2,
          yAxisID: "y",
        },
        {
          label: "LLM-era AI productivity (%/yr, Acemoglu benchmark)",
          data: productivity,
          borderColor: blue,
          borderDash: [10, 6],
          borderWidth: 3.5,
          pointRadius: 8,
          pointHoverRadius: 11,
          pointBackgroundColor: blue,
          pointBorderColor: "#fff",
          pointBorderWidth: 2,
          yAxisID: "y1",
          tension: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: "index", intersect: false },
      plugins: {
        legend: {
          position: "bottom",
          labels: { boxWidth: 16, padding: 18, font: { size: 13, weight: "500" } },
        },
        tooltip: {
          titleFont: { size: 14, weight: "600" },
          bodyFont: { size: 13 },
          callbacks: {
            label(ctx) {
              const v = ctx.parsed.y;
              if (ctx.datasetIndex === 0) return ` CapEx: $${v}B`;
              return ` Productivity: ${v}%/yr`;
            },
          },
        },
      },
      scales: {
        x: {
          grid: { display: false },
          title: { display: true, text: "Year", font: { weight: "600", size: 14 } },
          ticks: { font: { size: 12, weight: "500" } },
        },
        y: {
          position: "left",
          title: { display: true, text: "CapEx ($ billions)", color: pink, font: { weight: "600", size: 14 } },
          ticks: { callback: (v) => `$${v}B`, font: { size: 12 } },
          grid: { color: "rgba(232, 232, 236, 0.9)" },
        },
        y1: {
          position: "right",
          min: 0,
          max: 3.5,
          title: {
            display: true,
            text: "Annual productivity uplift (%)",
            color: blue,
            font: { weight: "600", size: 14 },
          },
          ticks: { callback: (v) => `${v}%`, font: { size: 12 } },
          grid: { drawOnChartArea: false },
        },
      },
    },
  });
})();
