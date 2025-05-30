"""
collections.deque(iter) - коллекция данных очередь. Похожи на списки, данные можно добавить слева и справа
collections.Counter(iter) - счетчик кол-ва значений.
collections.defaultdict() - обычный словарь, но с заданным типом данных для хранения новых элементов
collections.OrderedDict() - словарь, который помнит порядок ключей при добавлении
collections.namedtuple() - кортеж к элементам которого можно обращаться по имени
"""

import collections
help(collections)
print([i for i in dir(collections)])
d = collections.deque()
print(d)
d1 = collections.deque(['a', 'b', 'c'])
print(d1)
d1.append("d")
d1.appendleft("_")
d1.pop()
d1.popleft()
print(d1)
c = collections.Counter(['a', 'b', "c", "a", "a", "b"])
print(type(c), c)
print(c.most_common(2))
dd = collections.defaultdict(set)
print(dd)
for i in range(5):
    dd[i].add(i)
print(dd)
od = collections.OrderedDict(sorted({"ccc": 3, "bb": 2, "aa": 11}.items()))
print(od)
od = collections.OrderedDict(sorted({"ccc": 3, "bb": 2, "aa": 11}.items(), key=lambda t: t[1]))
print(od)
od = collections.OrderedDict(sorted({"ccc": 3, "bb": 2, "aa": 11}.items(), key=lambda t: len(t[0])))
print(od)
nt = collections.namedtuple('nt', ['a', 'b', 'c'])
print(nt)
hello = nt(5, 7, 43)
print(hello.c)


