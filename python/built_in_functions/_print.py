"""
print(*args, sep=' ', end='\n', file=None, flush=False)

Выводит значения переданных аргументов *args функции на стандартный поток вывода sys.stdout"""

help(print)
print(*['a', 'b', 'c'], sep='->')

with open('print_test', 'a') as f:
    print('new string', file=f)
    print('new string 2', file=f)