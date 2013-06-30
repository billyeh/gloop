import sqlite3, json

full = sqlite3.connect("/home/billyeh/workspace/patentwork/2013_data/full_disambiguation.sqlite3")
patdesc = sqlite3.connect("/home/billyeh/workspace/patentwork/2013_data/patdesc.sqlite3")
citations = sqlite3.connect("/home/billyeh/workspace/patentwork/2013_data/citations_and_refs_mar262013.sqlite3")

top_patents = [7663607,
               7674650,
               7665646,
               7680184,
               7732819,
               7657297,
               7654956,
               7665051,
               7711402,
               7770144]

patents = []
points = {}
points["type"] = "FeatureCollection"
points["features"] = []
link = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=1&p=1&f=G&l=50&d=PTXT&S1=7663607.PN.&OS=pn/"

for top_patent in top_patents:
  current = {}
  current["patent"] = top_patent
  row = patdesc.execute("SELECT Title FROM patdesc WHERE patent=?", ['0' + str(top_patent)]).fetchone()
  current["title"] = row[0]
  row = full.execute("SELECT Longitude, Latitude, City, Country FROM invpat WHERE patent=?", ['0' + str(top_patent)]).fetchone()
  current["location"] = [row[0], row[1]]
  current["city"] = row[2]
  current["country"] = row[3]
  current["link"] = link + str(top_patent)

  current["collection"] = {}
  current["collection"]["type"] = "FeatureCollection"
  current["collection"]["features"] = []

  point = {}
  point["patent"] = top_patent
  point["type"] = "Feature"
  point["geometry"] = {}
  point["geometry"]["type"] = "Point"
  point["geometry"]["coordinates"] = current["location"]
  point["properties"] = {}
  point["properties"]["color"] = "#FFD300"

  cites = []
  for row in citations.execute("SELECT ref FROM reffedby WHERE patent=?", [str(top_patent)]):
    cites.append(row[0])
  for cite in cites:
    row = full.execute("SELECT Longitude, Latitude FROM invpat WHERE patent=?", [cite]).fetchone()
    if row[0] and row[1]:
      feature = {}
      feature["type"] = "Feature"
      feature["geometry"] = {}
      feature["geometry"]["type"] = "LineString"
      feature["geometry"]["coordinates"] = [[row[0], row[1]], current["location"]]
      feature["properties"] = {}
      feature["properties"]["citation"] = cite
      current["collection"]["features"].append(feature)
      feature = {}
      feature["type"] = "Feature"
      feature["geometry"] = {}
      feature["geometry"]["type"] = "Point"
      feature["geometry"]["coordinates"] = [row[0], row[1]]
      feature["properties"] = {}
      feature["properties"]["color"] = "#FFD300"
      feature["properties"]["radius"] = 2
      current["collection"]["features"].append(feature)

  point["radius"] = round(len(cites) / 20)
  points["features"].append(point)
  patents.append(current)

open('patents.json', 'w').write(json.dumps(patents, indent=2, separators=(',', ': ')))
open('points.json', 'w').write(json.dumps(points, indent=2, separators=(',', ': ')))