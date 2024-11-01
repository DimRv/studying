"""
try:
    raise ErrorObject или InstanceOfException
except:

raise без аргумента повторно генерирует текущее исключение

Оператор raise позволяет самостоятельно генерировать исключения.
Если в raise передается объект-исключения, то автоматически создастся экземпляр этого исключения без параметров
"""

try:
    raise IndexError
except IndexError:
    print('Обработка исключения')


class MyError(Exception):
    pass


try:
    raise MyError()
except MyError:
    print("Обработка MyError")
    raise
