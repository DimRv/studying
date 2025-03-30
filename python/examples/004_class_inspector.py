def class_tree(cls, indent = 0):
    if cls.__name__ == 'object':
        return None;
    print(f"{indent * ' '}class {cls.__name__} has keys in dict: {[k for k in cls.__dict__.keys() if not k.startswith('__')]}")
    for super_class in cls.__bases__:
        class_tree(super_class, indent + 3)


def instance_tree(obj):
    print(f"{obj} has keys in dict: {[k for k in obj.__dict__]}")
    class_tree(type(obj))


if __name__ == "__main__":
    class A:
        a = "a"
        def a_method(self):
            pass
    class B:
        b = "b"
    class C(A, B):
        c = 'c'

    print(f"{'*' * 40}CLASS_INSPECT{'*' * 40}")
    for cls in (C, type([]), type(True), type(1.2), type(None), type("str")):
        class_tree(cls)
        print("*" * 40)
    print(f"{'*' * 40}INSTANCE_INSPECT{'*' * 40}")
    for obj in (C(),):
        instance_tree(obj)
        print("*" * 40)




