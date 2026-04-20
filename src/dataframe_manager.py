import pandas as pd
from src.utils import timestamp_to_datetime


class CandleDataFrame:
    def __init__(self, candles: list):
        # Internal DataFrame WITHOUT display format
        self.df = pd.DataFrame(candles)

        # Ensure candles are in the correct order
        self.df = self.df.sort_values(by="open_time").reset_index(drop=True)

    # -----------------------------
    # CORE: add candles
    # -----------------------------
    def add_candle(self, candle: dict):
        # Avoid duplicates (open_time as a single key)
        if candle["open_time"] in self.df["open_time"].values:
            return

        # Add a new candle
        self.df = pd.concat(
            [self.df, pd.DataFrame([candle])],
            ignore_index=True
        )

        # Keep the time order
        self.df = self.df.sort_values(by="open_time").reset_index(drop=True)

        # Automatic print from the updated status
        print("\nNew candle added:")
        self.print_dataframe()

    # -----------------------------
    # VIEW: consistent format
    # -----------------------------
    def _format_df(self):
        df = self.df.copy()

        # Timestamp conversion → readable datetime
        df["open_time"] = df["open_time"].apply(timestamp_to_datetime)

        return df

    # -----------------------------
    # OUTPUT controlled
    # -----------------------------
    def print_dataframe(self, last_n: int = 2000):
        df = self._format_df()

        print(df.tail(last_n).to_string(index=False))

    # -----------------------------
    # (optional) Full access
    # -----------------------------
    def get_raw(self):
        return self.df

    # -----------------------------
    # (optional) formated access
    # -----------------------------
    def get_view(self):
        return self._format_df()
