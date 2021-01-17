// from data.js
var tableData = data;

tbody = d3.select("tbody");

function resetTable() {
    tbody.html(""); //Clear the table

    // populate the html table with data
    tableData.forEach((data, idx) => {
        var row = tbody.append("tr");

        Object.entries(data).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });

    d3.select("#datetime").property("value", "");
    d3.select("#city").property("value", "");
    d3.select("#state").property("value", "");
    d3.select("#country").property("value", "");
    d3.select("#shape").property("value", "");
}

resetTable(); //Reset the table upon loading the page

//Function to handle the click of the filter botton
function handleFilterClick(event){
    d3.event.preventDefault(); //prevent page reload

    // obtain datetime value
    var datetime = d3.select("#datetime").property("value");
    var city = d3.select("#city").property("value");
    var state = d3.select("#state").property("value");
    var country = d3.select("#country").property("value");
    var shape = d3.select("#shape").property("value"); 

    var filterData = tableData;

    if (datetime) { //The datetime field is not empty
        filterData = filterData.filter((row) => row.datetime === datetime);
    }
    if (city) { //The city field is not empty
        filterData = filterData.filter((row) => row.city === city);
    }
    if (state) { //The state field is not empty
        filterData = filterData.filter((row) => row.state === state);
    }
    if (country) { //The country field is not empty
        filterData = filterData.filter((row) => row.country === country);
    }
    if (shape) { ////The shape
        filterData = filterData.filter((row) => row.shape === shape);
    }
    tbody.html(""); //clear table

    filterData.forEach((data, idx) => {
        var row = tbody.append("tr");

        Object.entries(data).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });
}

// Function to handle reset table
function handleResetClick(event) {
    d3.event.preventDefault();
    resetTable();
}

d3.selectAll("#filter-btn").on("click", handleFilterClick);
d3.selectAll("#reset-btn").on("click", handleResetClick);
