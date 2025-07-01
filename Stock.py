import yfinance as yf


class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        try:
            self.ticker = yf.Ticker(self.symbol)
        except Exception as e:
            raise ValueError(f"Failed to initialize stock '{self.symbol}': {e}")

    def get_current_price(self):
        try:
            data = self.ticker.history(period="1d", interval="1m")
            if not data.empty:
                return data["Close"].iloc[-1]
            return None
        except Exception as e:
            print(f"[{self.symbol}] Error getting current price: {e}")
            return None

    def get_history(self, period="1mo", interval="1d"):
        try:
            return self.ticker.history(period=period, interval=interval)
        except Exception as e:
            print(f"[{self.symbol}] Error fetching history: {e}")
            return None

    def get_dividends(self):
        try:
            return self.ticker.dividends
        except Exception as e:
            print(f"[{self.symbol}] Error fetching dividends: {e}")
            return None

    def get_recommendations(self):
        try:
            return self.ticker.recommendations
        except Exception as e:
            print(f"[{self.symbol}] Error fetching recommendations: {e}")
            return None
