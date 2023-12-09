import decimal, fractions

"""
В python числа представлены следующими типами:
- bool
- int
- float
- complex
- decimal (доп модуль)
- fraction (доп модуль)
- set
"""
t1 = True
t2 = 10
t3 = .1
t4 = 30 + 4j
t5 = decimal.Decimal(3.4123)
t6 = fractions.Fraction(8, 10)
t7 = {3, 5, 6, 7, 3, 5, 6}
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))
print(t6, type(t6))
print(t7, type(t7))
