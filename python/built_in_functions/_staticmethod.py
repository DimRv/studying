"""Создает статический метод """


class Test:
    attr = 'value'

    def __init__(self):
        self.x = 'test'

    def method(self):
        print(self.x)

    @staticmethod
    def st_method():
        print("It is static")

    @classmethod
    def cl_method(cls):
        print(cls.attr)


t = Test()
print(Test.method(t), type(Test.method))
print(Test.st_method(), type(Test.st_method))
print(Test.cl_method(), type(Test.cl_method))
