"""Выполняет блок кода, переданного в качестве параметра"""

help(exec)

c = """
print('Hello')
for i in 'Hello':
    print(i)
"""
exec(c)
