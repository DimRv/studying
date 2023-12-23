"""Возвращает строку, представляющую традиционное представление объекта"""


help(repr)

obj = [1, 2, 4]
obj_str = repr(obj)
#obj_str.pop() - ошибка из-за того что строка
print(obj_str, type(obj_str))
obj2 = eval(obj_str)
print(obj2, type(obj2))
print(obj2.pop)

