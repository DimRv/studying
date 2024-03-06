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

print('Пример 5. Расчет времени выполнения функции.'.center(60, '='))

import time


class TimeDecor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        run_time = time.perf_counter() - start
        print(f"Функции {self.func} потребовалось {run_time} на выполнение")
        return result

@TimeDecor
def get_list(n):
    return [i*2 for i in range(n)]


get_list(13000000)
get_list(13000000)
get_list(13000000)
get_list(13000000)

print('Пример 6. Приватные атрибуты класса.'.center(60, '='))


def get_info(*args):
    print([str(i) for i in args])


def private_dec(*private_attr):
    def decorate_class(Cls):
        class OnInstance:
            def __init__(self, *args, **kwargs):
                self.obj = Cls(*args, **kwargs)

            def __getattr__(self, item):
                get_info("getattr", item)
                if item in private_attr:
                    raise AttributeError(f"It is Private attribute: {item}",)
                else:
                    return getattr(self.obj, item)

            def __setattr__(self, key, value):
                get_info("setattr", key, value)
                if key == 'obj':
                    self.__dict__[key] = value
                elif key in private_attr:
                    raise AttributeError(f"It is Private attribute: {key}",)
                else:
                    setattr(self.obj, key, value)

        return OnInstance
    return decorate_class


@private_dec('data', 'data3', 'method')
class MyClass:
    data = 'data'
    data2 = 'data2'
    def __init__(self, bla):
        self.data3 = 'data3'
        self.data4 = 'data4'
        self.bla = bla
    def method(self):
        print('method')


m1 = MyClass('bla')

try:
    #print(m1.data)
    m1.data = 'newdata1'
except AttributeError:
    print("NO ACCESS")
try:
    print(m1.data2)
    m1.data2 = 'newdata2'
except AttributeError:
    print("NO ACCESS")
try:
    #print(m1.data3)
    m1.data3 = 'newdata3'
except AttributeError:
    print("NO ACCESS")
try:
    print(m1.data4)
    m1.data4 = 'newdata4'
except AttributeError:
    print("NO ACCESS")


print('Пример 7. Приватные и Публичные атрибуты класса.'.center(60, '='))


def access(testfunc):
    def decorate_class(cls):
        class Decor:
            def __init__(self):
                print('init')
                self.obj = cls

            def __getattr__(self, item):
                print('getattr')
                if testfunc(item):
                    raise TypeError("getting private attr")
                else:
                    return getattr(self.obj, item)

            def __setattr__(self, key, value):
                print('setattr')
                if key == 'obj':
                    self.__dict__[key] = value
                elif testfunc(key):
                    raise TypeError("changing private attr")
                else:
                    setattr(self.obj, key, value)
        return Decor
    return decorate_class

def private(attr):
    return access(testfunc = (lambda i: i in attr))

def public(attr):
    return access(testfunc = (lambda i: i not in attr))


@private('age')
class T1:
    """в этом классе только один приватный аттрибут - age, все остальные открытые"""
    age = 'age'
    data = 'data'

@public('age')
class T2:
    """в этом классе только один публичный аттрибут - age, все остальные закрытые"""
    age = 'age'
    data = 'data'

t1 = T1()
t2 = T2()

print(t1.data)
print(t2.age)
#print(t1.age)
#print(t2.data)


print('Пример 8. Проверка передаваемых аргументов.'.center(60, '='))


def check_value(*argchecks):
    def decorator(func):
        def checker(*args):
            for pos, mi, ma in argchecks:
                if args[pos] < mi or args[pos] > ma:
                    raise TypeError(f"Переданное значение {args[pos]} не входит в диапазон от {mi} до {ma}")
            return func(*args)
        return checker
    return decorator


@check_value((0, 1, 31), (1, 1, 12), (2, 1900, 2024))
def create_date(d, m, y):
    return f"{d}.{m}.{y}"


try:
    print(create_date(1, 12, 1987))
    print(create_date(17, 12, 1987))
    print(create_date(11, 13, 1987))
except TypeError as er:
    print(er)

try:
    print(create_date(22, 6, 1941))
    print(create_date(1, 1, 1900))
    print(create_date(32, 13, 1987))
except TypeError as er:
    print(er)
try:
    print(create_date(30, 10, 1899))
except TypeError as er:
    print(er)



