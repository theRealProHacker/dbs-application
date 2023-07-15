import json

filelor = "static/lor_planungsraeume_2021.geojson"

with open(filelor, "r", encoding="utf-8") as f:
    data2 = json.load(f)

for feature in data2["features"]: 
    props = feature["properties"]
    feature["PLR_ID"] = int(props["lor"])
    feature["Planungsraum"] = props["lor_name"]
    del feature["properties"]

with open(filelor, "w", encoding="utf-8") as f:
    json.dump(data2, f)