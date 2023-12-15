"""
del - оператор удаления
del object
Выполняет __delitem__ объект
"""
a = 5
del a
print(dir())
list1 = [1, 2, 3]
del list1[1]
print(list1)