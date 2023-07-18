"""
Das Skript, um die bezirksgrenzen.geojson-Datei 
in die Form zu bringen, in der sie gerade ist.
"""

import json

file = "static/bezirksgrenzen.geojson"
filelor = "static/lor_planungsraeume_2021.geojson"

#Bringt geojson-Datei mit Bezirken in Form

with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)


for feature in data["features"]:
    props = feature["properties"]
    feature["id"] = int(props["Gemeinde_schluessel"])
    feature["Bezirk"] = props["Gemeinde_name"]
    del feature["properties"]
       

with open(file, "w", encoding="utf-8") as f:
    json.dump(data, f)

#Bringt geojson-Datei mit Planungsraeumen in Form

with open(filelor, "r", encoding="utf-8") as f:
    data2 = json.load(f)

for feature in data2["features"]: 
    props = feature["properties"]
    feature["PLR_ID"] = int(props["lor"])
    feature["Planungsraum"] = props["lor_name"]
    del feature["properties"]

with open(filelor, "w", encoding="utf-8") as f:
    json.dump(data2, f)