"""Встроенная функция sorted используется для создания sorted-объекта - итерируемого объекта со значениями
в определенной последовательности
sorted(iterable, /, *, key=None, reverse=False)
"""


help(sorted)

li1 = [3, 44, 6, 21, 3, 51]
s1 = sorted(li1)
s2 = sorted(li1, reverse=True)
s3 = sorted(li1, key=lambda x: len(str(x)))
s4 = sorted(li1, key=lambda x: x > 5)


print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))





