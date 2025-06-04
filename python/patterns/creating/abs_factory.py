"""
Паттерн абстрактная фабрика расширяет возможности обычной фабрики застравляя реализовывать методы
"""
from abc import ABC, abstractmethod


class ABCClass(ABC):

    @abstractmethod
    def say(self):
        pass


class Cat(ABCClass):
    def __init__(self, name):
        self.name = name

    def say(self):
        return 'Мяу'


class Dog(ABCClass):
    def __init__(self, name):
        self.name = name

    def say(self):
        return 'Гав'


class Factory:
    @staticmethod
    def create(title, name):
        objects = {
            "cat": Cat,
            "dog": Dog
        }

        return objects[title](name)


cat1 = Factory.create('cat', 'Murzik')
cat2 = Factory.create('cat', 'Boris')
dog = Factory.create('dog', "Bobby")

for animal in cat1, cat2, dog:
    print(animal.say())
