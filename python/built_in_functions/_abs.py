"""
abs(obj) -> float/int

Встроенная функция abs() возвращает абсолютное значение объекта переданного в аргументе. Обычно передают объект типа
int, float или complex, но может быть любой другой объект в котором реализован метод __abs__.

Абсолютное значение числа x (или модуль x) в математике это расстояние от начальной точки координат до точки x,
значение не может быть отрицательным.
"""
print(abs(-4)) # вернет int
print(abs(-5.3)) # вернет float
print(abs(-3 - 4j)) # вернет float - расстояние от точки (0, 0) до точки (-3, -4)


class Coordinate:
    def __init__(self, x, y):
        self.point = (x, y)

    def __abs__(self):
        return (self.point[0] ** 2 + self.point[1] ** 2) ** 0.5


coord = Coordinate(-3, -4)
print(abs(coord)) # вернет результат выполнения метода __abs__
