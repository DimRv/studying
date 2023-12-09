"""
Расчет оклада за исключением вычета налога
"""
salary = int((input('Введите желаемый оклад: ')))

print("-"*40)
tax_rate = .13
tax = round(salary * tax_rate, 2)
real_salary = round(salary - tax, 2)
day_salary_in30 = round(real_salary/30, 2)
day_salary_in31 = round(real_salary/31, 2)
hour_salary_in30 = round(day_salary_in30/24, 2)
hour_salary_in31 = round(day_salary_in31/24, 2)
year_salary = round(real_salary * 12)
year_tax = round(tax * 12)
month_to_millioner = 1000000 / real_salary
print(f'Каждый месяц вы будете отдавать в качестве налога: {tax} рублей')
print(f'Ваш реальный заработок составит: {real_salary} рублей')
print(f'При 30-дневном месяце средний доход составит: {day_salary_in30} рублей в сутки '
      f'или {hour_salary_in30} в час.')
print(f'При 31-дневном месяце средний доход составит: {day_salary_in31} рублей в сутки '
      f'или {hour_salary_in31} в час.')
print(f'За год Вы заработаете {year_salary} рублей, а отдадите налогом {year_tax} рублей.')
print(f'Если Вы не будете тратить зарплату, миллионером станете через {month_to_millioner} месяцев')




