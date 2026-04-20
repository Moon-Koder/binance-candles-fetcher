from src.candles_rest import get_candles


def test_get_candles_returns_list():
    candles = get_candles("BTCUSDT", "1m", limit=5)
    assert isinstance(candles, list)


def test_candle_structure():
    candles = get_candles("BTCUSDT", "1m", limit=1)
    candle = candles[0]

    expected_keys = {"open", "high", "low", "close", "volume"}

    assert expected_keys.issubset(candle.keys())
