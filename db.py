import pandas as pd

def accidents_by_district() -> list[dict[str, str]]:
    return pd.DataFrame(
        [
            {"id":1,"name": "Mitte", "accidents": 123},
            {"id":2,"name": "Friedrichshain-Kreuzberg", "accidents": 456},
            {"id":3,"name": "Pankow", "accidents": 789},
            {"id":4,"name": "Charlottenburg-Wilmersdorf", "accidents": 123},
            {"id":5,"name": "Spandau", "accidents": 123},
            {"id":6,"name": "Steglitz-Zehlendorf", "accidents": 123},
            {"id":7,"name": "Tempelhof-Schöneberg", "accidents": 123},
            {"id":8,"name": "Neukölln", "accidents": 123},
            {"id":9,"name": "Treptow-Köpenick", "accidents": 123},
            {"id":10,"name":"Marzahn-Hellersdorf", "accidents": 123},
            {"id":11,"name": "Lichtenberg", "accidents": 123},
            {"id":12,"name": "Reinickendorf", "accidents": 123},
        ]
    )


if __name__ == "__main__":
    print(accidents_by_district())