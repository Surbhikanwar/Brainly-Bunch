const burstCtx = document.getElementById('reviewBurst').getContext('2d');
new Chart(burstCtx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [{
            label: 'Review Burst Patterns',
            data: [7, 6, 7, 8, 6, 7, 5],
            backgroundColor: '#10b981'
        }]
    }
});

const genuineCtx = document.getElementById('genuineVsFake').getContext('2d');
new Chart(genuineCtx, {
    type: 'bar',
    data: {
        labels: ['Genuine', 'Fake'],
        datasets: [{
            label: 'Review Distribution',
            data: [12, 8],
            backgroundColor: ['#10b981', '#ef4444']
        }]
    }
});
