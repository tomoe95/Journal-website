// Set today's date
document.getElementById('today-date').innerText = new Date().toLocaleDateString();


document.addEventListener("DOMContentLoaded", () => {
    const ctx_weekly = document.getElementById('weekly-chart').getContext('2d');
    const ctx_monthly = document.getElementById('monthly-chart').getContext('2d');

    const weeklyChart = new Chart(ctx_weekly, {
        type: 'doughnut', // Specify chart type
        data: {
            labels: ['Red', 'Blue', 'Yellow'], // Labels for chart segments
            datasets: [{
                label: 'My Dataset',
                data: [300, 50, 100], // Values for each segment
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top', // Position of the legend
                },
            }
        }
    });

    const monthlyChart = new Chart(ctx_monthly, {
        type: 'doughnut', // Specify chart type
        data: {
            labels: ['Red', 'Blue', 'Yellow'], // Labels for chart segments
            datasets: [{
                label: 'My Dataset',
                data: [300, 50, 100], // Values for each segment
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top', // Position of the legend
                },
            }
        }
    });
});
