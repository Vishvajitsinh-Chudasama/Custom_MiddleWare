document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('statusChart');
    const ctx = canvas.getContext('2d');

    const labels = JSON.parse(canvas.dataset.labels);
    const counts = JSON.parse(canvas.dataset.counts);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Number of Requests',
                data: counts,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
});
