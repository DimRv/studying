"""Вывод всех встроенных функций"""

functions = [i for i in dir(__builtins__) if i[0] in [chr(j) for j in range(97, 127)]]
print(functions, len(functions))