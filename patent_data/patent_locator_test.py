import json, GeoJSONTest

patents_test = [c["collection"] for c in json.load(open('patents.json'))]
for c in patents_test:
  collection = GeoJSONTest.FeatureCollectionTest(c)
  collection.test()
points_test = GeoJSONTest.FeatureCollectionTest(json.load(open('points.json')))
points_test.test()
