"""Возвращает True/False - есть ли атрибут в объекте"""


class Test:
    attr = 'value'


def f1():
    pass


f1.attr = 'value'


print(hasattr(Test, 'attr'))
print(hasattr(Test, 'attr2'))
print(hasattr(f1, 'attr'))
print(hasattr(f1, 'attr2'))

