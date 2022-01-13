import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/temp.csv')

# data = data[data.index>4300]

test = data[data.index >= 4550]
train = data[data.index < 4550]

train_set = train['high']
test_set = test['high']

from sklearn.preprocessing import MinMaxScaler 
sc = MinMaxScaler(feature_range = (0, 1))
#需將資料做reshape的動作，使其shape為(資料長度,1) 
train_set= train_set.values.reshape(-1,1)
training_set_scaled = sc.fit_transform(train_set)

print(training_set_scaled)



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


inputs = test_set.values.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(10, len(inputs)):
    X_test.append(inputs[i-10:i-1, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
#使用sc的 inverse_transform將股價轉為歸一化前
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

plt.plot(test['high'].values, color = 'black', label = 'Real 2330TW Stock Price')
plt.plot(predicted_stock_price, color = 'green', label = 'Predicted 2330TW Stock Price')
plt.title('TATA Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
# plt.savefig('lstm_2330.png')