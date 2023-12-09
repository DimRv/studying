import datetime

help(datetime)
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date.today()
time_delta1 = date2 - date1
time_delta2 = datetime.timedelta(days=1)
print(date1, date2.year, time_delta1, time_delta2)
print(date2.weekday())