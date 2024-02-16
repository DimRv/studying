"""
object - основной type от которого наследуются все другие

От него наследуется 89 встроенных подклассов
"""

help(object)
a = object()
b = object()
print(a, type(a), dir(a))
#a.attr = 'val' - error
print(a == b)


