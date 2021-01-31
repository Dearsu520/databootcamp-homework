//text box popup for the mouseover event
var textBox = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

//load csv data
d3.csv("assets/data/data.csv").then((data) => {
    console.log(data);

    //Set up the dimensions
    var margin = {top: 10, right: 30, bottom: 120, left: 120};
    var width = 1000 - margin.left - margin.right;
    var height = 600 - margin.top - margin.bottom;

    //x axis boundries
    var xAxisValues = {
        income: {min: 35000, max: 80000},
        age: {min: 28, max: 48},
        poverty: {min: 8, max: 24}
    }

    //y axis boundries
    var yAxisValues = {
        obesity: {min: 18, max: 42},
        smokes: {min: 8, max: 28},
        healthcare: {min: -2, max: 30}
    }

    function loadPlot(xlabel, ylabel){
        //clear the scatter plot
        d3.select("#scatter").html("");

        //Add svg scattered
        var svg = d3.select("#scatter")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        
        //x-axis and labels
        var x = d3.scaleLinear()
            .domain([xAxisValues[xlabel].min, xAxisValues[xlabel].max])
            .range([0, width]);
        
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));
        
        svg.append("text")
            .attr("transform", 
                "translate(" + (width / 2) + " ," + (height + margin.top + 40) + ")")
            .style("text-anchor", "middle")
            .style("font-family", "Time New Roman")
            .style("fill", xlabel == "poverty" ? "pink":"black")
            .style("cursor", "pointer")
            .text("In Poverty(%)")
            .on("click", () => loadPlot("poverty", ylabel));
        
        svg.append("text")
            .attr("transform", 
                "translate(" + (width / 2) + " ," + (height + margin.top + 60) + ")")
            .style("text-anchor", "middle")
            .style("font-family", "Time New Roman")
            .style("fill", xlabel == "age" ? "pink":"black")
            .style("cursor", "pointer")
            .text("Age (Median)")
            .on("click", () => loadPlot("age", ylabel));
        
        svg.append("text")
            .attr("transform", 
                "translate(" + (width / 2) + " ," + (height + margin.top + 80) + ")")
            .style("text-anchor", "middle")
            .style("font-family", "Time New Roman")
            .style("fill", xlabel == "income" ? "pink":"black")
            .style("cursor", "pointer")
            .text("Household Income (Median)")
            .on("click", () => loadPlot("income", ylabel));

        //y-axis and labels
        var y = d3.scaleLinear()
            .domain([yAxisValues[ylabel].max, yAxisValues[ylabel].min])
            .range([10, height]);
        
        svg.append("g")
            .call(d3.axisLeft(y));

        svg.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left + 40)
            .attr("x", 0 - (height / 2))
            .attr("dy", "1em")
            .style("text-anchor", "middle")
            .style("font-family", "Time New Roman")
            .style("fill", ylabel == "healthcare" ? "pink":"black")
            .style("cursor", "pointer")
            .text("Lacks Healthcare (%)")
            .on("click", () => loadPlot(xlabel, "healthcare"));
        
        svg.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left + 20)
            .attr("x", 0 - (height / 2))
            .attr("dy", "1em")
            .style("text-anchor", "middle")
            .style("font-family", "Time New Roman")
            .style("fill", ylabel == "smokes" ? "pink":"black")
            .style("cursor", "pointer")
            .text("Smokes (%)")
            .on("click", () => loadPlot(xlabel, "smokes"));
        
        svg.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left)
            .attr("x", 0 - (height / 2))
            .attr("dy", "1em")
            .style("text-anchor", "middle")
            .style("font-family", "Time New Roman")
            .style("fill", ylabel == "obesity" ? "pink":"black")
            .style("cursor", "pointer")
            .text("Obesse (%)")
            .on("click", () => loadPlot(xlabel, "obesity"));
        
        //populate circles    
        var points = svg.append("g")
            .selectAll("circle")
            .data(data)
            .enter();

        //append dots to the svg
        points.append("circle")
            .attr("cx", (d) => x(d[xlabel]))
            .attr("cy", (d) => y(d[ylabel]))
            .attr("r", 12)
            .style("fill", "pink")
            .style("cursor", "pointer")
            .on("mouseover", (d) => { //mouseover event
                textBox 
                    .style("opacity", .9)
                    .style("text-align", "center")
                    .style("background-color", "lightgrey")
                    .style("padding", "10px");

                textBox.html("<text>" + d.state + "</text></br>" 
                    + "<text>Poverty: " + d.poverty + "%</text></br>"
                    + "<text>Obesity: " + d.obesity + "%</text>")
                .style("left", d3.event.pageX + "px")
                .style("top", d3.event.pageY + "px");
            });
        //add states abbr to each corresponding circle
        points.append("text")
            .attr("dx", (d) => x(d[xlabel]))
            .attr("dy", (d) => y(d[ylabel]) + 3)
            .style("font-size", "x-small")
            .style("text-anchor", "middle")
            .style("fill", "white")
            .text((d) => d.abbr);
    }

    loadPlot("poverty", "healthcare");
});