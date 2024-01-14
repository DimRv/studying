"""
all(iterable) -> bool

Встроенная функция all(iter) возвращает True если все значения в переданном итерируемом объекте iter вернут True для
bool(). Если iter пуст, то all вернет True.
Функция bool() возвращает True для всех не пустых последовательностей и возвращает Falsе для 0 и None"""

print(all([-3, 's', True, print]))
print(all([]))
print(all((None, 'False')))
print(all([x > 0 for x in range(-1, 5)]))