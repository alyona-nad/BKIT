'''класс "Прямоугольник"'''
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    # get-method
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        self.fc = FigureColor()
        self.fc.colorproperty = color

    # вычисление площади
    def square(self):
        return self.width * self.height

    # вывод данных фигуры
    def __repr__(self):
        return '{} {} цвета с шириной {} и высотой {} имеет площадь {}'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.square()
        )
