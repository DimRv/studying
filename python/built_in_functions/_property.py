"""
property(fget=None, fset=None, fdel=None, doc=None)

"""

help(property)


class Test:
    def __init__(self):
        self.x = 'start'


t = Test()
print(t.x)
t.x = 'second'
print(t.x)
del t.x


class Test2:
    """Свойство защищено от перезаписи и удаления"""
    @property
    def x(self):
        return 'test'

t2 = Test2()
print(t2.x)
print(Test2.x, type(Test2.x))
print(dir(Test2.x))
#t2.x = '1'
#del t2.x


class Test3:
    """Свойство защищено от удаления"""

    def __init__(self):
        self.n = 'start'

    @property
    def x(self):
        return self.n

    @x.setter
    def x(self, x):
        self.n = x


t3 = Test3()
print(t3.x)
t3.x("end")

