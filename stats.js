var width = 960,
    height = 500;

var path = d3.geo.path();

var svg = d3.select(".container").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("image")
    .attr("xlink:href", "./images/patent_ma.png")
    .attr("x", -60)
    .attr("y", 0)
    .attr("width", width)
    .attr("height", height);

svg.selectAll("path")
    .data(tested)
  .enter().append("path")
    .attr("d", function(d) {return path(d.collection);});
    
svg.append("path")
    .datum(untested)
    .attr("d", path)
    .style("fill", "#FFD300");