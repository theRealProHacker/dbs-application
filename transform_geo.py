"""
Das Skript, um die bezirksgrenzen.geojson-Datei 
in die Form zu bringen, in der sie gerade ist.
"""

import json

file = "static/bezirksgrenzen.geojson"


with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)


for feature in data["features"]:
    props = feature["properties"]
    feature["id"] = int(props["Gemeinde_schluessel"])
    feature["Bezirk"] = props["Gemeinde_name"]
    del feature["properties"]
       

with open(file, "w", encoding="utf-8") as f:
    json.dump(data, f)