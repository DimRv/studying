"""
ascii(obj) -> str

Встроенная функция ascii возвращает строковой представление объекта, переданного в качестве аргумента, в котором все
не ASCII символы заменены их Unicode эквивалентами.

В переданном объекте должен быть реализован метод __repr__
"""
print(ascii('test'))
print(ascii('Тест'))
print(ascii('He sayed: "Поехали!"'))


class Test:
    def __init__(self):
        self.test = 'test Тест'

    def __repr__(self):
        return self.test


t = Test()
print(ascii(t))
