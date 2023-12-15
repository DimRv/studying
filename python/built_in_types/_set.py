"""Множество - НЕ упорядоченная последовательность из неизменяемых уникальных объектов
Изменяемый тип данных
"""

help(set)
print([i for i in dir(set) if not i.startswith('_')])

s1 = {3, 5, 3, 'string', print, True, None}
s2 = {3, 6, 67, 5}
print(s1, type(s1))

#Операторы
print(s1 & s2) #intersection
print(3 in s1)
print(s1 == {3, 5, 3, 'string', print, True, None}, s1 is {3, 5, 3, 'string', print, True, None})
print(s1 | s2) #union
print(s1 - s2) #difference
print(s1 ^ s2) #symmetric_difference

#МЕТОДЫ
s3 = {1, 2}
print(s3.add(3), s3)
print(s3.clear(), s3)
s3 = {1, 2}
print(s3.copy(), s3)
s4 = {2, 3}
print(s3.difference(s4), s3 - s4)
print(s3.difference_update(s4), s3)
print(s3.discard(2), s3) # Удаление при наличии элемента
print(s3.intersection({1, 2}), s3 & {1, 2} )
print(s3.intersection_update({1, 2}), s3)
print({1, 2}.isdisjoint({3})) #проверка на отсутствие совпадений с другим объектом
print({1}.issubset({1, 2}))
print({1, 2}.issuperset({1}))
print(s3.pop(), s3)
print(s4.remove(2), s4)
print(s3.symmetric_difference(s4), s3 ^ s4)
print(s3.symmetric_difference_update(s4), s3)
print(s3.union(s4), s3 | s4)
print(s3.update(s4), s3)



