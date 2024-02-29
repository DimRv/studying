"""Пример средств инспекции содержимого объектов"""


def class_tree(cls, indent = 1):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        class_tree(supercls, indent+4)


def instance_tree(inst):
    print(f"Tree of {inst}")
    class_tree(inst.__class__, 3)


class InstanceInfo:
    """Использование __dict__ как инструмент инспекции объекта"""
    def __attr_info(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f"\t{attr} = {self.__dict__[attr]}\n"
        return result

    def __str__(self):
        return f"<Instance of {self.__class__.__name__}, id:{id(self)}>\n" \
               f"{self.__attr_info()}"


class ClassInfo:
    """Инспекция объекта с помощью dir()"""
    def __attr_info(self):
        result = ''
        for attr in dir(self):
            if attr.startswith("__") and attr.endswith("__"):
                result += f'\t{attr}\n'
            else:
                result += f"\t{attr} = {getattr(self, attr)}\n"
        return result

    def __str__(self):
        return f"<Instance of {self.__class__.__name__}, id:{id(self)}>\n" \
               f"{self.__attr_info()}"


class ListTree:

    def __get_attr_info(self, obj, indent=0):
        space = "\t" * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith("__") and attr.endswith("__"):
                result += f"{space}{attr} -> {type(getattr(obj, attr))}\n"
            else:
                result += f"{space}{attr} = {getattr(self, attr)}\n"
        return result

    def __get_class_info(self, cls, indent):
        line = '\t' * indent
        if cls not in self.__visited:
            self.__visited.add(cls)
            attr_info = self.__get_attr_info(cls, indent)
            sup_info = ""
            for sup_cls in cls.__bases__:
                sup_info += self.__get_class_info(sup_cls, indent+1)
            return f"{line}<Class: {cls.__name__}, id: {id(cls)}>\n" \
                   f"{attr_info}\n{sup_info}\n"
        else:
            return f"\n See {cls.__name__} above\n"

    def __str__(self):
        self.__visited = set()
        attr_info = self.__get_attr_info(self, 0)
        cls_info = self.__get_class_info(self.__class__, 1)
        return f'<Instance of {self.__class__.__name__}, id: {id(self)}>\n' \
               f'{attr_info}\n{cls_info}\n'






if __name__ == '__main__':
    print("classTree".center(100, '-'))
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

    print("InstanceInfo".center(100, '-'))

    class Super:
        def __init__(self):
            self.sup_data = '00101011'

        def test(self):
            pass

    class Test(Super, InstanceInfo):
        def __init__(self):
            Super.__init__(self)
            self.data = '01010110'

    t = Test()
    print(t)

    print("InstanceInfo".center(100, '-'))

    class Super:
        def __init__(self):
            self.sup_data = '00101011'

        def test(self):
            pass

    class Test(Super, ClassInfo):
        def __init__(self):
            Super.__init__(self)
            self.data = '01010110'


    t = Test()
    print(t)

    print("ListTree".center(100, '-'))

    class Test(Super, ListTree):
        def __init__(self):
            Super.__init__(self)
            self.data = '01010110'


    t = Test()
    print(t)


    class Test(list, ListTree):
        pass
    t = Test()
    print(t)

