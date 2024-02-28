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

Когда файл открывается в текстовом режиме, чтение его данных автоматически декодирует его содержимое.
Запись подразумевает автоматическое кодирование перед передачей в файл.
Когда файл открывается в двоичном режиме, чтение не декодирует данные. А передает объект bytes
Запись тоже без кодирования

Изображения, данные передаваемые по сети это двоичные данные
Текстовые файлы также содержат d в начале BOM - bytes order mark в кодировках utf-16 или utf-32

str.encode(), bytes(S, encoding) - из str в bytes
bytes.decode() и str(b, encoding) - из bytes в str

стандартная кодировка utf8, но open использует из модуля locale и sys cp1252
sys.getdefaultencoding()
locale.getprefferendenencoding(False)


"""

help(open)
with open('open_test') as f:
    print(f.read())
with open('open_test', 'rb') as f:
    print(f.read())
with open('pixel.jpg', 'rb') as f:
    print(f.read())
