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
Создание объекта time:
- datetime.time(h, m, s, micro_sec, tzinfo=None) - создание объект datetime.time
- datetime.time.replace(h=0, m=0, s=0, ms=0) - создание объект datetime.time путем замены другого

Свойства:
- instance.time.hour - int часы
- instance.time.minute int минуты
- instance.time.second int секунды
- instance.time.microsecond int - микросекунды
- instance.time.isoformat - str преобразование времени к iso формату
- instance.time.dst - учтен ли переход на летнее время
- instance.time.fold - учет повторяющегося интервала при переходе летнего и зимнего
- instance.time.tzinfo
- instance.time.tzname
- instance.time.utcoffset()
- instance.time.strftime()

Условные константы:
- instance.max 23:59:59.999999
- instance.min 00:00:00
- instance.resolution 0:00:00.000001

-------------------------------------datetime-------------------------------------------
поддержка свойств time и date, а также:
Создание:
- datetime.datetime.combine(date2, time2)
- datetime.datetime.utcnow()
- datetime.datetime.strptime(str, format)

Доп свойства:
- instance.date
- instance.time
- instance.astimezone() - str с UTC

-------------------------------------timedelta-------------------------------------------
Создание:
- datetime.timedelta(days, hours)
- datetime.datetime1 - datetime.datetime2

-------------------------------------format-------------------------------------------
%a - сокращенный день недели
%A - полный день недели
%b - сокращенное название месяца
%B - полное название месяца
%c - Tue Dec 12 15:40:53 2023
%d - day 01..31
%H - hour 00..23
%I - 01..12
%j - день в году 1..366
%m - 01..12
%M - 00..59
%p - AM or PM
%S - секунды 00..61
%U - номер недели 00..53 0-Sunday
%w - день недели
%W - номер недели 00..53 0-Monday
%x - date представление
%X - time представление
%y - год в короткой записи
%Y - год в четырехзначном
%z - -23:59, +23:59
%Z - Time zone name
"""


import datetime

#ИНТРОСПЕКЦИЯ МОДУЛЯ:
help(datetime)
print(dir(datetime))
print([i for i in dir(datetime.date) if i[0] != '_'])
print([i for i in dir(datetime.time) if i[0] != '_'])
print([i for i in dir(datetime.datetime) if i[0] != '_'])
print([i for i in dir(datetime.timedelta) if i[0] != '_'])
print([i for i in dir(datetime.tzinfo) if i[0] != '_'])

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
#Создание объекта time
time1 = datetime.time(23, 11, 30, 122255)
time2 = datetime.time(10)
print(time1, time2, type(time1))
print(datetime.time.fromisoformat('10:30'), type(datetime.time.fromisoformat('10:30')))
print(time1.replace(10), type(time1))
#Свойства объекта time
print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)
print(time1.isoformat())
print(time1.dst())
print(time1.fold)
print(time1.tzinfo)
print(time1.tzname())
print(time1.utcoffset())
#Условные константы:
print(time1.max)
print(time1.min)
print(time1.resolution)

print('-'*30, 'datetime', '-'*30)
dt1 = datetime.datetime.now()
dt2 = datetime.datetime.today()
dt3 = datetime.datetime.combine(date2, time2)
dt4 = datetime.datetime.utcnow()
dt5 = datetime.datetime.strptime('31.12.2023 23:59:59.999999', '%d.%m.%Y %H:%M:%S.%f')
print(dt1, dt2, dt3, dt4, dt5, type(dt1))
print(dt1.astimezone())
print(dt1.date)
print(dt1.time)
print(dt1.strftime("%c"))

print('-'*30, 'timedelta', '-'*30)
time_delta1 = date2 - date1
time_delta2 = datetime.timedelta(days=1)
print(time_delta1.days)
print(time_delta1.max)
print(time_delta1.microseconds)
print(time_delta1.min)
print(time_delta1.seconds)
print(time_delta1.resolution)
print(time_delta1.total_seconds())
