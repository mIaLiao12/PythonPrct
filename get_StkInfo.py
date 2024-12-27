import requests as rq
from bs4 import BeautifulSoup 
import pandas as pd 

try:
    params = {'strMode':'2'}
    web = rq.get('https://isin.twse.com.tw/isin/C_public.jsp',params=params)
    #print(web.text)
    soup = BeautifulSoup(web.text, "lxml")    
    tr = soup.findAll('tr')
    s = []
    tds = []
    for raw in tr:
         data = [td.get_text() for td in raw.findAll("td")]
         if len(data) == 1: #類別
            s= data
         elif len(data) == 7:
            #有價證券代號及名稱拆成二個欄位
            stock = data[0].split('\u3000') 
            tds.append(s+stock+data[1:])

    #標頭列處理-往前加的欄位
    tds[0].insert(0,"有價證券代號")        
    tds[0].insert(0,"類別")        
    tds[0][2]='名稱' 

    df = pd.DataFrame(tds[1:],columns=tds[0])             
    #print(df)
    #編碼 此網頁是ansi encoding
    df.to_csv("output\stock.csv",index=False,encoding="ansi")
      
except Exception as e:
    print(e)
      

