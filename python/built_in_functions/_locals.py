"""Встроенная функция locals возвращает словарь из 'переменная':'значение текущей области видимости'"""

help(locals)

a = 'val_a'
b = 'val_b'

print(locals())


def f1():
    a = 'val_a'
    b = 'val_b'
    print(locals())


f1()


class Test:
    a = 'val_a'
    b = 'val_b'
    print(locals())