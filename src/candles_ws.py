import websocket
import json
from src.utils import normalize_candle


def start_candle_socket(symbol: str, interval: str, on_message):
    stream = f"{symbol.lower()}@kline_{interval}"
    url = f"wss://fstream.binance.com/ws/{stream}"

    def _on_message(ws, message):
        data = json.loads(message)
        candle = data["k"]

        if candle["x"]:  # closed candle
            normalized = normalize_candle(candle, "ws")
            on_message(normalized)

    ws = websocket.WebSocketApp(
        url=url,
        on_message=_on_message
    )

    ws.run_forever()
