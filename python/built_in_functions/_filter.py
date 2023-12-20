"""Возвращает fiter-объект - итерируемый объект, содержащий отфильтрованные значения

filter(func, iterable) -> filter-obj

    func должно возвращать True/False

в списковых включениях это if:
[exp for var in iter_object if filter]
"""

help(filter)

a = [3, 4, 5, 6, 9]
f = filter(lambda n: n > 4, a)
print(list(f), type(f))