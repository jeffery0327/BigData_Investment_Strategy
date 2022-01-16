import requests as req
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import keras



start=1970
end=2020
stock=["2330.TW","6547.TWO","3081.TWO","2610.TW","2618.TW","2609.TW","2615.TW","2603.TW","2303.TW","2317.TW","5706.TW","2734.TWO","2731.TW","9943.TW","2002.TW","1216.TW","1203.TW","1210.TW","1215.TW","1217.TW","1227.TW"]
stock_name=["TSMC","MVC","UBIP","CAL","EVAAIR","YMTC","WANHAI","EVA_Air","UMC","Hon_Hai","PHX_TOUR","Ezfly","Liontravel","HOLIDAY","SINOSTEEL","UNI_PRESIDENT","Ve_Wong","CHEMCHINA","CP","AGV","SFC"]


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
    df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0])
    df['date']=date
    # 日期 時間 收市價 低點 高點 成交量 開市價
    non_null_data = df.dropna()
    
    return non_null_data[['high','date']] 

def df_toCSV(df,dist):
    df.to_csv(dist)

def stamp_toDate(stamp):
    date=[]
    for i in range(0,len(stamp)):
        time_stamp = stamp[i] # 設定timeStamp
        struct_time = time.localtime(time_stamp) # 轉成時間元組
        timeString = time.strftime("%Y-%m-%d", struct_time) # 轉成字串
        date.append(timeString)
    return date

def init():
    for i in range(0,len(stock)):
        datapath = "data/"+stock_name[i]+".csv"
        df_toCSV(crawl_price(stock[i],start,end),datapath)

def LSTM(datapath_id):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    datapath = "data/"+stock_name[datapath_id]+".csv"

    data = pd.read_csv(datapath)

    train_len = len(data)*7 /10


    test = data[data.index >= train_len]
    train = data[data.index < train_len]

    train_set = train['high']
    test_set = test['high']
    data_set = data['high']

    from sklearn.preprocessing import MinMaxScaler 
    sc = MinMaxScaler(feature_range = (0, 1))
    #需將資料做reshape的動作，使其shape為(資料長度,1) 
    train_set= train_set.values.reshape(-1,1)
    training_set_scaled = sc.fit_transform(train_set)

    X_train = [] 
    y_train = []
    for i in range(10,len(train_set)):
        X_train.append(training_set_scaled[i-10:i-1, 0]) 
        y_train.append(training_set_scaled[i, 0]) 
    X_train, y_train = np.array(X_train), np.array(y_train) 
    X_train = np.reshape(X_train, 
                            (X_train.shape[0], X_train.shape[1], 1))

    # print("i 天前")
    # print(X_train)
    # print("第 i 天")
    # print(y_train)

    import keras
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.layers import LSTM
    from keras.layers import Dropout,BatchNormalization

    keras.backend.clear_session()
    regressor = Sequential()
    regressor.add(LSTM(units = 100, input_shape = (X_train.shape[1], 1)))
    regressor.add(Dense(units = 1))
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

    history = regressor.fit(X_train, y_train, epochs = 100, batch_size = 16)
    # plt.title('train_loss')
    # plt.ylabel('loss')
    # plt.xlabel('Epoch')
    # plt.plot( history.history["loss"])

    # dataset_total = pd.concat((train['high'], test['high']), axis = 0)
    # inputs = dataset_total[len(dataset_total) - len(test) - 10:].values


    inputs = data['high'].values.reshape(-1,1)
    inputs = sc.transform(inputs)
    X_test = []
    for i in range(train_len+1, len(inputs)):
        X_test.append(inputs[i-10:i-1, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predicted_stock_price = regressor.predict(X_test)
    #使用sc的 inverse_transform將股價轉為歸一化前
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)

    plt.plot(data_set.values, color = 'black', label = 'Real '+stock_name[datapath_id]+' Stock Price')
    plt.plot(predicted_stock_price, color = 'green', label = 'Predicted '+stock_name[datapath_id]+' Stock Price')
    plt.title('TATA Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.savefig('data/chart/'+stock_name[datapath_id]+'.png')
    plt.clf()
    


def run():
    for i in range(0,len(stock_name)):
        LSTM(i)

init()
run()


