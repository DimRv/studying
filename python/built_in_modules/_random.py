"""
Модуль random содержит инструменты для получения случайных значений
"""

import random

print(dir(random))

# случайный float от 0 до 1
print(random.random())
# случайный in от start до end
print(random.randint(0, 10))
# случайный in от start до end c шагом
print(random.randrange(9, 100, 9))
# случайный элемент из списка
print(random.choice('abcdefg'))
# изменение списка путем перемещения элементов случайным образом
li = [i for i in 'abcdefg']
random.shuffle(li)
print(li)
# создание нового списка из случайных НЕ уникальных элементов
print(random.choices([i for i in 'abcdefg'], k=10))
# создание нового списка из случайных уникальных элементов
print(random.sample([i for i in 'abcdefg'], k=5))
