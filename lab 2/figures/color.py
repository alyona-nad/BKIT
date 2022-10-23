'''класс "Цвет фигуры"'''


class FigureColor:
    def __init__(self):
        self._color = None

    @property
    # get-метод
    def colorproperty(self):
        return self._color

    @colorproperty.setter
    # set-метод
    def colorproperty(self, value):
        self._color = value
