from src.candles_ws import start_candle_socket


def handle_candle(candle):
    print("New closed candle:", candle)


start_candle_socket("BTCUSDT", "1m", handle_candle)
