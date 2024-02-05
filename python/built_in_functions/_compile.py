"""
compile(source, filename, mode) -> code-object
source - выражение которое должно быть выполнен (str, bytes или AST-object)
filename - файл модуля из которого взята строка кода (str, bytes)
mode - режим выполнения, один из трех вариантов:
    - "single" - обычное выражение
    - 'eval' - однострочный код
    - 'exec' - многострочный код

Встроенная функция compile возвращает объект code, который в дальнейшем может быть выполнен функциями eval или exec
"""
x = 10
test = compile('x', '<string>', 'single')
exec(test)
test = compile('print("res ", 9+4)', '<string>', 'eval')
eval(test)
test = compile('print("res ", 9+4)\nprint("Hi")', 'test', 'exec')
exec(test)

f = open('_abs.py', 'r')
temp = f.read()
f.close()
test = compile(temp, '', 'exec')
exec(test)