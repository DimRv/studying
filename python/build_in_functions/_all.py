"""Возвращает True, если все значения в итераторе вернут True, если итератор пуст то тоже вернет True"""


help(all)
print(all([3, 's', True, print]), all([]), all((None, 'False')))