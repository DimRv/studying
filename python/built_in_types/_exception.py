"""
Exception - объект используемый при создании собственных исключений.

IndexError - объект класса
IndexError() - уже экземпляр класса IndexError

BaseException -> Exception -> ArithmeticError -> ZeroDivision (математические ошибки)
BaseException -> Exception -> LookupError -> IndexError, KeyError (ошибки индексирования)

exception.args - кортеж из параметров переданных классу исключению
"""

# Все Исключения наследуются от Exception:
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
print(type(ex4), type(MyError))
print(isinstance(ex4, ex))

try:
    raise SyntaxError
except Exception:
    print("!!")


class SubErr1(MyError):
    pass


class SubErr2(MyError):
    pass


try:
    raise SubErr2
except MyError:
    print("Обработано исключение вызванное подклассом")