"""Позволяет скомпилировать код для дальнейшего выполнения exec или eval

compile(source, filename, mode)
source - модуль,  выражение или оператор
filename - для вывода ошибок
mode - exec for module,
        - single for single statement
        - eval for expression
"""

help(compile)

test = compile('+', 'test', 'single')
eval(test)

test = compile('print("res ", 9+4)', 'test', 'eval')
eval(test)

test = compile('print("res ", 9+4)\nprint("Hi")', 'test', 'exec')
exec(test)