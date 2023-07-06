import pandas as pd

diebstähle = pd.read_csv("data/Fahrraddiebstahl.csv", encoding="ansi")
plr = pd.read_csv("data/lor_planungsraeume_2021.csv", encoding="ansi")
bezirke = pd.read_csv("data/bezirksgrenzen.csv", encoding="ansi")
bezirke.rename(columns={"Gemeinde_schluessel": "BEZ"}, inplace=True)

print(plr.join(bezirke, on="BEZ", lsuffix="_plr", rsuffix="_bezirke"))
