import json

file = "static/bezirksgrenzen.geojson"

def transform(feature):
    feature["properties"]["Gemeinde_schluessel"] = int(feature["properties"]["Gemeinde_schluessel"])
    return feature

with open(file, "r") as f:
    data = json.load(f)
    
data["features"] = [transform(feature) for feature in data["features"]]

with open(file, "w") as f:
    json.dump(data, f)