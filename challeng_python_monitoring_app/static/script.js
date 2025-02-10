document.addEventListener("DOMContentLoaded", function () {
    const cpuChart = new Chart(document.getElementById("cpuChart"), {
        type: "doughnut",
        data: {
            labels: ["Used", "Free"],
            datasets: [{
                data: [0, 100],
                backgroundColor: ["red", "lightgray"]
            }]
        },
        options: { responsive: true }
    });

    const memoryChart = new Chart(document.getElementById("memoryChart"), {
        type: "doughnut",
        data: {
            labels: ["Used", "Free"],
            datasets: [{
                data: [0, 100],
                backgroundColor: ["blue", "lightgray"]
            }]
        },
        options: { responsive: true }
    });

    function updateData() {
        fetch("/metrics").then(response => response.json()).then(data => {
            cpuChart.data.datasets[0].data = [data.cpu, 100 - data.cpu];
            memoryChart.data.datasets[0].data = [data.memory, 100 - data.memory];
            cpuChart.update();
            memoryChart.update();

            let tableBody = document.getElementById("process-table");
            tableBody.innerHTML = "";
            data.processes.forEach(proc => {
                let row = `<tr>
                    <td>${proc.pid}</td>
                    <td>${proc.name}</td>
                    <td>${proc.memory}%</td>
                    <td>${proc.cpu}%</td>
                    <td>${proc.threads}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        });
    }

    setInterval(updateData, 3000);
    updateData();
});
