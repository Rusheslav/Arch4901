from abc import ABC, abstractmethod


class IRectangle(ABC):
    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(IRectangle):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(IRectangle):
    def __init__(self, side):
        self.side = side

    def set_width(self, width):
        self.side = width

    def area(self):
        return self.side * self.side
