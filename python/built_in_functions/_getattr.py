"""Повзволяет получить атрибут объекта"""

help(getattr)


class Test:
    attr = 'value'


print(getattr(Test, 'attr'))
print(Test.attr)
print(getattr(Test, 'attr2', "нет значения"))


class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, item):
        print(item)
        return getattr(self.wrapped, item)


w = Wrapper([1, 2, 3])
print(w.wrapped)
w.append(4)
print(w.wrapped)

a=[1, 2, 3]
getattr(a, 'append')(4)
print(a)