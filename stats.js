var width = 960,
    height = 500;

var path = d3.geo.path();

var svg = d3.select(".container").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("image")
    .attr("xlink:href", "./images/patent_map.png")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", width)
    .attr("height", height);
