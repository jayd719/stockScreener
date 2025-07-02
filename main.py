from StockTracker import StockTracker
from functions import get_stock_list

tracker = StockTracker(get_stock_list("list.txt"))

df = tracker.to_dataframe()
df.to_csv("this.csv")
print(df)
