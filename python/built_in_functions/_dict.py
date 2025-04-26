"""
Встроенная функция для создания словаря или преобразования итерируемых объектов к словарю
"""

help(dict)


d1 = dict()
d2 = dict([('test', 'hi'), ('test2', 'hello')])
d3 = dict(test='hi', age=9, is_baby=True)

print(d1, type(d1))
print(d2, type(d2))
print(d3, type(d3))
