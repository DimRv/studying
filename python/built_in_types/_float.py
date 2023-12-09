"""
float - десятичные числа в python
Свойства в основном такие же как у int, но не поддерживают длинную арифметику
Но обладают ограниченной точностью, при необходимости лучше использовать Decimal и Fraction
"""

help(float)
a1 = 0.1
print(type(a1))
print(a1+a1+a1+a1+a1+a1+a1+a1+a1+a1)
print((0.5).as_integer_ratio())
print((1.0).is_integer())
print((1.1).hex())
print(float.fromhex('0x1.5000000000000p+3'))
