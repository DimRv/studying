"""
bool(obj) -> True/False

Функция bool() возвращает Falsе для 0, None и для всех пустых последовательностей ('', [], {} и т.д).
Во всех других случаях возвращает True.
"""
print(bool(''))
print(bool(' '))
print(bool(0))
print(bool([False]))
print(bool(None))
print(bool())
