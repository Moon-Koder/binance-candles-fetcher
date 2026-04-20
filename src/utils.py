from datetime import datetime


def timestamp_to_datetime(ts: int):
    return datetime.fromtimestamp(ts / 1000)


def normalize_candle(data: dict, source: str = "rest"):
    if source == "rest":
        return {
            "open_time": data[0],
            "open": float(data[1]),
            "high": float(data[2]),
            "low": float(data[3]),
            "close": float(data[4]),
            "volume": float(data[5])
        }

    elif source == "ws":
        return {
            "open_time": data["t"],
            "open": float(data["o"]),
            "high": float(data["h"]),
            "low": float(data["l"]),
            "close": float(data["c"]),
            "volume": float(data["v"])
        }
