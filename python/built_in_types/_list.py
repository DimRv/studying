"""
Список - упорядоченная последовательность различных объектов в которой важен порядок следования объектов.
Желательно создавать списки с одинаковыми типами данных.
Изменяемый тип.
Итерируемый тип.
"""


#Интроспекция:
help(list)
print([i for i in dir(list) if not i.startswith('_')])

#Создание:
l1 = [3, 4, 5] #базовый синтаксис
l2 = list((3, 4, 5)) #Получение списка из другого итерируемого объекта
l3 = [(i + 5) * 2 for i in range(4)] #списковое включение

#Операторы:
print([1] + [2])
test = [1]
test += [2]
print(test)
del l1[1]
print('after del: ', l1)
print(l1 == l2, l1 is l2)
print(l1 > l2, l1 <= l2)
print([1, 3] * 5)

#МЕТОДЫ:
print(l1.append(6), l1) #добавление в конец
print(l2.clear(), l2) #удаление содержимого списка
print(l1.copy()) #возвращает копию
print(l1.count(5))
print(l1.extend([7, 8]), l1)
print(l1.index(7))
print(l1.insert(0, 0), l1)
print(l1.pop(4), l1)
print(l1.remove(8), l1)
print(l1.reverse(), l1)
print(l1.sort(), l1)

test = [10, 1, 2, 20]
test.sort()
print(test)
test = ['print', '1', '2', '01']
test.sort()
print(test)
test.sort(key=lambda n: len(n))
print(test)
a = [1]
#print(a[-5]) IndexError

a = [[1], [2]]
b = a[:]
print(a, b)