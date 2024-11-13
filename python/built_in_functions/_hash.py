"""Возвращает int - хэш-значение объекта. Функция связана с __hash__ объекта.
Списки и словари не имеют хеш-эначения.

Хэш часто используется при сравнении двух объектов
"""

help(hash)

print(hash(2), type(hash(2)))
print(type(hash('string')), hash('string'), len(str(hash('string'))))

print(dir(int))
