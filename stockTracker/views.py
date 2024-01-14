from django.shortcuts import render
from os.path import exists


class Stock:
    def __init__(self,sym,price,sector,industry):
          self.stockSymbol= sym
          self.price = price
          self.sector = sector
          self.industry = industry
          
          
          
def stockList(requests):
    print(exists('stockData.txt'))
    fh = open('stockTracker/stockData.txt','r',encoding='utf-8')  
    STOCKLIST = []
  
    for line in fh:
        data=line.split('::')
        STOCKLIST.append(Stock(data[0],data[1],'d','s'))
        
        
    data={"title":"index",
          'stockList':STOCKLIST}
    print("hellow worls")
    print(STOCKLIST)
    
    return render(requests,'stockTracker/trackerList.html',context=data)
