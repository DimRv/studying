"""
shelve -полка
Shelve модуль предназначен для хранения python-объектов в файлах, доступ к объектам осуществляется как для словарей

Используется pickle и БД dbm
"""

import shelve

print(dir(shelve))

db = shelve.open('shelve_test')
data = {
    'nums': [1, 1.1, 5+3j],
    'strings': ('hello', 'world'),
    'bools': {True, False}
}

db['data'] = data
data_read = db['data']
db.close()

print(data)
print(data_read)
