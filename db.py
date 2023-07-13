from functools import cache

import pandas as pd
import sqlalchemy as sa

engine = sa.create_engine('postgresql://postgres:dbs23@localhost:5432/biketheft_berlin')

@cache
def accidents_by_district():
    with engine.connect() as conn:
        df = pd.read_sql("""
                        SELECT bg.gemeinde_schluessel AS id, COUNT(fd.LOR) AS Diebstähle
                        FROM bezirksgrenze bg
                        JOIN lor_planungsraueme lp ON bg.gemeinde_schluessel = lp.BEZ
                        JOIN fahrraddiebstahl fd ON lp.PLR_ID = fd.LOR
                        GROUP BY bg.gemeinde_schluessel;""", conn)
    df.rename(columns={"diebstähle": "Diebstähle"}, inplace=True)
    return df

@cache
def accidents_by_lor():
    with engine.connect() as conn:
        df = pd.read_sql("""
                        SELECT LOR, COUNT(*) AS Unfälle
                        FROM fahrraddiebstahl
                        WHERE Versuch = '0'
                        GROUP BY LOR;
                        """, conn)
    return df

@cache
def all_accidents():
    with engine.connect() as conn:
        df = pd.read_sql("""
                        SELECT F.tatzeit_anfang_datum AS Datum, B.gemeinde_namen AS Bezirk, L.plr_name AS Planungsraum, F.schadeshoehe AS Schaden, F.art_des_fahrrads AS Fahrradtyp
                        FROM fahrraddiebstahl F, lor_planungsraueme L, bezirksgrenze B
                        WHERE F.lor = L.plr_id AND L.bez = B.gemeinde_schluessel
                        """, conn)
    return df


if __name__ == "__main__":
    print(accidents_by_district())