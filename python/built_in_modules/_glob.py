"""
glob - для поиска каталогов и файлов по регулярному выражению

* - произвольное кол-во символов
? - один символ
[] - диапазон символов

"""
import glob
print(dir(glob))

result = glob.glob('./?shelve*')
print(result)
result = glob.glob('./shelve*')
print(result)
