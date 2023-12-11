"""Возвращает True, если какой-нибудь объект вернет True для bool() в итерируемом объекте"""


help(any)
print(any(['', None, False, []]), any(['', None, False, [3]]))