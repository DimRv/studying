"""
try:
    block_try - выполнение блока и отслеживание возникновений исключений
except ExceptObject1:
    block_ExceptObject1 - выполнится если возникнет ExceptObject1
except (ExceptObject2, ExceptObject3):
    block_ExceptObject1 - выполнится если возникнет ExceptObject2 или ExceptObject3
except (ExceptObject4, ExceptObject5) as ins:
    block_ExceptObject1 - выполнится если возникнет ExceptObject4 или ExceptObject5 и позволяет работать с экземпляром
...
except ExceptObjectN:
    block_ExceptObjectN - выполнится если возникнет ExceptObjectN
else:
    block_else - выполнится если не возникло исключений
finally:
    block_finally - выполняется в любом случае


Исключения - события способные изменить поток управления в программе.

Операторы для работы с исключениями:

try - выполнение блока кода в котором могут возникнуть исключения и перехват их
except Exception - обработка возникшего исключения
else - если исключений не было
finally - выполнение кода после обработки всех исключений ес
raise - создание собственного исключения
assert - создание условного исключения

Стандартная обработка ошибок - остановка программы и вывод ошибки: имя объекта исключения и трассировка стека: список
всех строк и функций, которые были активны на момент возникновения исключения. Далее происходит очистка памяти, то есть
обратно к коду, где возникло исключение вернутся нельзя

При try интерпретатор запоминает текущий контекст программы для возврата к нему.
При наличии исключений происходит поиск первого совпадения в except

Обычно применяется там где могут возникнуть ошибки, например, открытие файлов или обращение к сокетам
Серверы желательно должны иметь возможность обрабатывать ошибки
"""

help('try')

print('Пример 1. Операторы try/except'.center(80, '-'))
test = 'Hello'
#print(test[7]) - выведет ошибку IndexError
try:
    test[7]
except IndexError:
    print('Возникло исключение, а здесь его обработка!')
    print('Out of range!')
print("Возвращение в стандартный поток")




print('Пример 2. Оператор raise'.center(80, '-'))
a = 5
b = 7
try:
    result = a - b
    if result < 0:
        raise IndexError
except IndexError:
   print("Значение не может быть отрицательным. Проверьте как так получилось")


print('Пример 3. Пользовательские исключения'.center(80, '-'))
class Minus(Exception): pass
try:
    result = a - b
    if result < 0:
        raise Minus()
except Minus:
   print("Значение не может быть отрицательным. Проверьте как так получилось")

print('Пример 4. Пользовательские исключения'.center(80, '-'))
a = 5
b = 6
try:
    result = a - b
    if result < 0:
        raise Minus()
except Minus:
    print("Значение не может быть отрицательным. Проверьте как так получилось")
finally:
    print('Действия после обработки исключений')
print('Продолжение основного потока')

print('Пример 4. Функции'.center(80, '-'))
class ZeroError(Exception): pass

def newDivision(a, b):
    if b == 0:
        raise ZeroError()
    else:
        return int(a / b)

try:
    print(newDivision(4, 2))
    #print(newDivision(4, 0))
except ZeroError:
    print('Infinitive')
else:
    print('No errors')
