"""
del object

del - оператор удаления

Выполняет __del__, __delitem__, __delattr__ объекта
"""
a = 5
del a
print(dir())
list1 = [1, 2, 3]
del list1[1]
print(list1)


class NoDelTest:
    val = 5
    data = [1, 2]

    def __del__(self):
        print("IN __del__")

    def __delattr__(self, item):
        print("IN __delattr__")

    def __delitem__(self, item):
        print("IN __delitem__")


d = NoDelTest()
del d.val
del d[1]
del d