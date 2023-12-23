"""Возвращает объект iter из способного к итерации объекта
или из callable объекта пока тот не достигнет sentinel

iter(iterable) -> iterator
iter(callable, sentinel) -> iterator
"""

help(iter)

print(range(5), type(range(5)))
print(iter(range(5)), type(iter(range(5))))

a = iter(['Dima', 'Kolya', 'Mike'])
print(next(a))
print(next(a))
print(next(a))


class Test:
    def __init__(self):
        self.ind = 0
        self.values = ['Dima', 'Kolya', 'Mike']

    def __call__(self):
        val = self.values[self.ind]
        self.ind += 1
        return val

a2 = iter(Test(), 'Mike')
print(next(a2))
print(next(a2))
print(next(a2))