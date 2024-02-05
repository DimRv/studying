"""
while условие:
    блок_кода
else:
    блок_кода_else
блок_кода_после_while

while - оператор многократного выполнения кода.

Блок_кода будет выполняться пока условие возвращает True, соответственно возможно появление бесконечного цикла
если в блоке кода НЕ реализованно изменение параметров условия или break.
Блок_кода_else выполнится только если в цикл завершился не применяя инструкцию break
Внутри блок_кода допускается использование break и continue
"""

help('while')

print('Пример1')
n = 0
while True:
    n += 1
    if n == 3:
        continue
    print(n)
    if n == 5:
        break
else:
    print('Блок else')

print('Пример2')
n = 0
while n < 5:
    print("Выполнение кода")
    n += 1
else:
    print('Блок else')
