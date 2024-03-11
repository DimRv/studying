"""
type(object) - возвращает type объекта, переданного в параметре
type(name, bases, dict, **kwds) - создает новый объект class, аргументы становятся значениями __name__, __bases__, __dict__

Встроенная функция type и оператор class создают один и тот же объект type, вызов которого создает экземпляры.

type один из методов интроспекции (способность исследования объектов внутри самого кода)
"""

help(type)
print(type(None))
print(type(True))
print(type(2))
print(type(""))
print(type(type(None)))
print('-'*30)


d = {
    'test': 'test',
    'test2': 'test2',
}
TestType = type('TestType', (object,), d)

a = TestType()
print(a)
print(a.test, a.test2)


class TestType2:
    test = 'test'
    test2 = 'test2'


a2 = TestType2()
print(a2)
print(a2.test, a2.test2)

new_var = type(a2)
a3 = new_var()
print(a3.test, a3.test2)

