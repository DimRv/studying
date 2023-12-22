"""Возвращает True/False - результат проверки является ли объект экземпляром класса

isinstance(obj, class_or_tuple, /)
"""


help(isinstance)
print(isinstance(5, int))
print(isinstance('str', str))
print(isinstance('str', object))
print(isinstance(True, int))
print(isinstance(True, (float, str, int))) #bool is int subclass

