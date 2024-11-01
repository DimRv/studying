"""
@decorator (метафункция)
def func / class Cls

Декораторы позволяют расширить функционал исходной метафункции не изменяя саму функцию
Декоратор записывается в одиночной строке, внутри тела оператора class.
Выполняется сразу при

Популярные встроенные декораторы:
- property
- staticmethod
- classmethod

"""


class StaticMethod:
    """Статический метод может быть вызван и экземпляра, при этом не передается self"""
    @staticmethod
    def method():
        print("hi!")


test = StaticMethod()
test.method()


def test_decorator(func):
    print("Эта функция выполнится первой и один раз")
    print("Подразумевается что функция вернет объект-функцию или объект-класс")
    return func


class TestDecorator:

    @test_decorator
    def testing_func(self):
        print("Текст оригинальной функции")


test = TestDecorator()
test.testing_func()
test.testing_func()


class TestDec:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


@TestDec
def test_func(a, b ,c):
    return a + b + c


print(test_func("a", "b", "c"))
print(test_func("1", "2", "3"))
print(test_func(1, 2, 3))

print(test_func.calls)



