def Cal_sec(start,end):
    days=0
    for i in range(start,end):
        days+=Perpetual_calendar(i)
    sec=days*86400
    return sec

# 公元年分非4的倍數，為平年。
# 公元年分為4的倍數但非100的倍數，為閏年。
# 公元年分為100的倍數但非400的倍數，為平年。
# 公元年分為400的倍數為閏年。

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



print(Cal_sec(1990,2022))