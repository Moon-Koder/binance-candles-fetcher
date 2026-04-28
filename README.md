# Binance Candles Fetcher

A lightweight Python module to fetch and stream candlestick data from Binance using both REST and WebSocket APIs.

## 🚀 Features
📊 Fetch historical candles with pagination (beyond API limits)
⚡ Real-time candle updates via WebSocket
🧹 Automatic deduplication and ordering
🎯 Exact candle count control
🐼 Integrated with Pandas DataFrame
🛡️ Rate-limit friendly (dynamic request throttling)

## 🧠 Overview
This project combines two data sources:

REST API → for historical data
WebSocket → for real-time updates

The result is a continuously updating DataFrame that can be used for:

backtesting strategies
real-time trading systems
data analysis pipelines

## ⚙️ Installation
git clone https://github.com/Moon-Koder/binance-candles-fetcher.git
cd binance-candles-fetcher

pip install -r requirements.txt

## ▶️ Usage
Fetch historical candles
from src.candles_rest import get_candles

candles = get_candles("BTCUSDT", "1m", limit=2000)
Start real-time stream
from src.candles_ws import start_candle_socket

def handle_candle(candle):
    print(candle)

start_candle_socket("BTCUSDT", "1m", on_message=handle_candle)
DataFrame integration
from src.dataframe_manager import CandleDataFrame

df_manager = CandleDataFrame(candles)

def handle_candle(candle):
    df_manager.add_candle(candle)

start_candle_socket("BTCUSDT", "1m", on_message=handle_candle)

## 📊 Example Output
open_time           open    high     low   close   volume
2026-04-19 14:23    75510   75520   75500   75515   12.34
2026-04-19 14:24    75515   75525   75510   75520    9.87
...

## 🛡️ Notes
No API key required (public endpoints only)
Designed to avoid rate limits
Ensures data consistency (no duplicates, correct ordering)

## 👨‍💻 Author
MoonKoder

## ⭐ Why this project?

This project was built to explore:

real-time data systems
trading infrastructure
clean modular Python design
