'''Возвращает абсолютное значение объекта'''

help(abs)
print(abs(-4), abs(5))


class Abs:
    def __init__(self, val):
        self.num = val

    def __abs__(self):
        return abs(self.num)


i_abs = Abs(-3)

print(abs(i_abs))
