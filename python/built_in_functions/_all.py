"""Возвращает True если все значения в итераторе вернут True для bool(). Если итератор пуст, то вернет True"""


help(all)
print(all([3, 's', True, print]), all([]), all((None, 'False')))
