"""Без переданного агрумента - locals.
Если передали obj, то вернет mappingproxy-object obj.__dict__
"""


help(vars)

v1 = vars()
print(v1, type(v1))


class Test:
    attr = 'val'


v2 = vars(Test)
print(v2, type(v2))