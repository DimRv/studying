"""
Exception - объект используемый при создании собственных исключений.

IndexError - объект класса
IndexError() - уже экземпляр класса IndexError
"""

ex = Exception
ex2 = IndexError()
ex3 = SyntaxError()
print(dir(ex))
print(dir(ex2))
print(dir(ex3))
print(isinstance(ex2, ex))
print(isinstance(ex3, ex))


class MyError(Exception):
    pass


ex4 = MyError()
print(isinstance(ex4, ex))

try:
    raise SyntaxError
except Exception:
    print("!!")