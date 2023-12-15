'''Кортеж - неизменяемая последовательность упорядоченных объектов'''

help(tuple)
print([i for i in dir(tuple) if not i.startswith('_')])

t1 = (1100, 1200)
t2 = (1100, 1300)
print(type(t1))
print(t1[0])
#t1[0] = 1001 - будет ошибка
print((1, 2) + (3, 4))
print(1 in (1, 2))
print((1, 2) == (1, 2))
print(t1 >= t2, t1 <= t2)
print(t1[0])
print((1, 2) * 4)

#МЕТОДЫ
print((1, 2, 1, 1, 3).count(1))
print((1, 2, 3, 4).index(3))
