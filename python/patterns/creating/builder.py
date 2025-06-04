"""
Пример паттерна Builder.
Паттерн позволяет создавать экземпляры с разным количеством свойств
"""


class Builder:

    def create_color(self, color):
        self.color = color
        return self

    def create_width(self, width):
        self.width = width
        return self

    def create_height(self, height):
        self.height = height
        return self

    def create_depth(self, depth):
        self.depth = depth
        return self


a = Builder().create_color('white').create_width(100).create_height(100).create_depth(10)
b = Builder().create_color('black')

