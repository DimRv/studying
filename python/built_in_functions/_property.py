"""
property(fget=None, fset=None, fdel=None, doc=None)

Свойства - механизм, который позволяет автоматически запускать методы при обращениях к атрибутам экземпляра.
В какой то степени это альтернатива __getattr__ и __setattr__/
По умолчанию к атрибутам класса есть полный доступ на чтение, запись и удаление.
Свойства могут использоваться для ограничения доступа, при отсутствии сеттера или делитера
Возвращает новый объект property.
Обычно геттер у property вычисляет какое-то значение

"""

help(property)

print('Пример1'.center(60, "-"))


class Test:
    """Обычный доступ к атрибутам """
    test = 'test'

    def __init__(self):
        self.x = 'start'


t = Test()
print(t.test, t.x)
t.test = 'new'
t.x = 'second'
t.new_attr = 'new_attr'
print(t.x)
del t.x, t.test

print('Пример2'.center(60, "-"))


class Test2:
    """Свойство защищено от перезаписи и удаления при отсутствии сеттера и делитера"""
    @property
    def x(self):
        return 'test'

t2 = Test2()
print(t2.x)
print(Test2.x, type(Test2.x))
print(dir(Test2.x))
#t2.x = '1' - ошибка
#del t2.x - ошибка

print('Пример3'.center(60, "-"))


class Test3:
    """Свойство защищено только от удаления"""

    def __init__(self):
        self.n = 'start'

    @property
    def x(self):
        return self.n + ' get'

    @x.setter
    def x(self, x):
        self.n = x + ' set'


t3 = Test3()
print(t3.x)
t3.x = 'end'
print(t3.x)
t3.n = 'some'
print(t3.x)

