"""Встроенная функция reversed возвращает итерируемый объект со значениями в обратном порядке"""

help(reversed)

rev1 = reversed([1, 2, 3])
rev2 = reversed({'1': 1, "2": 2, '3': 3})
print(rev1, type(rev1))
print(rev2, type(rev2))