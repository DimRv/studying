"""
Пример паттерна factory
Тип создаваемого объекта определяется по переданному параметру
Класс создает экземпляры разных типов
"""


class NoFactoryObjectError(ValueError):
    pass


class A:
    def __init__(self):
        self.a = "A"


class B:
    def __init__(self):
        self.b = "B"


class Factory:

    @staticmethod
    def create_object(title):
        objects = {
            'a': A,
            'b': B,
        }

        obj = objects.get(title, None)
        if obj:
            return obj()
        raise NoFactoryObjectError


a = Factory.create_object("a")
b = Factory.create_object("b")
