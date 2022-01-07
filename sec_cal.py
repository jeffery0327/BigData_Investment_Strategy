def Cal_sec(start,end):
    days=0
    for i in range(start,end):
        days+=Perpetual_calendar(i)
    sec=days*86400
    return sec

def Cal_sec_Month(start_year,start_month,end_year,end_month):
    days=0
    for i in range(start_year,end_year):
        days+=Perpetual_calendar(i)
    days-=Month_calendar(start_month,start_year)
    days+=Month_calendar(end_month,end_year)
    sec=days*86400
    return sec

# 1  2     3  4  5  6  7  8  9  10 11 12 (月)
# 31 28|29 31 30 31 30 31 31 30 31 30 31 
# 31 59|60 90|91 120|121 151|152 181|182 212|213 243|244 273|274 304|305 334|335 365|366

def Month_calendar(month,year):
    month-=1
    normal_year=[31,59,90,120,151,181,212,243,273,304,334,365]
    leap_year=[31,60,91,121,152,182,213,244,274,305,335,366]
    if year%4!=0:
        return normal_year[month]
    else:
        if year%100!=0:
            return leap_year[month]
        else:
            if year%400!=0:
                return normal_year[month]
            else:
                return leap_year[month]

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





print(Cal_sec(2020,2022))
print(Cal_sec_Month(2020,2,2021,12))