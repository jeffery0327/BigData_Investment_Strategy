# BigData_Investment_Strategy

# 專題目標

1.  以多項金融時間序列進行資產配置，計算資產配置策略效能分析

2.  使用貝氏定理進行決策

3.  時間序列也可能是高頻時間序列(每十分鐘一筆資料)

4.  使用深度學習網路，例如 RNN，使用 LSTM 單元，進行投資策略計算，要嘗試去解釋如何獲得最佳配置?

# 名詞解釋

## 金融時間序列

時間序列是用時間排序的一組隨機變量，國內生產毛額（GDP）、消費者物價指數（CPI）、加權股價指數、利率、匯率等等都是時間序列。

## 貝氏定理

貝氏定理是關於隨機事件 A 和 B 的條件機率的一則定理
![貝氏定理公式](https://wikimedia.org/api/rest_v1/media/math/render/svg/e08d4ab0386c0ebb7d87f398cd38f911440fe3da)
![關係圖](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Bayes%27_Theorem_2D.svg/450px-Bayes%27_Theorem_2D.svg.png)

## 高頻時間序列

高頻數據是指數據採樣的時間間隔較短，採樣頻率大於一般研究時採用的頻率。但高頻這個概念是相對而言的，例如，對於股票，可能要在一天內有多個數據才能稱為高頻數據，而對於巨集觀經濟數據，可能一周採樣一次就可以稱為高頻數據了。

## RNN

循環神經網路（Recurrent neural network：RNN）是神經網路的一種。單純的 RNN 因為無法處理隨著遞歸，權重指數級爆炸或梯度消失問題，難以捕捉長期時間關聯；而結合不同的 LSTM 可以很好解決這個問題。

時間循環神經網路可以描述動態時間行為，因為和前饋神經網路（feedforward neural network）接受較特定結構的輸入不同，RNN 將狀態在自身網路中循環傳遞，因此可以接受更廣泛的時間序列結構輸入。手寫識別是最早成功利用 RNN 的研究結果。

## 遞歸神經網路（RNN）和長短期記憶模型（LSTM）的運作原理

[RNN-LSTM 介紹](https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_rnns_lstm_work.html)

# 專題內容

### 主題: COVID-19 (2020/12~now)對股票的影響

---

### 目標分析股票
#生技 高端疫苗(MVC) 6547 / 聯亞(UBIP) 3081<br>
#航運 華航(CAL) 2610 / 長榮航(EVAAIR) 2618 / 陽明(YMTC) 2609 /萬海(WANHAI) 2615 /長榮(EVA_Air) 2603<br>
#半導體 台積電(TSMC) 2330 /聯電(UMC) 2303<br>
#其他電子 鴻海(Hon_Hai) 2317<br>
#觀光 鳳凰(PHX_TOUR) 5706 / 易飛網(Ezfly) 2734 / 雄獅(Liontravel) 2731 / 好樂迪(HOLIDAY) 9943<br>
#鋼鐵 中鋼(SINOSTEEL) 2002 /<br>
#食品 統一(UNI_PRESIDENT) 1216 / 味王(Ve_Wong) 1203 / 大成(CHEMCHINA) 1210 / 卜蜂(CP) 1215 / 愛之味(AGV) 1217 / 佳格(SFC) 1227<br>

---

### 資料獲取
https://query1.finance.yahoo.com/v8/finance/chart/1598.TW?period1=0&period2=1612417257&interval=1d&events=history&=hP2rOschxO0

1598.TW 為 股票號碼.國家
period1 = 開始時間 ( 1970年 + 0秒 )
period2 = 結束時間 ( 1970年 + 1612417257秒 )

---
### RNN 實作

[透過 LSTM 預測股票](https://wenwender.wordpress.com/2019/10/18/%E5%AF%A6%E4%BD%9C%E9%80%8F%E9%81%8Elstm%E9%A0%90%E6%B8%AC%E8%82%A1%E7%A5%A8/)

1.切分 Test 集

2.將數據做歸一化(Normalization)

3.訓練
