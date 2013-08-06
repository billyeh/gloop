var width = 960,
    height = 500;

var path = d3.geo.path();
var projection = d3.geo.albersUsa();

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
              .style("fill", "#FFD300");
    }
});
d3.json("./patent_data/points.json", function (data) {
    svg.selectAll("circle")
          .data(data.features)
        .enter().append("circle")
          .attr("r", function(d) {return d.radius * 2;})
          .style("fill", "#FFD300")
          .style("stroke", "#222")
          .attr("class", function(d) {return d.patent;})
          .attr("transform", function(d) {return "translate(" + projection(d.geometry.coordinates) + ")";});
    d3.select(".container")
          .selectAll("p")
          .data(data.features)
        .enter().append("p")
          .text(function(d) {return "Patent " + d.patent;});
});
/*
svg.selectAll("path")
            .data(features)
          .enter().append("path")
            .attr("d", function(d) {return d;});

svg.append("path")
            .datum(data[i].collection)
            .attr("d", path)
            .style("fill", "FFD300");
*/