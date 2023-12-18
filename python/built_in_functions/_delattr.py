"""Удаляет атрибут у объекта

delattr(odj, str_attr)
"""

help(delattr)


class Test:
    surname = 'dmitriy'


print(dir(Test))
delattr(Test, 'surname')
print(dir(Test))