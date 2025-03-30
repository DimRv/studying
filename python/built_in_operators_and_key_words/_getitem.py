"""__getitem__ выполняется при операция iter[], iter[:], in """


class MyIter:
    def __init__(self, i):
        self.iterable = i

    def __getitem__(self, item):
        if isinstance(item, int):
            return f"Item {item} will return: {self.iterable[item]}"
        else:
            return f"Item {item} with params {item.start, item.stop, item.step} will return: {self.iterable[item]}"


my = MyIter("Hello, World")
print(my[0])
print(my[:3])
print([i for i in my])
