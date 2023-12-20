"""Повзволяет получить атрибут объекта"""

help(getattr)


class Test:
    attr = 'value'


print(getattr(Test, 'attr'))
print(Test.attr)
print(getattr(Test, 'attr2', "нет значения"))