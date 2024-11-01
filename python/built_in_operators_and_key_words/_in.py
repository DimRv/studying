"""
obj in iterable

Оператор проверки наличия объекта в последовательности
Вызывает метод __contains__ в объекте или __iter__, а затем __getitem__
"""

print('o' in 'Hello')


class InTest:
    data = 'Hello'

    def __contains__(self, item):
        print('in contains')
        for i in self.data:
            if i == item:
                return True
        return False


i = InTest()
print('o' in i)
