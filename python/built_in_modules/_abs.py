"""Создает абстрактные суперклассы и методы"""


from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def m(self): pass


class B(A):
    def __init__(self, b):
        self.b = b

    def m(self):
        self.b = self.b * 2

    def __str__(self):
        return str(self.b)


b = B("a")
print(b)
b.m()
print(b)

