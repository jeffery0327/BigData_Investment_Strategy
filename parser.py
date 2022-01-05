import requests as req

stock="1598.TW"
sec_start="0"
sec_end="1640995200"

site = "https://query1.finance.yahoo.com/v8/finance/chart/"+stock+"?period1="+sec_start+"&period2="+sec_end+"&interval=1d&events=history&=hP2rOschxO0"

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

response = req.get(site,headers=headers)

print(response.text)