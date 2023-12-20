"""Встроенная функция format возвращает __format__(spec) объекта

format(obj, spec) -> obj.__format__(spec)

spec - [fill[align][sign][#][0][width][grouping][.prec][type]
"""
help(format)
help('FORMATTING')

print("fill+align+width".center(60, "-"))
print(format('Hello', "*^30"))
print(format('Hello', ".>30"))
print(format('Hello', "_<30"))
print(format(-30, "=30"))

print("sign".center(60, "-"))
print(format(5, '+'))
print(format(-5, '+'))
print(format(5, '-'))
print(format(-5, '-'))
print(format(5, ' '))
print(format(-5, ' '))

print("#-alernative-form".center(60, "-"))
#FOR int, float
print(format(5, 'b'))
print(format(5, '#b'))

print("grouping".center(60, "-"))
print(format(1000000, ','))
print(format(1000000, '_'))

print("prec".center(60, "-"))
print(format(1.125125125, ',.3')) #s-format, поэтому кол-во символов
print(format(1.125125125, ',.3f'))

print("type".center(60, "-"))
print(format('123', 's'))
print(format(5, 'b'))
print(format(97, 'c')) #unicode символ
print(format(5, 'e'))
print(format(5, 'E'))
print(format(5, 'f'))
print(format(5, 'F'))
print(format(5, 'g'))
print(format(5, 'G'))
print(format(8, 'o'))
print(format(16, 'x'))
print(format(.9, 'n'))
print(format(.1, '.0%'))
