"""Встроенные в python ключевые слова"""

import keyword
print([i for i in dir(keyword) if not i.startswith("_")])

print(keyword.kwlist)
print(keyword.softkwlist)