import pandas as pd
import requests
from io import StringIO
import time
def monthly_report(year, month):
    
    # 假如是西元，轉成民國
    if year > 1990:
        year -= 1911
    
    url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'_0.html'
    if year <= 98:
        url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'.html'
    
    #
    res = requests.get(url)
    res.encoding = 'big5'
    html_df = pd.read_html(res.text)           
   
    # Step3. 篩選出個股月營收資訊
    # 3.1 剃除行數錯誤的表格,並將表格合併
    df = pd.concat([df for df in html_df if df.shape[1] == 11]) 

    # 3.2 設定表格的header 
    df.columns = df.columns.get_level_values(1)

    #  3.3 剃除多餘欄位, 重新排序索引值
    df = df[df['公司名稱'] != '合計']
    df = df.reset_index(drop=True)    

    return df 


# --------------
import datetime
import pandas as pd
import time

data = {}
n_days = 6
now = datetime.datetime.now()

year = now.year
month = now.month

ds=[]
tds =[]

while len(data) < n_days:
    
    print('parsing', year, month)
    
    # 使用 crawPrice 爬資料
    try:
        data['%d-%d-01'%(year, month)] = monthly_report(year, month)  



    except Exception as e:
        print('get 404, please check if the revenues are not revealed')
    
    # 減一個月
    month -= 1
    if month == 0:
        month = 12
        year -= 1

    time.sleep(10)

for i,j in data.items():    
    j.to_html("output/"+i +".html")
    