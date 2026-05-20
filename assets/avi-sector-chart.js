/**
 * AVI by sector — horizontal bar chart (top sectors by AVI %).
 */
(function () {
  const canvas = document.getElementById("vs-avi-sector-chart");
  if (!canvas || typeof Chart === "undefined") return;

  const labels = [
    "Finance back-office",
    "Marketing creative",
    "Mfg. lighthouses",
    "Legal doc review",
    "Software dev.",
    "Consulting",
    "TMT IT",
    "Customer service",
    "Government",
    "Education",
  ];
  const avi = [28.6, 25.5, 24.8, 24.6, 21.6, 20.5, 17.8, 13.4, 9.3, 7.4];

  const colors = avi.map((v) =>
    v >= 25 ? "#FF005E" : v >= 15 ? "#FF669D" : "#FFD1E0"
  );

  new Chart(canvas, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "AVI (%)",
          data: avi,
          backgroundColor: colors,
          borderRadius: 4,
          borderSkipped: false,
        },
      ],
    },
    options: {
      indexAxis: "y",
      responsive: true,
      maintainAspectRatio: true,
      aspectRatio: 1.35,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label(ctx) {
              return ` AVI: ${ctx.parsed.x}%`;
            },
          },
        },
        annotation: {},
      },
      scales: {
        x: {
          min: 0,
          max: 32,
          title: { display: true, text: "AI Value Index (AVI) %" },
          ticks: { callback: (v) => `${v}%` },
          grid: { color: "rgba(232, 232, 236, 0.9)" },
        },
        y: {
          grid: { display: false },
          ticks: { font: { size: 11 } },
        },
      },
    },
  });
})();
