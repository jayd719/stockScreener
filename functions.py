def get_stock_list(filepath):
    stock_list = []
    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            stock_list = [line.strip().upper() for line in fh if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found → {filepath}")
    except Exception as e:
        print(f"Error reading stock list: {e}")
    return stock_list
