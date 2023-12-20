"""Встроенная функция globals возвращает словарь из переменных глобальной области видимости"""


help(globals)
print(globals())

x = 'x'


def f1():
    y = 'y'
    print(globals())


f1()
