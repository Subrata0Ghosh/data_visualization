// script.js
document.addEventListener('DOMContentLoaded', function() {
    fetchData();
});

function fetchData() {
    fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        drawChart(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

function drawChart(data) {
    // D3.js code to render visualization
}
