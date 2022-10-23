'''абстрактный класс "Геометрическая фигура", от которого наследуются другие'''
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    # вычисление площади
    def square(self):
        pass
