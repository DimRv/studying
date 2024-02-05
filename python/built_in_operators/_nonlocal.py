"""
nonlocal var_name

Используется во вложенной функции для указания внешней переменной и возможностью ее изменения
"""
a = 1000
def test():
    a = 100
    print(a)
    def in_test():
        nonlocal a
        a = 10
    in_test()
    print(a)

test()
print(a)