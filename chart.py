import numpy as np
import matplotlib.pyplot as plt  # for 畫圖用
import pandas as pd

data = pd.read_csv("data/temp.csv")

data.plot()
plt.show()