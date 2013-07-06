import json, GeoJSONTest

collections = [c["collection"] for c in json.load(open('patents.json'))]
for c in collections:
  collection = GeoJSONTest.FeatureCollectionTest(c)
  collection.test()