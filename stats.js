var width = 960,
    height = 500;

var path = d3.geo.path();
path.radius = 5;

var svg = d3.select(".container").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("image")
    .attr("xlink:href", "./images/patent_map1.png")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", width)
    .attr("height", height);

d3.json("./patent_data/patents.json", function (data) {
    for (var i = 0; i < data.length; i++) {
        svg.append("path")
            .datum(data[i].collection)
            .attr("d", path)
            .style("fill", "FFD300");
    }
});

svg.selectAll("path")
            .data(features)
          .enter().append("path")
            .attr("d", function(d) {return d;});

svg.append("path")
            .datum(data[i].collection)
            .attr("d", path)
            .style("fill", "FFD300");