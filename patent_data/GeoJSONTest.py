class FeatureCollectionTest:
  def __init__(self, feature_collection):
    self.collection = feature_collection
  def test(self):
    if (self.collection["type"] != "FeatureCollection"):
      print("Collection type should be FeatureCollection")
    if ("features" in self.collection and type(self.collection["features"]) != list):
      print("Collection features should be list")
    for f in self.collection["features"]:
      feature = FeatureTest(f)
      feature.test()

class FeatureTest:
  def __init__(self, f):
    self.feature = f
  def test(self):
    if ("type" not in self.feature or self.feature["type"] not in ["Point",
                                                                  "Multipoint",
                                                                  "LineString",
                                                                  "MultiLineString",
                                                                  "Polygon",
                                                                  "MultiPolygon",
                                                                  "GeometryCollection",
                                                                  "Feature",
                                                                  "FeatureCollection"]):
      print("Feature type should be one of the valid ones")
    if ("geometry" not in self.feature):
      print("Feature needs geometry")
      return
    if (type(self.feature["geometry"]) != dict):
      print("Feature's geometry needs to be an object")
      return
    if (self.feature["type"] != "GeometryCollection"):
      if ("coordinates" not in self.feature["geometry"]):
        print("Feature must have a coordinates array")
        return
      if (type(self.feature["geometry"]["coordinates"]) != list):
        print("Feature's coordinates must be a list")
        return

    if "type" not in self.feature["geometry"]:
      print("Geometry must have type")
    if self.feature["geometry"]["type"] == "Point":
      _PointTest(self.feature).test()
    if self.feature["geometry"]["type"] == "Multipoint":
      _MultipointTest(self.feature).test()
    if self.feature["geometry"]["type"] == "LineString":
      _LineStringTest(self.feature).test()
    if self.feature["geometry"]["type"] == "MultiLineString":
      _MultiLineStringTest(self.feature).test()


class _Feature:
  def __init__(self, f):
    self.feature = f
    self.coordinates = self.feature["geometry"]["coordinates"]

class _PointTest(_Feature):
  def test(self):
    _are_coordinates(self.coordinates)

class _MultipointTest(_Feature):
  def test(self):
    _is_coordinate_array(self.coordinates)

class _LineStringTest(_Feature):
  def test(self):
    _is_coordinate_array(self.coordinates)

class _MultiLineStringTest(_Feature):
  def test(self):
    for c in self.coordinates:
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