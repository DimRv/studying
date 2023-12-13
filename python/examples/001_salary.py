"""C помощью внешнего json файла определяет количество выходных и рабочих дней в каждом месяце и оценивает 'ценность'
рабочего дня в разные месяцы

pip install requests при необходимости
"""
import json
import requests
import datetime

salary = int(input("Введите желаемый уровень оклада: "))
tax_rate = .13
tax = round(salary * tax_rate, 2)
real_salary = salary - tax
year_tax = tax * 12
year_real_salary = real_salary * 12
print(f'При окладе в {salary} рублей:')
print(f'Вы будете ежемесячно отдавать в качестве налога: {tax} рублей в месяц')
print(f'Ваш реальных доход составит: {real_salary} рублей в месяц')
print(f'За год вы отдадите: {year_tax} рублей')
print(f'За год вы заработаете: {year_real_salary} рублей')
year = str(datetime.date.today().year)
url = 'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant' + year + '.json'
holidays_calendar = json.loads(requests.get(url).text)
start_day = datetime.date(int(year), 1, 1)
end_day = datetime.date(int(year)+1, 1, 1)
delta = datetime.timedelta(days=1)
calendar = []
working_days = 0
holidays = 0
day = start_day
last_day = day.day
while day != end_day:
    if str(day) in holidays_calendar['holidays']:
        holidays += 1
    else:
        working_days += 1
    day += delta
    if day.day < last_day:
        calendar.append((working_days, holidays))
        holidays = 0
        working_days = 0
        last_day = 0
    last_day += 1
month_names = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
               'декабрь']


print('\n', f'Ценность рабочего дня в разные месяцы за {year} ГОД:', sep='')
for num, data in enumerate(calendar):
    print('-'*20, month_names[num], '-'*20)
    print(f"За {month_names[num]} {calendar[num][0]} рабочих и {calendar[num][1]} выходных дней.")
    print(f"Ваш доход за день: {round(real_salary/calendar[num][0], 2)} рублей")
