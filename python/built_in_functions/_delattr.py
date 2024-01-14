"""
delattr(odj, name)

Удаляет атрибут у объекта
"""

help(delattr)


class Test:
    surname = 'dmitriy'


print(dir(Test))
delattr(Test, 'surname')
print(dir(Test))