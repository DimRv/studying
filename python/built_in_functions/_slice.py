"""Создает slice-объект - объект среза, который можно использовать в операциях нарезания
"""


help(slice)


sl1 = slice(1, 4)
sl2 = slice(2, 10, 2)
print(sl1, type(sl1))
li1 = list(range(9))
print(li1[sl1])
print(li1[sl2])
