function getdf() {
    var filename = "{{ file_name | safe }}";
    var url = '/'+filename+'/api/df';
    $.ajax({
        type: "GET",
        url: url,
        dataType: "json",

        success: function(response) {
            if (response !== null && response !== undefined) {
                var headers = response.df_headers;
                console.log(headers);

                var table = document.createElement("myTable");
                table.id = "myTable";
                document.body.appendChild(table);

                var tr = document.createElement("tr");
                tr.id = "tableHead";
                table.appendChild(tr);
                for (var i = 0; i < headers.length; i++) {
                    var th = document.createElement("th");
                    th.textContent = headers[i];
                    tr.appendChild(th);
                    console.log(tr);
                }

                var tableBody = document.createElement("tbody");
                tableBody.innerHTML = ""; // Clear existing content

                for (var i = 0; i < response.df.length; i++) {
                    var tr = document.createElement("tr");
                    var keys = headers;
                    console.log(keys);
                    for (var j = 0; j < keys.length; j++) {
                        var key = keys[j];
                        console.log(key);
                        var td = document.createElement("td");
                        td.textContent = response.df[i][key]; 
                        console.log(td);
                        tr.appendChild(td);
                        console.log(tr);
                    }
                    tableBody.appendChild(tr);
                    
                    table.appendChild(tableBody);
                }
            } else {
                console.error("Error: df is null or undefined");
            }
        },
        error: function(xhr, status, error) {
            console.error("Error: " + error);
        }
    });
}