"""Отображение словарь - неупорядоченная последовательность именованных объектов"""

help(dict)
print([i for i in dir(dict) if not i.startswith('_')])

d1 = {
    'name': 'Dmitriy',
    'surname': 'Rvantsov',
    'something': None
}

print(d1, type(d1))
print('name' in d1, 'Dmitriy' in d1)
del d1['something']
d1['name'] = 'Denis'
print(d1, d1['name'])
d1 |= {'city': 'SPB'}
print(d1, len(d1))

d2 = d1.copy()
print(d2.clear(), d2)
print(d1.copy())
print(d1.fromkeys(['name']), d1)
print(d1.get('surname'))
print(d1.items())
print(d1.keys())
print(d1.pop('surname'), d1)
print(d1.popitem(), d1)
print(d1.update({'surname': 'Rvantsov'}))
print(d1.values())
