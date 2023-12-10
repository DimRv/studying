"""
Модуль datetime содержит объекты:
time
date
    datetime
timedelta
tzinfo
    timezone

Создание объекта date:
- datetime.date(year, month, day)
- datetime.date.fromisocalendar(year,week,day) во втором столбце недели, а не месяц
- datetime.date.fromisoformat("2023-12-10") из строки
- datetime.date.fromordinal(day) точка отсчета date - начало эпохи (1970)
- datetime.date.fromtimestamp(timestamp) - timestamp - время прошедшее с начала эпохи (будет 1970 + ts)
- datetime.date.replace(year, month, day) - путем замены года, месяца или дня в другой дате
"""
import datetime

#ИНТРОСПЕКЦИЯ:
help(datetime)
print(dir(datetime))
#РАБОТА С ДАТОЙ:
print('-'*30, 'date', '-'*30)
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date.today()
print([i for i in dir(date1) if i[0] != '_'])
print(date1)
print(date2.year)
print(date2.month)
print(date2.day)
print(date2.ctime())
print(date2.fromisocalendar(2023, 6, 1))
print(date2.fromisoformat("2023-12-10"))
print(date2.fromordinal(366))
ts = datetime.datetime.timestamp(datetime.datetime.now())
print(ts, datetime.date.fromtimestamp(ts))
print(date2.isocalendar())
print(date2.isoformat())
print(date2.isoweekday())
print(date2.max)
print(date2.min)
print(date2.replace(2024))
print(date2.resolution)
print(date2.strftime('%d.%m.%Y %H:%M'))
print(date2.timetuple())
print(date2.toordinal())
#help(date2.resolution)

print('-'*30, 'time', '-'*30)
time1 = datetime.time(23, 1, 30)
time2 = datetime.time(0, 0, 0)

print('-'*30, 'datetime', '-'*30)
dt1 = datetime.datetime.now()
dt2 = datetime.datetime.today().day
dt3 = datetime.datetime.combine(date2, time2)

print('-'*30, 'timedelta', '-'*30)
time_delta1 = date2 - date1
time_delta2 = datetime.timedelta(days=1)


print(date1, date2.year)
print(time_delta1, time_delta2)
print(time1, time2)
print(dt1, dt2)
print(date2.weekday())