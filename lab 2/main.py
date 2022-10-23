from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pymorphy2


def main():
  morph = pymorphy2.MorphAnalyzer()
  blue = morph.parse("синий")[0].inflect({'gent'})
  green = morph.parse("зелёный")[0].inflect({'gent'})
  red = morph.parse("красный")[0].inflect({'gent'})
  rect = Rectangle(blue.word, 20, 19)
  circle = Circle(green.word, 20)
  square = Square(red.word, 20)
  print(rect)
  print(circle)
  print(square)


if __name__ == "__main__":
    main()	
