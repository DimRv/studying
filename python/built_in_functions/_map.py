"""Возвращает итерируемый объект map полученный путем применения функции к каждому элементу итератора

map(func, *iterables) -> map-object
"""

help(map)


def f1(val, add='added_info'):
    return val + add


m1 = map(f1, ['1', 'one'])
print(m1, type(m1))
print(list(m1))

m2 = map(f1, ['1', 'one'], ['add1', 'add2'])
print(m2, type(m2))
print(list(m2))