"""__bases__ - кортеж из объектов суперклассов"""


class A:
    a = "a"


class B:
    b = "b"


class C(A, B):
    c = "c"


print(C.__bases__)
print(A.__bases__)
print(B.__bases__[0].__bases__)




