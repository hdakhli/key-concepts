from unittest import TestCase
from shape import Square, Circle


class TestShape(TestCase):

    def test_square_area(self):
        # Arrange
        carre = Square(2)

        # Act
        area = carre.area()
        fact = carre.fact()

        # Assert
        self.assertEqual(4, area)
        self.assertEqual("Squares have each angle equal to 90 degrees.", fact)

    def test_circle_area(self):
        # Arrange
        circle = Circle(2)

        # Act
        area = circle.area()
        fact = circle.fact()

        # Assert
        self.assertEqual(12.566370614359172, area)
        self.assertEqual("I am a two-dimensional shape.", fact)
