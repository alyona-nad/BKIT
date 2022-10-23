'''класс "Квадрат"'''
from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    # get-method
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, side):
        self.side = side
        super().__init__(color, self.side, self.side)

    # вывод данных фигуры
    def __repr__(self):
        return '{} {} цвета со стороной {} имеет площадь {}'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )
