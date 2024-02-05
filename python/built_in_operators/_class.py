"""
class ClassNane(parents):
    code


inst = ClassName() - экземпляр класса ClassName


Свойства ООП:
0. Имя класса обычно пишется с большой буквы и ВерблюжьейНотацией
1. Основные инструменты - классы ,грубо говоря, объект, содержащий функции. Можно сказать это фабрики по созданию
экземпляров. Экземпляры - отдельный объект представитель класса, создаются при вызовах объекта-класса
2. Классы создаются по средствам оператора class.
3. Классы поддерживают наследование - механизм настройки и многократного применения кода. Наследование свойств от
родительского класса - суперкласса.
4. Композиция - классы содержат в себе другие объекты.
5. Поддержка множества экземпляров
6. Собственное пространство имен
7. Перегрузка операций - переопределение поведения объекта при участии в различных встроенных операциях
8. Операции = внутри class создают атрибуты. Операция объект-экземпляр.атрибут - запускает процедуру поиска атрибута
в иерархии наследования: экземпляр -> класс -> в суперклассах
9. Методы - функции, объявленные внутри объекта-класса, которые обрабатывают экземпляры класса через self
10. При создании экземпляра вызывется метод __init__(self), в котором описываются свойства каждого экземпляра
11. Полиморфизм - способность различного взаимодействия с операторами в зависимости от типа объекта.
12. Инкапсуляция - сокрытие атрибутов и методов объекта от вмешательства из вне.
13. Суперклассы передаются внутри (parents)
"""


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
