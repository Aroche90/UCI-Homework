// from data.js
var tableData = data;

// get the table reference
var tbody = d3.select("tbody");

// build table with all sightings
tableData.forEach(function(allSightings) {
    var row = tbody.append("tr");
    Object.entries(allSightings).forEach(function([key, value]) {
      // append a cell to the rows 
      var cell = row.append("td");
      cell.text(value);
    });
  });

// select "Filter Table" button
var filterButton = d3.select("#filter-btn");

// handle click for the "Filter Table" button
filterButton.on("click", function() {

// event listener to prevent the page from refreshing
d3.event.preventDefault();

// select input element and get value property
var date = d3.select("#datetime").property("value");

// create filteredData from tableData
var filteredData = tableData.filter(function (sighting) {
return sighting.datetime === date;
});

// clear the data in tbody
tbody.text('');

// populate tbody with rows and cells needed for filteredData
filteredData.forEach(record => { 

// assign new appended row into a variable for later use
var row = tbody.append('tr');

// loop through each record
Object.entries(record).forEach( ([key, value]) => {

// append a 'td' element to the row with the value of each key in the object
row.append('td').text(value);
  });
 });
});





