import pandas as pd
import random
import sqlalchemy as sa
from sqlalchemy import text

engine = sa.create_engine('postgresql://postgres:12345@localhost:5432/biketheft_berlin')

def accidents_by_district() -> list[dict[str, str]]:
    return pd.DataFrame(
        [
            {"id":x+1, "Unfälle": random.randint(0, 1000)} for x in range(12)
        ]
    )

def accidents_by_district():
    with engine.connect() as conn:
        df = pd.read_sql("""
                        SELECT bg.gemeinde_schluessel AS id, COUNT(fd.LOR) AS Unfälle
                        FROM bezirksgrenze bg
                        JOIN lor_planungsraueme lp ON bg.gemeinde_schluessel = lp.BEZ
                        JOIN fahrraddiebstahl fd ON lp.PLR_ID = fd.LOR
                        GROUP BY bg.gemeinde_schluessel;""", conn)
        df.rename(columns={"id": "id", "unfälle": "Unfälle"}, inplace=True)
        return df

def accidents_by_lor():
    with engine.connect() as conn:
        df = pd.read_sql("""
                        SELECT LOR, COUNT(*) AS Unfälle
                        FROM fahrraddiebstahl
                        WHERE Versuch = '0'
                        GROUP BY LOR;
                        """, conn)
        return df


if __name__ == "__main__":
    print(accidents_by_district())