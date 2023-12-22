"""Встроенная функция setattr создает атрибут в объекте
setattr(obj, name, value, /)

"""

help(setattr)


class Test:
    pass


setattr(Test, 'attr1', 'val1')
Test.attr2 = 'val2'
print(Test.attr1)
print(Test.attr2)

