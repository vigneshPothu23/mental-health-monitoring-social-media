function renderChart(labels, data) {
    const ctx = document.getElementById("emotionChart").getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Confidence %",
                data: data,
                backgroundColor: "#38bdf8"
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}
