"""
pickle - соленый огурец или мариновать

Преобразует python-объекты из ОЗУ в строки байтов для хранения на ПЗУ

Основные функции:

pickle.dump(obj, file, protocol=None, *, fix_imports=True) - записывает сериализованный объект в файл.
Дополнительный аргумент protocol указывает используемый протокол. По умолчанию равен 3 и именно он рекомендован для
использования в Python 3 (несмотря на то, что в Python 3.4 добавили протокол версии 4 с некоторыми оптимизациями).
В любом случае, записывать и загружать надо с одним и тем же протоколом.

pickle.dumps(obj, protocol=None, *, fix_imports=True) - возвращает сериализованный объект.
Впоследствии вы его можете использовать как угодно.

pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict") - загружает объект из файла.

pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict") - загружает объект из потока байт
"""

import pickle

print(dir(pickle))

data = {
    'nums': [1, 1.1, 5+3j],
    'strings': ('hello', 'world'),
    'bools': {True, False}
}

with open('pickle_test', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)


with open('pickle_test', 'rb') as pickle_file:
    data_read = pickle.load(pickle_file)

print(data)
print(data_read)