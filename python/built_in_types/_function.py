"""
def func_name(параметры):
    Блок_кода

func_name(values)

Функция - минипрограмма внутри большой программы
Основная задача группирование строк кода, позволяет избегать повторяемого кода, тем самым устраняя избыточность.

Свойства функций:

1. Функции создаются с помощью оператора def
2. Имя функции func_name начинается с малой буквы и следует правилам именования переменных
3. Параметры (или аргументы) - задают локальные переменные, значения переменных определяются при вызове функции
4. Тело функции содержит код, который выполняется только при вызове функции
5. Вызов функции это операция ()
6. Передача значений при вывозе функции может быть как по позиции, так и по значению агрумента
7. Модуль inspect и getsource() позволяют получить код функции, func_name.__name__ - имя
8. Функции обладают локальной областью видимости.
9. Возможно использование операторов nonlocal или global, поиск
10. переменной осуществляется по правилу LEG (Local, External, Global)
"""
import inspect

print('Пример1'.center(40, '-'))
def func1():
    """Пример пустой функции"""
    pass
print(func1())

print('Пример2'.center(40, '-'))
def func2(num, mul=2):
    """Пример функции с параметром и возвращением значения"""
    return num * mul
print(func2(5))
print(func2(6, mul=3))
print('Пример3'.center(40, '-'))
print(inspect.getsource(func2))
