var width = 960,
    height = 500;

var path = d3.geo.path();
var projection = d3.geo.albersUsa();

var svg = d3.select('.container').append('svg')
      .attr('width', width)
      .attr('height', height);

svg.append('image')
      .attr('xlink:href', './images/patent_map.png')
      .attr('x', -65)
      .attr('y', 10)
      .attr('width', width)
      .attr('height', height);

d3.json('./patent_data/points.json', function (data) {
  svg.selectAll('circle')
        .data(data.features, function(d) {return d.patent;})
      .enter().append('circle')
        .attr('r', function(d) {return d.radius * 2;})
        .style('fill', '#FFD300')
        .style('stroke', '#222')
        .attr('class', function(d) {return d.patent;})
        .attr('transform', function(d) {return 'translate(' + coordinates(d.geometry.coordinates) + ')';});
  d3.select('#patent-header')
        .selectAll('span')
        .data(data.features)
      .enter().append('span')
        .attr()
        .text(function(d, i) {return '' + (i + 1) + '. ' + d.patent;});
});

d3.json('./patent_data/patents.json', function (data) {
  for (var i = 0; i < data.length; i++) {
    var collection = data[i].collection;
    var features = collection.features;
    for (var j = 0; j < features.length; j++) {
      if (features[j].geometry.type === 'Point') {
        svg.append('circle')
            .attr('r', 3)
            .style('fill', '#FFD300')
            .attr('transform', function(d) {return 'translate(' + coordinates(features[j].geometry.coordinates) + ')';});
      }
      else if (features[j].geometry.type === 'LineString') {
        svg.append('path')
            .attr('d', path(features[j]))
            .style('stroke', '#FFD300');
      }
    }
  }
});

function coordinates(c) {
  if (c !== null && projection(c) !== null) {
    return projection(c);
  }
  return '-20,' + height / 2;
}