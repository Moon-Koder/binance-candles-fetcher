from src.candles_rest import get_candles


candles = get_candles("BTCUSDT", "5m")
print(candles[-1])
