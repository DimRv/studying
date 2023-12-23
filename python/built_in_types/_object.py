"""object - основной объект от которого наследуются все другие"""

help(object)
a = object()
b = object()
print(a, type(a), dir(a))
#a.attr = 'val' - error
print(a==b)


