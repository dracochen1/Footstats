from datetime import date, timedelta

sdate = date(2019, 1, 15)   # start date
edate = date(2020, 9, 15)   # end date

delta = edate - sdate       # as timedelta

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    print("Date")
    print(day)