"""Возвращает следующий элемент в итераторе

Если задан default, то вернет его, а не исключение StopIteration
"""

help(next)

i1 = iter([2, 3, 5])
print(next(i1, 0))
print(next(i1, 0))
print(next(i1, 0))
print(next(i1, 0))
print(next(i1, 0))