"""Итерируемые объекты (iterable) это все последовательности (смотри built_in_objects -> sequences)

Такие объекты имеют методы __iter__ и __next__, которые используется при участии объекта в операции for

__length_hint__() - позволяет получить кол-во элементов в итераторе не выполняя итерацию.
Это приблизительное значение len
"""

help(iter)
i1 = iter(range(5))
i2 = iter([2, 3, 5, 7])
i3 = iter((2, 3, 5, 7))
i4 = iter({'1': 1})
i5 = iter({1, 4, 6})
i6 = iter('string')


class Test:
    def __init__(self):
        self.x = 'Привет'

    def __iter__(self):
        print('iter применился')
        return iter(self.x)


t = Test()
for i in t:
    print(i)

print(i1, type(i1))
print(i2, type(i2))
print(i3, type(i3))
print(i4, type(i4))
print(i5, type(i5))
print(i6, type(i6))

print(dir(object))
print(dir(i1))
print(dir(i2))
print(dir(i3))
print(dir(i4))
print(dir(i5))
print(dir(i6))

print(i1.__length_hint__())
print(i2.__length_hint__())


