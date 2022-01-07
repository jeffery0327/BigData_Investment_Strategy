import requests as req
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Cal_sec(start,end):
    days=0
    for i in range(start,end):
        days+=Perpetual_calendar(i)
    sec=days*86400
    return str(sec)

def Perpetual_calendar(year):
    if year%4!=0:
        return 365
    else:
        if year%100!=0:
            return 366
        else:
            if year%400!=0:
                return 365
            else:
                return 366

def crawl_price(stock,year_start,year_end):

    sec_start=Cal_sec(1970,year_start)
    sec_end=Cal_sec(1970,year_end)

    #抓資料
    site = "https://query1.finance.yahoo.com/v8/finance/chart/"+stock+"?period1="+sec_start+"&period2="+sec_end+"&interval=1d&events=history&=hP2rOschxO0"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    response = req.get(site,headers=headers)

    #將資料整裡成 DataFrame
    data = json.loads(response.text)
    stamp = data['chart']['result'][0]['timestamp']
    date = stamp_toDate(stamp)
    df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=date)
    # 日期 時間 收市價 低點 高點 成交量 開市價
    

    return df[['high']] 

def df_toCSV(df,dist):
    df.to_csv(dist)

def stamp_toDate(stamp):
    date=[]
    for i in range(0,len(stamp)):
        time_stamp = stamp[i] # 設定timeStamp
        struct_time = time.localtime(time_stamp) # 轉成時間元組
        timeString = time.strftime("%Y-%m-%d %H:%M:%S", struct_time) # 轉成字串
        date.append(timeString)
    return date

start=1970
end=2020
stock=["2330.TW","6547.TW","3081.TW","2610.TW","2618.TW","2609.TW","2615.TW","2603.TW"]
datapath=["data/temp.csv","data/MVC.CSV","data/UBIP.CSV","data/CAL.CSV","data/EVAAIR.CSV","data/YMTC.CSV","data/WANHAI.CSV","data/EVA_Air.CSV"]



df_toCSV(crawl_price(stock[0],start,end),datapath[0])






