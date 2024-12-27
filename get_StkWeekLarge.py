# base on https://www.finlab.tw/python_crawler_tdcc_inventory/#wei_lai_kai_fa
import datetime
import requests
import pandas as pd
from io import StringIO


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1\
    0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
res = requests.get("https://smart.tdcc.com.tw/opendata/getOD.ashx?id=1-5", headers=headers)

df = pd.read_csv(StringIO(res.text))

df = df.astype(str)
df = df.rename(columns={
        '資料日期': 'stk_date',
        '證券代號': 'stk_id',
        '持股分級': 'stk_lvl',
        '人數' : 'amt_people',
        '股數': 'stock_cnt', 
        '占集保庫存數比例%': 'stk_percent'
    })  


# 移除「公債」相關的id
debt_id = list(set([i for i in df['stk_id'] if i[0] == 'Y']))
df = df[~df['stk_id'].isin(debt_id)]

#print(debt_id)

# 官方有時會有不同格式誤傳，做例外處理
if 'stk_percent' not in df.columns:    
    df = df.rename(columns={'佔集保庫存數比例%': 'stk_percent'})
        
# 持股分級=16時，資料都為0，要拿掉
df = df[df['stk_lvl'] != '16']
    
# 資料轉數字
float_cols = ['amt_people', 'stock_cnt', 'stk_percent']
df[float_cols] = df[float_cols].apply(lambda s: pd.to_numeric(s, errors="coerce"))
    
# 抓表格上的時間資料做處理
df['stk_date'] = datetime.datetime.strptime(df[df.columns[0]][0], '%Y%m%d')
    
#移掉第一個資料日期欄位 上一行是搞笑嗎...移掉的話下行也無法跑index
#df = df.drop(columns=df.columns[0])

    
# 索引設置 unique index 設下去欄位就不見了
#df = df.set_index(['資料日期','stock_id','持股分級'])

df.to_csv("output\stockLarge0524.csv",index=False,encoding="ansi")
  