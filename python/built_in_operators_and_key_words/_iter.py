"""__iter__ dозвращает итерационный объект"""


class MyIter:
    def __init__(self, start, end):
        self.now = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.now == self.end:
            raise StopIteration
        else:
            self.now += 1
            return self.now * 2


my = MyIter(2, 6)
for i in my:
    print(i)
