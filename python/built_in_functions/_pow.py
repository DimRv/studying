"""
pow(base, exp, c=Non: a ** b (при c=None) a ** b % c (при с=число только если int)
Возвращает число (int, float), результат возведения числа base в степень exp"""

help(pow)

print(pow(3, 4))
print(pow(2.5, 2))
print("-"*30)
print(3 ** 4)
print(2.5 ** 2)
print("-"*30)
print(pow(3, 4, 5))
#не сработат: print(pow(2.5, 2, 5))
print("-" * 30)
print(3 ** 4 % 5)
print(2.5 ** 2 % 5)

