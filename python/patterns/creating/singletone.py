"""
Пример паттерна Singletone.
Паттерн подразумевает создание одного экземпляра"""


class A:
    """В обычном классе каждый экземпляр это разные объекты"""
    a = 'test'


a = A()
b = A()
print(a is b)


class Single:
    """В Singletone все экземпляры это один и тот же объект"""
    __param = None

    def __new__(cls, *args, **kwargs):
        if not cls.__param:
            cls.__param = super().__new__(cls, *args, **kwargs)
        return cls.__param


a = Single()
b = Single()

print(a == b)

