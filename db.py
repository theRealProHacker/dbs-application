import pandas as pd
import random

def accidents_by_district() -> list[dict[str, str]]:
    return pd.DataFrame(
        [
            {"id":x+1, "Unfälle": random.randint(0, 1000)} for x in range(12)
        ]
    )


if __name__ == "__main__":
    print(accidents_by_district())