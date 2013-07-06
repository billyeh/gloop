class FeatureCollectionTest:
  def __init__(this, feature_collection):
    this.collection = feature_collection
  def test(this):
    if (this.collection["type"] != "FeatureCollection"):
      print("Collection type should be FeatureCollection")
    if ("features" in this.collection and type(this.collection["features"]) != list):
      print("Collection features should be list")
    for f in this.collection["features"]:
      feature = FeatureTest(f)
      feature.test()

class FeatureTest:
  def __init__(this, f):
    this.feature = f
  def test(this):
    if ("type" not in this.feature or this.feature["type"] not in ["Point",
                                                                  "Multipoint",
                                                                  "LineString",
                                                                  "MultiLineString",
                                                                  "Polygon",
                                                                  "MultiPolygon",
                                                                  "GeometryCollection",
                                                                  "Feature",
                                                                  "FeatureCollection"]):
      print("Feature type should be one of the valid ones")
    if ("geometry" not in this.feature):
      print("Feature needs geometry")
      return
    if (type(this.feature["geometry"]) != dict):
      print("Feature's geometry needs to be an object")
      return
    if (this.feature["type"] != "GeometryCollection"):
      if ("coordinates" not in this.feature["geometry"]):
        print("Feature must have a coordinates array")
        return
      if (type(this.feature["geometry"]["coordinates"]) != list):
        print("Feature's coordinates must be a list")
        return

    if "type" not in this.feature["geometry"]:
      print("Geometry must have type")
    if this.feature["geometry"]["type"] == "Point":
      _PointTest(this.feature).test()
    if this.feature["geometry"]["type"] == "Multipoint":
      _MultipointTest(this.feature).test()
    if this.feature["geometry"]["type"] == "LineString":
      _LineStringTest(this.feature).test()
    if this.feature["geometry"]["type"] == "MultiLineString":
      _MultiLineStringTest(this.feature).test()


class _Feature:
  def __init__(this, f):
    this.feature = f
    this.coordinates = this.feature["geometry"]["coordinates"]

class _PointTest(_Feature):
  def test(this):
    _are_coordinates(this.coordinates)

class _MultipointTest(_Feature):
  def test(this):
    _is_coordinate_array(this.coordinates)

class _LineStringTest(_Feature):
  def test(this):
    _is_coordinate_array(this.coordinates)

class _MultiLineStringTest(_Feature):
  def test(this):
    for c in this.coordinates:
      _is_coordinate_array(c)

def _is_num(number):
  try:
    float(number)
    return True
  except ValueError:
    return False

def _are_coordinates(coordinates):
  if (len(coordinates) < 2):
    print("Point must have at least 2 coordinates")
  elif (not _is_num(coordinates[0]) and not _is_num(coordinates[1])):
    print("Point's first two coordinates should be numbers")

def _is_coordinate_array(coordinates):
  for c in coordinates:
    _are_coordinates(c)