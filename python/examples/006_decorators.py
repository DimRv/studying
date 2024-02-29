"""
Декорирование - способ указать управляющий или дополняющий код для функций и классов.
Декоратор это функция или класс, которая управляет другой функцией или классом.
Предлагается способ вставки автоматически запускаемого кода в тело def/class декоратора


"""

print('Пример 1. Декоратор функция.'.center(60, '='))


def add_decorator1(f):
    print("Это дополнительный код к переданной функции, выполнится только один раз при объявлении функции")
    return f


@add_decorator1
def get_value(val):
    """Исходная функция"""
    return val


print(get_value("test1"))
print(get_value("test2"))


def add_decorator2(f):
    """Такой декоратор может применяться и к функции и к методу"""
    def wrapper(*args):
        """Позволяет добавить код к исходной функции не меняя ее"""
        print("Это дополнительный код к переданной функции, выполняется при каждом вызове исходной функции")
        return f(*args)
    return wrapper


@add_decorator2
def get_value(val):
    """Исходная функция"""
    return val


print(get_value("test1"))
print(get_value("test2"))


class MyClass:

    @add_decorator2
    def get_value(self, arg):
        return arg

ins = MyClass()
print(ins.get_value("method1"))
print(ins.get_value("method2"))

print('Пример 2. Декоратор класс.'.center(60, '='))


class Decor:
    """Такой декоратор ТОЛЬКО для декорирования функций, для методов не подходит"""
    def __init__(self, func):
        print("Дополнительный код при объявлении функции")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Дополнительный код при вызовах функции")
        return self.func(*args)


@Decor
def get_value(val):
    """Исходная функция"""
    return val

print(get_value("test1"))
print(get_value("test2"))


print('Пример 3. Декорирование класса.'.center(60, '='))


def add_class_dec1(cls):
    print("Дополнительный код при инициализации класса")
    return cls


@add_class_dec1
class My:
    a = 'test'


my = My()
print(my.a)
print(my.a)


def add_class_dec2(cls):

    class Wrapper:
        def __init__(self, *args):
            print("Дополнительный код при инициализации класса")
            self.cls = cls(*args)

        def __getattr__(self, item):
            print("Дополнительный код при обращении к атрибутам")
            return getattr(self.cls, item)
    return Wrapper


@add_class_dec2
class My:
    a = 'test'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test(self):
        return self.a + self.b


my = My(3, 4)
print(my.a)
print(my.b)
print(my.test())


print('Пример 4. Подсчет кол-ва вызовов объектов.'.center(60, '='))


class Decorator:

    def __init__(self, obj):
        self.calls = 0
        self.obj = obj

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"{self.calls} calls of {self.obj.__name__}")
        return self.obj(*args)


@Decorator
def test(a, b):
    return a + b


print(test(4, 3))
print(test(5, 3))


@Decorator
class T:
    def __init__(self):
        print(self)


a = T()
b = T()
