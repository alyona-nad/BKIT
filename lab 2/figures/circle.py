'''класс "Круг"'''
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from math import pi


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    # get-method
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, r):
        self.radius = r
        self.fc = FigureColor()
        self.fc.colorproperty = color

    # вычисление площади
    def square(self):
        return round(pi * (self.radius ** 2), 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} имеет площадь {}'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.radius,
            self.square()
        )
