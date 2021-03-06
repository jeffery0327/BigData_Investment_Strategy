from pandas.core.frame import DataFrame
import requests as req
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime

def crawl_price(stock):

    sec_start="0"
    sec_end="1549258857"

    #抓資料
    site = "https://query1.finance.yahoo.com/v8/finance/chart/"+stock+"?period1="+sec_start+"&period2="+sec_end+"&interval=1d&events=history&=hP2rOschxO0"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    response = req.get(site,headers=headers)


    #將資料整裡成 DataFrame
    data = json.loads(response.text)

    stamp = data['chart']['result'][0]['timestamp']
    date = stamp_toDate(stamp)

    df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0])
    # 日期 時間 收市價 低點 高點 成交量 開市價
    df['date'] = date

    # 去除空資料
    non_null_data = df.dropna()

    return non_null_data[['high','date'] ]

def stamp_toDate(stamp):
    date=[]
    for i in range(0,len(stamp)):
        time_stamp = stamp[i] # 設定timeStamp
        struct_time = time.localtime(time_stamp) # 轉成時間元組
        
        timeString = time.strftime("%Y-%m-%d", struct_time) # 轉成字串
        
        date.append(timeString)
    return date

stock="6547.TWO"
crawl_price(stock).to_csv("data/MVC.csv")






