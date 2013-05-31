var width = 960,
    height = 500;

var path = d3.geo.path();

var svg = d3.select(".container").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("us.json", renderMap);

function renderMap(error, topology) {
  svg.append("path")
      .datum(topojson.feature(topology, topology.objects.land))
      .attr("d", path)

  svg.append("path")
      .datum(topojson.mesh(topology, topology.objects.counties, function(a, b) { return a !== b && (a.id / 1000 | 0) === (b.id / 1000 | 0); }))
      .attr("d", path)
      .attr("class", "county-boundary");

  svg.append("path")
      .datum(topojson.mesh(topology, topology.objects.states, function(a, b) { return a !== b; }))
      .attr("d", path)
}

d3.csv("patents_2010.csv", renderPatents);

function renderPatents(error, d) {
  var projection = d3.geo.albersUsa();
  svg.selectAll("circle")
      .data(d)
    .enter().append("circle")
      .attr("r", 2)
      .style("fill", "rgba(0, 0, 255, .04")
      .attr("transform", function(d) {return "translate(" + projection([d.long, d.lat]) + ")";});
}
