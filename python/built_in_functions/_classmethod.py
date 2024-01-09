"""
classmethod(method) -> classmethod

Преобразует обычный метод в метод класса.
Обычный метод работает с экземпляром объекта (self первый параметр).
Classmethod работает с классом (cls первый параметр)
"""
#Обычный метод:
class Test:
    val = 'val'

    def f_test(self):
        print(self.val)

    def __init__(self, val):
        self.val = val


t = Test('test')
print(type(Test.f_test), Test.f_test(t))


#Метод класса
class Test:
    val = 'val'

    def f_test(cls):
        print(cls.val)

    def __init__(self, val):
        self.val = val

    f_test = classmethod(f_test)


t = Test('test')
print(type(Test.f_test), Test.f_test())


#Применение
class Enemy:
    enemy_list = []

    @classmethod
    def show_enemy_pos(cls):
        for i in cls.enemy_list:
            print(i.pos)

    def __init__(self, pos):
        self.pos = pos
        self.__class__.enemy_list.append(self)


Enemy((10, 20))
Enemy((20, 20))
Enemy((30, 20))
Enemy.show_enemy_pos()
print(len(Enemy.enemy_list)) #Кол-во экземплятов