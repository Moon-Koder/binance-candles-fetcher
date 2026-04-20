from src.client import BinanceClient
from src.utils import normalize_candle
import pandas as pd
import time

client = BinanceClient()

BINANCE_LIMIT = 1500


def get_candles(symbol: str, interval: str, limit: int = 500):
    all_candles = []
    end_time = None

    while len(all_candles) < limit:
        remaining = limit - len(all_candles)
        fetch_limit = min(BINANCE_LIMIT, remaining)

        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": fetch_limit
        }

        if end_time:
            params["endTime"] = end_time

        data = client.get("/fapi/v1/klines", params)

        if not data:
            break

        # Candles normalization
        candles = [normalize_candle(c, "rest") for c in data]

        # Add to the total list
        all_candles.extend(candles)

        # Prepare the next page (go back in time)
        first_open_time = candles[0]["open_time"]
        end_time = first_open_time - 1

        # Safe API sleep (dynamic)
        time.sleep(0.05 if fetch_limit < 500 else 0.1)

        # Extra security
        if len(data) < fetch_limit:
            break

    # Final clean with DataFrame
    df = pd.DataFrame(all_candles)

    # Remover duplicates
    df = df.drop_duplicates(subset=["open_time"])

    # Order correctly
    df = df.sort_values(by="open_time").reset_index(drop=True)

    # Ensure the exact number of candles
    if len(df) > limit:
        df = df.tail(limit)

    return df.to_dict("records")
