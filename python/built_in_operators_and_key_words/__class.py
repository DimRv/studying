"""__class__ - связь экземпляра со своим классом"""


class A:
    a = "a"


class B(A):
    b = "b"


i_b = B()
print(i_b.__class__)
print(B.__class__)
print(A.__class__)

