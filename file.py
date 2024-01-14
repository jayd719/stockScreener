
from playwright.sync_api import sync_playwright
from time import sleep
from os.path import exists
HEADLESS=True

STOCKS=['UBER','TD','ABNB']




class Stock:
    def __init__(self,sym,price,sector,industry):
          self.stockSymbol= sym
          self.price = price
          self.sector = sector
          self.industry = industry
          
def yahooURL(stock):
    return f'https://ca.finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch'

def infoFromYahoo(webpage):
    stockSymbol = webpage.text_content('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1')
    stockPrice = webpage.text_content('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')
    webpage.keyboard.press("PageDown")
    webpage.keyboard.press("PageDown")
    stockSector =webpage.text_content('//*[@id="Col2-12-QuoteModule-Proxy"]/div/div/div/div/p[2]/span[2]')
    stockIndustry=webpage.text_content('//*[@id="Col2-12-QuoteModule-Proxy"]/div/div/div/div/p[2]/span[4]')
    
    return Stock(stockSymbol,stockPrice,stockSector,stockIndustry)


def stockList():
    STOCKLIST =[]
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS, slow_mo=50)
            webpage = browser.new_page()
            for STOCK in STOCKS:
                webpage.goto(yahooURL(STOCK))
                STOCKLIST.append(infoFromYahoo(webpage))
            browser.close()
    return STOCKLIST


dataFile = open('stockTracker/stockData.txt','w',encoding='utf-8')
for stock in stockList():
    dataFile.write(f'{stock.stockSymbol}::{stock.price}\n')
    