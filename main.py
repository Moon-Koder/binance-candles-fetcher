from src.candles_rest import get_candles
from src.candles_ws import start_candle_socket
from src.dataframe_manager import CandleDataFrame


def main():
    # 1. Get the most recent 5 candles using REST
    candles = get_candles("BTCUSDT", "1m", limit=20000)

    # 2. Create DataFrame
    df_manager = CandleDataFrame(candles)

    print("Initial DataFrame:")
    df_manager.print_dataframe()

    # 3. Function to receive the new candles
    def handle_candle(candle):
        df_manager.add_candle(candle)

    print("\nStarting WebSocket engine...\n")

    # 4. Start the WebSocket
    start_candle_socket("BTCUSDT", "1m", on_message=handle_candle)


if __name__ == "__main__":
    main()
