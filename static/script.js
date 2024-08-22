window.onload = function() {
    // Make the AJAX request
    fetch('/database/api/data')
        .then(response => response.json())
        .then(data => {
            // Populate the table with the received data
            const tableBody = document.getElementById('data_of_database-body');
            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${row.Name}</td>
                    <td>${row.Category}</td>
                    <td>${row.From}</td>
                    <td>${row.To}</td>
                    <td>${row.Frequency}</td>
                    <td>${row.Links}</td>
                `;
                tableBody.appendChild(tr);
            });
        })
        .catch(error => console.error(error));
};