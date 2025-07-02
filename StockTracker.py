from StockExntended import StockExtended
import pandas as pd
from tqdm import tqdm


class StockTracker:
    def __init__(self, symbols):
        self.stocks = [
            StockExtended(symbol) for symbol in tqdm(symbols, desc="Init Tracker")
        ]

    def get_all_info(self):
        """Returns basic info for all tracked stocks."""
        return [
            stock.get_info()
            for stock in tqdm(self.stocks, desc="Generating Dataframe..")
        ]

    def get_all_prices(self):
        """Returns current price of all stocks."""
        return {stock.symbol: stock.get_current_price() for stock in self.stocks}

    def to_dataframe(self):
        """Convert all stock info into a pandas DataFrame"""
        data = self.get_all_info()
        return pd.DataFrame(data)
