"""сlass основной инструмент ООП

Используется для создания новых class-объектов при вызовах которых создаются instance-объекты"""


class ClassName:
    def __init__(self):
        self.test = 'test'


cl = ClassName()
print(cl.test)
