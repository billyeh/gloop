var width = 960,
    height = 500;

var path = d3.geo.path();

var svg = d3.select(".container").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("us.json", renderMap);

function renderMap(error, topology) {
  svg.selectAll("path")
      .data(topojson.feature(topology, topology.objects.counties).features)
    .enter().append("path")
      .attr("d", path);
}

d3.csv("patents_2010.csv", renderPatents);

function renderPatents(error, d) {
  var projection = d3.geo.albersUsa();
  svg.selectAll("circle")
      .data(d)
    .enter().append("circle")
      .attr("transform", function(d) {return "translate(" + projection([d.long,d.lat]) + ")";});
}
