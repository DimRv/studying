"""__dict__ - словарь в котором содержатся атрибуты и их значения"""


class A:
    a = "a"


print(A.__dict__.keys())


class B(A):
    b = 'b'


print(B.__dict__.keys())
i_b = B()
print(i_b.__dict__.keys())
