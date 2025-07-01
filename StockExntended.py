from Stock import Stock


class StockExtended(Stock):
    def __init__(self, symbol: str):
        super().__init__(symbol)

    def get_info(self):
        try:
            info = self.ticker.info

            return {
                # === Identity ===
                "Company Name": info.get("longName") or info.get("shortName", "N/A"),
                "Symbol": self.symbol,
                "Exchange": info.get("exchange", "N/A"),
                "Currency": info.get("currency", "N/A"),
                "Country": info.get("country", "N/A"),
                "Sector": info.get("sector", "N/A"),
                "Industry": info.get("industry", "N/A"),
                "Website": info.get("website", "N/A"),
                # === Employees & Ownership ===
                "Full-Time Employees": info.get("fullTimeEmployees", "N/A"),
                "Insider Ownership (%)": (
                    round(info.get("heldPercentInsiders", 0) * 100, 2)
                    if info.get("heldPercentInsiders")
                    else "N/A"
                ),
                "Institutional Ownership (%)": (
                    round(info.get("heldPercentInstitutions", 0) * 100, 2)
                    if info.get("heldPercentInstitutions")
                    else "N/A"
                ),
                # === Valuation ===
                "Market Cap ($B)": (
                    round(info.get("marketCap", 0) / 1e9, 2)
                    if info.get("marketCap")
                    else "N/A"
                ),
                "Enterprise Value ($B)": (
                    round(info.get("enterpriseValue", 0) / 1e9, 2)
                    if info.get("enterpriseValue")
                    else "N/A"
                ),
                "Shares Outstanding (B)": (
                    round(info.get("sharesOutstanding", 0) / 1e9, 3)
                    if info.get("sharesOutstanding")
                    else "N/A"
                ),
                "Float Shares (B)": (
                    round(info.get("floatShares", 0) / 1e9, 3)
                    if info.get("floatShares")
                    else "N/A"
                ),
                "Book Value/Share ($)": (
                    round(info.get("bookValue", 0), 2)
                    if info.get("bookValue")
                    else "N/A"
                ),
                "EV/EBITDA": (
                    round(info.get("enterpriseToEbitda", 0), 2)
                    if info.get("enterpriseToEbitda")
                    else "N/A"
                ),
                "EV/Revenue": (
                    round(info.get("enterpriseToRevenue", 0), 2)
                    if info.get("enterpriseToRevenue")
                    else "N/A"
                ),
                # === Technicals & Price Data ===
                "Current Price ($)": (
                    round(info.get("currentPrice", 0), 2)
                    if info.get("currentPrice")
                    else "N/A"
                ),
                "Open ($)": (
                    round(info.get("open", 0), 2) if info.get("open") else "N/A"
                ),
                "Previous Close ($)": (
                    round(info.get("previousClose", 0), 2)
                    if info.get("previousClose")
                    else "N/A"
                ),
                "Day High ($)": (
                    round(info.get("dayHigh", 0), 2) if info.get("dayHigh") else "N/A"
                ),
                "Day Low ($)": (
                    round(info.get("dayLow", 0), 2) if info.get("dayLow") else "N/A"
                ),
                "52-Week High ($)": (
                    round(info.get("fiftyTwoWeekHigh", 0), 2)
                    if info.get("fiftyTwoWeekHigh")
                    else "N/A"
                ),
                "52-Week Low ($)": (
                    round(info.get("fiftyTwoWeekLow", 0), 2)
                    if info.get("fiftyTwoWeekLow")
                    else "N/A"
                ),
                "50-Day MA ($)": (
                    round(info.get("fiftyDayAverage", 0), 2)
                    if info.get("fiftyDayAverage")
                    else "N/A"
                ),
                "200-Day MA ($)": (
                    round(info.get("twoHundredDayAverage", 0), 2)
                    if info.get("twoHundredDayAverage")
                    else "N/A"
                ),
                "Volume": info.get("volume", "N/A"),
                "Avg Volume": info.get("averageVolume", "N/A"),
                # === Profitability & Ratios ===
                "EPS (TTM)": (
                    round(info.get("trailingEps", 0), 2)
                    if info.get("trailingEps")
                    else "N/A"
                ),
                "EPS (Forward)": (
                    round(info.get("forwardEps", 0), 2)
                    if info.get("forwardEps")
                    else "N/A"
                ),
                "PE Ratio (Trailing)": (
                    round(info.get("trailingPE", 0), 2)
                    if info.get("trailingPE")
                    else "N/A"
                ),
                "PE Ratio (Forward)": (
                    round(info.get("forwardPE", 0), 2)
                    if info.get("forwardPE")
                    else "N/A"
                ),
                "PEG Ratio": (
                    round(info.get("pegRatio", 0), 2) if info.get("pegRatio") else "N/A"
                ),
                "Profit Margin (%)": (
                    f"{round(info.get('profitMargins', 0) * 100, 2)}%"
                    if info.get("profitMargins")
                    else "N/A"
                ),
                "Operating Margin (%)": (
                    f"{round(info.get('operatingMargins', 0) * 100, 2)}%"
                    if info.get("operatingMargins")
                    else "N/A"
                ),
                "ROA (%)": (
                    f"{round(info.get('returnOnAssets', 0) * 100, 2)}%"
                    if info.get("returnOnAssets")
                    else "N/A"
                ),
                "ROE (%)": (
                    f"{round(info.get('returnOnEquity', 0) * 100, 2)}%"
                    if info.get("returnOnEquity")
                    else "N/A"
                ),
                # === Cash Flow ===
                "Operating CF ($B)": (
                    round(info.get("operatingCashflow", 0) / 1e9, 2)
                    if info.get("operatingCashflow")
                    else "N/A"
                ),
                "Free CF ($B)": (
                    round(info.get("freeCashflow", 0) / 1e9, 2)
                    if info.get("freeCashflow")
                    else "N/A"
                ),
                "CapEx ($B)": (
                    round(info.get("capitalExpenditures", 0) / 1e9, 2)
                    if info.get("capitalExpenditures")
                    else "N/A"
                ),
                # === Debt / Liquidity ===
                "Total Debt ($B)": (
                    round(info.get("totalDebt", 0) / 1e9, 2)
                    if info.get("totalDebt")
                    else "N/A"
                ),
                "Debt to Equity": (
                    round(info.get("debtToEquity", 0), 2)
                    if info.get("debtToEquity")
                    else "N/A"
                ),
                "Quick Ratio": (
                    round(info.get("quickRatio", 0), 2)
                    if info.get("quickRatio")
                    else "N/A"
                ),
                "Current Ratio": (
                    round(info.get("currentRatio", 0), 2)
                    if info.get("currentRatio")
                    else "N/A"
                ),
                # === Dividends ===
                "Dividend Rate ($)": (
                    round(info.get("dividendRate", 0), 2)
                    if info.get("dividendRate")
                    else "N/A"
                ),
                "Dividend Yield (%)": (
                    round(info.get("dividendYield", 0) * 100, 2)
                    if info.get("dividendYield")
                    else "N/A"
                ),
                "Payout Ratio": (
                    f"{round(info.get('payoutRatio', 0) * 100, 2)}%"
                    if info.get("payoutRatio")
                    else "N/A"
                ),
                "Ex-Dividend Date": info.get("exDividendDate", "N/A"),
                # === Growth ===
                "Revenue Growth YoY": (
                    f"{round(info.get('revenueGrowth', 0) * 100, 2)}%"
                    if info.get("revenueGrowth")
                    else "N/A"
                ),
                "Earnings Growth YoY": (
                    f"{round(info.get('earningsGrowth', 0) * 100, 2)}%"
                    if info.get("earningsGrowth")
                    else "N/A"
                ),
                # === Dates ===
                "Earnings Date": info.get("earningsDate", "N/A"),
                "Last Split Date": info.get("lastSplitDate", "N/A"),
                "Last Split Factor": info.get("lastSplitFactor", "N/A"),
            }

        except Exception as e:
            return {"error": f"Failed to fetch extended info for {self.symbol}: {e}"}
