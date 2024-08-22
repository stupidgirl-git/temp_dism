window.onload = function() {
    // Make the AJAX request
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            // Populate the table with the received data
            const tableBody = document.getElementById('table-body');
            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${row.column1}</td>
                    <td>${row.column2}</td>
                    <td>${row.column3}</td>
                `;
                tableBody.appendChild(tr);
            });
        })
        .catch(error => console.error(error));
};