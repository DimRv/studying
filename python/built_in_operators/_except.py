"""
try:
    блок кода
except Exception:
    обработка исключения

Оператор except используется для обработки возникших исключений в блоке кода за оператором try

Exception может быть как конкретное исключение, так и целая категория

"""

a = [1]
try:
    b = a[3]
except IndexError:
    b = None

print(b)

try:
    print("!")
    raise SyntaxError

except:
    print('expept all!! IT is BAD')


print("локальная переменная х сама удалится после блока try:")
try:
    raise IndexError()

except IndexError as x:
    print(dir())

print(dir())


