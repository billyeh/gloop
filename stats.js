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

var untested =  {
                  "type": "FeatureCollection",
                  "features": [
                    {
                      "geometry": {
                        "type": "Point",
                        "coordinates": [
                          -98.516667,
                          31.283333
                        ]
                      },
                      "type": "Feature",
                      "properties": {
                        "color": "#FFD300",
                        "radius": "5"
                      }
                    }
                  ]
                }


var tested =  {"type": "FeatureCollection",
                "features": [
                  { "type": "Feature",
                    "geometry": {
                      "type": "LineString",
                      "coordinates": [
                        [-75.308372,39.856213], [-98.516667,31.283333]
                      ]
                    }
                  }
                ]
              }

svg.append("path")
    .datum(tested)
    .attr("d", path);

svg.append("path")
    .datum(untested)
    .attr("d", path)
    .style("fill", "#FFD300");
