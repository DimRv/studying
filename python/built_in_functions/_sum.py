"""Возвращает сумму чисел в итерируемом объекте"""

help(sum)

s1 = sum([2, 4, 5])
s2 = sum(range(1, 9))
s3 = sum(range(1, 9), 100)
s4 = sum(range(1, 9), 0.0)

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))