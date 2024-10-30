"""
Последовательность Коллатца называют "простейшая из неразрешенных проблем математики

Не зависимо от начального числа, последовательность Коллатца всегда заканчивается 1
"""


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


value = int(input("Введите любое число: "))

collatz_list = [value]

while value != 1:
    value = collatz(value)
    collatz_list.append(value)

print(collatz_list)
