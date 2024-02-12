"""
class ИмяКласса(Суперкласс1,... СуперклассN):
    тело класса
    атрибут = значение
    def метод(self):
        self.атрибут = значение


inst = ClassName() - экземпляр класса ClassName

Оператор class возвращает объект типа type - создание нового типа данных. Это основной объект в Объектно Ориентированном
Программировании (ООП).
Разные определения объектов:
 - коллекции операций, имеющих общее состояние (Питер Венгер)
 - сущности, соединяющие в себе свойства процедур и данных. Процедуры это методы.
 - по сути содержит единицы состояния, объекты могут передать возможность взаимодействия со своим состоянием


Свойства классов и ООП :
0. Имя класса в операторе class обычно пишется с большой буквы и ВерблюжьейНотацией
1. Основные инструменты - классы ,грубо говоря, объекты, содержащие функции. Можно сказать это фабрики по созданию
экземпляров. Экземпляры - отдельный объект представитель класса, создаются при вызовах объекта-класса
2. Классы создаются по средствам оператора class, а тело класса в отличие от функций выполняется сразу
3. Классы поддерживают наследование - механизм настройки и многократного применения кода. Наследование свойств от
родительского класса - суперкласса.
4. Композиция - классы содержат в себе другие объекты.
5. Поддержка множества экземпляров
6. Собственное пространство имен
7. Перегрузка операций - переопределение поведения объекта при участии в различных встроенных операциях
8. Операции = внутри class создают атрибуты. Операция объект-экземпляр.атрибут - запускает процедуру поиска атрибута
в иерархии наследования: экземпляр -> класс -> в суперклассах
9. Методы - функции, объявленные внутри объекта-класса, которые обрабатывают экземпляры класса через self
10. При создании экземпляра вызывается метод __init__(self), в котором описываются свойства каждого экземпляра
11. Полиморфизм - способность различного взаимодействия с операторами в зависимости от типа объекта.
12. Инкапсуляция - сокрытие атрибутов и методов объекта от вмешательства из вне.
13. Суперклассы передаются внутри (parents)
14. @методы - декораторы. Запускаются до выполнения самой функции
15. Делегирование - передача выполнения метода другому методу, например, методу суперкласса
16. Композиция - термин описывающий, что сам объект может содержать в себе другие объекты
17. Псевдозакрытые атрибуты начинаются с __
18. _атрибут - не предназначен для внешнего применения
19. Абстрактным супеклассом называют такой класс который вызывает необъявленный метод, подразумевается что в подклассе
должен быть реализован этот метод. Используется в качестве обобщения классов, когда не может быть спрогнозировано
поведение подкласса.


Специальные атрибуты:
self.__class__ - ссылка экземпляра на класс
cls.__name__ - содержит имя класса
cls.__bases__ - суперклассы
obj.__dict__ - словарь из пары атрибут:значение


Методы перегрузки операций:
__new__ -> obj - выполняетcя при создании объекта-экземпляра, возвращает объект для __init__
__init__ - выполняется при инициализации экземпляра объекта, часто называют конструктором
__str__ -> str - при преобразовании объекта к строковому виду (str() или print() )
__repr__ -> str - при выводе как устроен объект-класс, например, при отображении списка в котором есть объекты-классы
__getattr__ -> obj - выполняется при вызове неопределенных атрибутов
__getattribute__ -> выполнятся при обращении ко всем атрибутам
__setattr__ - при изменении атрибута
__delattr__ - при удалении атрибута
__add__ и __radd__ при участии в операции "+"
__iadd__ - +=
__sub__ и __rsub__ при участии в операции "-"
__del__ - при операции del экземпляра
__or__ - при операции |
__call__ - при вызове ()
__getitem__ - индексирование, нарезание, итерация
__setitem__ - присваивание по индексу
__delitem__ - удаление по индексу
__len__ - len()
__bool__ - при операциях проверки истинности, может использоваться __len__
__lt__, __gt__, __le__, __ge__, __eq__, __ne__ - сравнения
__iter__, __next__ -> obj -  iter(), next(), for in, при итерациях
__contains__ - item in obj
__index__ - целочисленное значение hex(), oct()...
__enter__, __exit__ - with obj as var:
__get__, __set__, __del__ - f

При итерации сначала поиск __iter__ если нет, то __getitem__
"""

print("Пример1".center(40, "-"))
class Animal:
    legs = 4


class Dog(Animal):
    voice = 'Гав'

    def __init__(self, color):
        """Отдельные свойства каждого экземпляра"""
        self.color = color

    def say(self):
        """Метод для всех экземпляров Dog"""
        print(self.voice)


Lucy = Dog('Red')
Bobby = Dog('Black')

Lucy.say()
print(Bobby.legs)
print(type(Dog), type(Lucy))
print(Lucy.__dict__)
print(Lucy.__class__.__dict__)