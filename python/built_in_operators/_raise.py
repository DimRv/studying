"""
try:
    raise ErrorObject или InstanceOfException
except:

raise без аргумента повторно генерирует текущее исключение

Оператор raise позволяет самостоятельно генерировать исключения.
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
