"""Передает выполнение метода в дереве классов"""

help(super)


class Base:
    increase = 0

    def __init__(self):
        self.__class__.increase += 1


class Sub(Base):
    def __init__(self):
        s = super()
        print(s, type(s))
        super().__init__()


s = Sub()
print(s.increase)


class Subsub(Sub):
    def __init__(self):
        Base.__init__(self)


s2 = Subsub()
print(s.increase)

