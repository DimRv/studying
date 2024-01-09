"""
any(iterable)

Возвращает True, если какой-нибудь объект вернет True для bool() в итерируемом объекте"""

print(any(['', None, False, []]))
print(any(['', None, False, [3]]))
