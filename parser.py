import requests as req
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def crawl_price(stock):

    sec_start="0"
    sec_end="1640995200"

    #抓資料
    site = "https://query1.finance.yahoo.com/v8/finance/chart/"+stock+"?period1="+sec_start+"&period2="+sec_end+"&interval=1d&events=history&=hP2rOschxO0"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    response = req.get(site,headers=headers)

    #將資料整裡成 DataFrame
    data = json.loads(response.text)
    df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))
    # 日期 時間 收市價 低點 高點 成交量 開市價
    #print(df)

    return df[['high']] 


stock="2330.TW"
print(crawl_price(stock))






