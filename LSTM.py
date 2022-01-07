import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


train = pd.read_csv("data/temp_train.csv")
test = pd.read_csv("data/temp_test.csv")

train_set=train['high']
test_set=test['high']


import sklearn
from sklearn.preprocessing import MinMaxScaler 
sc = MinMaxScaler(feature_range = (0, 1))
#需將資料做reshape的動作，使其shape為(資料長度,1) 
train_set= train_set.values.reshape(-1,1)
training_set_scaled = sc.fit_transform(train_set)