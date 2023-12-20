"""Возвращает enumerate object, который можно представить как список: [(index, value), ...]"""

help(enumerate)
print(enumerate([1, 2, 3]))
for i, j in enumerate([1, 3, 4]):
    print(i, j)

print(dict(enumerate([1, 2, 3])))