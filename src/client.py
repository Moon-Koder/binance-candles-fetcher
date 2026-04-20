import requests


BASE_URL = "https://fapi.binance.com"


class BinanceClient:
    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint: str, params: dict = None):
        url = BASE_URL + endpoint
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
