"""Неизменяемый set"""

f1 = frozenset({1, 2, 3, 2, 3})
help(f1)
print([i for i in dir(frozenset) if not i.startswith('_')])
print(f1, type(f1))

#Методы смотри в _set