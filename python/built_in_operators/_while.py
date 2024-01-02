"""while используется для повторного выполнения блока кода

while выражение:
    блок кода

Блок кода выполняется пока выражение возвращает True
"""

help('while')

print('Пример1')
n=0
while True:
    print("Выполнение кода")
    n += 1
    if n == 5:
        break
else:
    print('Блок else')

print('Пример2')
n=0
while n<5:
    print("Выполнение кода")
    n += 1
else:
    print('Блок else')
