"""Возвращает объект memoryview

memoryview(bytes-like-obj) -> memoryview-obj

Класс memoryview в Python позволяет получать прямой доступ к внутренним данным объекта,
который поддерживает протокол буфера обмена, без копирования.
Это может быть полезно для работы с большими массивами данных или бинарными файлами
"""


help(memoryview)

mem1 = memoryview(b'string')
print(mem1, type(mem1))
print(mem1[0])
print(mem1[1:4], bytes(mem1[1:4]))
