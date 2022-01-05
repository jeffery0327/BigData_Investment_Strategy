# BigData_Investment_Strategy

# 專題目標

1.  以多項金融時間序列進行資產配置，計算資產配置策略效能分析

2.  使用貝氏定理進行決策

3.  時間序列也可能是高頻時間序列(每十分鐘一筆資料)

4.  使用深度學習網路，例如 RNN，使用 LSTM 單元，進行投資策略計算，要嘗試去解釋如何獲得最佳配置?

# 名詞解釋

金融時間序列
---

    時間序列是用時間排序的一組隨機變量，國內生產毛額（GDP）、消費者物價指數（CPI）、加權股價指數、利率、匯率等等都是時間序列。

貝氏定理
---

貝氏定理是關於隨機事件 A 和 B 的條件機率的一則定理
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/e08d4ab0386c0ebb7d87f398cd38f911440fe3da)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Bayes%27_Theorem_2D.svg/450px-Bayes%27_Theorem_2D.svg.png)


高頻時間序列
---

高頻數據是指數據採樣的時間間隔較短，採樣頻率大於一般研究時採用的頻率。但高頻這個概念是相對而言的，例如，對於股票，可能要在一天內有多個數據才能稱為高頻數據，而對於巨集觀經濟數據，可能一周採樣一次就可以稱為高頻數據了。
