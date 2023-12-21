"""Возвращает поток (stream), тип зависит от mode

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file - str or byte - имя файла
mode - режим:
    'r' - read
    'w' - write
    'x' - creating and writing
    'a' - adding
    'b' - binary mode
    't' - text mode
    '+' - add reading + writing
"""

help(open)
with open('open_test') as f:
    print(f.read())
with open('open_test', 'rb') as f:
    print(f.read())
