"""
collections.deque(iter) - коллекция данных как linked List
collections.Counter(iter) - счетчик кол-ва значений

"""

import collections

print([i for i in dir(collections)])
d = collections.deque()
print(d)
d1 = collections.deque(['a', 'b', 'c'])
print(d1)
d2 = collections.deque({'a': 'a', "b": "b"})
print(d2)
d1.append("d")
d1.appendleft("_")
print(d1)
c = collections.Counter(['a', 'b', "c", "a", "a", "b"])
print(type(c), c)

