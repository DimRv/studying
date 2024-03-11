"""
Метаклассы позволяют вставлять логику, подлежащую автоматическому выполнению в конце оператора class, при
создании объекта класса.

type - встроенная функция генерирующая классы
метаклассы - подклассы класса type
объекты классов это экземпляры класса type
экземпляры объекта генерируются из класса

Вызов type запускает (__call__):
type.__new__(type, class_name, суперклассы, словарь атрибутов) - создание объекта класса
type.__init__(класс, имя_класса, суперклассы, словарь атрибутов) - инициализация объекта класса

Метаклассы меняют стандартный вызов type специальным подклассом

Создание:

class NewMeta(type):
    def __new__(cls, name, bases, dct):

Объявление:

class ClName(metaclass=Meta):

"""


class SimpleMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Создание нового класса {name}")
        return type.__new__(cls, name, bases, dct)


class MyClass(metaclass=SimpleMeta):
    a = "test"

a = MyClass()
b = MyClass()


class ValidationMeta(type):
    def __new__(cls, name, bases, dct):
        if "attribute" not in dct:
            raise ValueError("Класс должен содержать атрибут 'attribute'")
        return super().__new__(cls, name, bases, dct)


class ValidClass(metaclass=ValidationMeta):
    attribute = 42


class InvalidClass(metaclass=ValidationMeta):
    pass