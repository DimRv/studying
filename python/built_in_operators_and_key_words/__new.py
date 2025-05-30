class A:
    def __new__(cls, *args, **kwargs):
        print("Произошло создание Экземпляра через NEW")
        return object.__new__(cls)

    def __init__(self):
        print("Произошло создание Экземпляра через INIT")

    print("В конце class A")


print(A)
a1 = A()
a2 = A()
print(a1)
print(a2)
