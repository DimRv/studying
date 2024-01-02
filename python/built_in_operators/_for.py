"""Используется для итерации внутри последовательностей

for переменная in последовательность:
else:
    код здесь выполнится только если не будет break
для последовательности применяется iter()
"""

help('for')
print('Пример 1')
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("!")

print('Пример 2')
for i in range(5):
    print(i)
else:
    print("!")

print('Пример 3')
class Test:
    def __init__(self):
        self.pos = 0
        self.test = 'test'

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.test):
            self.pos = 0
            raise StopIteration
        else:
            value = self.test[self.pos]
            self.pos += 1
            return value
t = Test()
for i in t:
    print(i)
print()
for i in t:
    print(i)
