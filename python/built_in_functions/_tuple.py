"""Возвращает кортеж из итерируемого объекта"""


help(tuple)


t1 = tuple([2, 5, 3, 7])
t2 = tuple(range(9))
t3 = tuple(reversed(range(5)))

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))