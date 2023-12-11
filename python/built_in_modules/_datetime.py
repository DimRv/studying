"""
Модуль datetime содержит объекты:
time
date
    datetime
timedelta
tzinfo
    timezone

-------------------------------------date-------------------------------------------
Создание объекта date:
- datetime.date(year, month, day) - вернет экземпляр объекта date с заданными значениями
- datetime.date.today() - date с текущей датой
- datetime.date.replace(year, month, day) - путем замены года, месяца или дня в другой дате
- datetime.date.fromisoformat("2023-12-10") создается из строки
- datetime.date.fromisocalendar(year,week,day) во втором столбце недели, а не месяц
- datetime.date.fromordinal(day) точка отсчета date - начало эпохи (1970)
- datetime.date.fromtimestamp(timestamp) - timestamp - время прошедшее с начала эпохи (будет 1970 + ts)

Получение свойств объекта date:
- instance.year - возвращает целое число, год экземпляра объекта (1..9999)
- instance.month - возвращает целое число, месяц экземпляра объекта (1..12)
- instance.day - возвращает целое число, день экземпляра объекта (1..30 или 1..31)
- instance.ctime() - вернет строку в формате: Mon Dec 11 00:00:00 2023
- instance.isoformat() - вернет строку в формате: 2023-12-11
- instance.isoweekday() - возвращает целое число, день недели (1..7 mon..sun)
- instance.isocalendar() - создаст объект datetime.IsoCalendarDate из текущей даты
- instance.timetuple() - создаст объект time.struct_time из текущей даты
- instance.toordinal() - возвращает число количество дней до указанной даты (используется при сравнении дат)
- instance.strftime(format) - возвращает строку, преобразованную под format

УСЛОВНЫЕ КОНСТАНТЫ:
- instance.max - вернет число максимально допустимая дата: 9999-12-31
- instance.min - вернет число минимально допустимая дата: 0001-01-01
- instance.resolution - вернет datetime.timedelta: 1 day, 0:00:00 минимально возможное изменение data

-------------------------------------time-------------------------------------------
"""
import datetime

#ИНТРОСПЕКЦИЯ ОБЪЕКТА:
help(datetime)
print(dir(datetime))
print([i for i in dir(datetime.date) if i[0] != '_'])
print([i for i in dir(datetime.time) if i[0] != '_'])
print([i for i in dir(datetime.datetime) if i[0] != '_'])
#РАБОТА С ДАТОЙ:
print('-'*30, 'date', '-'*30)
#СОЗДАНИЕ объектов date:
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date.today()
print(date2, type(date2))
print(datetime.date.fromisocalendar(2023, 6, 1), type(datetime.date.fromisocalendar(2023, 6, 1)))
print(datetime.date.fromisoformat("2023-12-10"), type(datetime.date.fromisoformat("2023-12-10")))
print(datetime.date.fromordinal(366), type(datetime.date.fromordinal(366)))
ts = datetime.datetime.timestamp(datetime.datetime.now())
print(ts, type(ts), datetime.date.fromtimestamp(ts), type(datetime.date.fromtimestamp(ts)))
print(date2.replace(2024))
#СВОЙСТВА ОБЪЕКТА date:
print(date1, type(date1))
print(date2.year, type(date2.year))
print(date2.month, type(date2.month))
print(date2.day, type(date2.month))
print(date2.ctime(), type(date2.ctime()))
print(date2.isocalendar(), type(date2.isocalendar()))
print(date2.isoformat(), type(date2.isoformat()))
print(date2.isoweekday(), type(date2.isoweekday()))
print(datetime.date(2023, 12, 10).isoweekday())
print(date2.strftime('%d.%m.%Y %H:%M'), type(date2.strftime('%d.%m.%Y %H:%M'),))
print(date2.timetuple(), type(date2.timetuple()))
print(date2.toordinal(), type(date2.toordinal()))
#Условные константы:
print(date2.max)
print(date2.min)
print(date2.resolution)


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