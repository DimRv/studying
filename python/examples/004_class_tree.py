"""Пример демонстрации иерархии наследования"""


def class_tree(cls, indent = 1):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        class_tree(supercls, indent+4)


def instance_tree(inst):
    print(f"Tree of {inst}")
    class_tree(inst.__class__, 3)


if __name__ == '__main__':
    class A:
        pass


    class B(A):
        pass


    class C(A):
        pass


    class D(B, C):
        pass


    class E:
        pass


    class F(D, E):
        pass


    instance_tree(B())
    instance_tree(F())
