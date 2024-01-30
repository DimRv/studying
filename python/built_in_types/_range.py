"""
range(start, end, step)

Возвращает последовательность целых чисел с заданным шагом
"""

help(range)
print([i for i in dir(range) if not i.startswith('_')])

r1 = range(5)
r2 = range(4, 20, 4)
print(r1, type(r1))

print(bool(r1))
print(6 in r2)
print(r1 == range(5), r1 is range(5))
print(r2[3])
print(len(r2))

#Методы
print('-'*20, 'methods', '-'*20)
print(r2.start)
print(r2.step)
print(r2.stop)
print(r2.count(2))
print(r2.index(8))



