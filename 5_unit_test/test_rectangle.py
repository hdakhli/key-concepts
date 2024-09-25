from unittest import TestCase
from rectangle import Rectangle


class TestRectangle(TestCase):
    def test_area(self):
        rectangle1 = Rectangle(2, 4)
        area = rectangle1.area()
        self.assertEqual(8, area)

    def test_perimetre(self):
        rectangle2 = Rectangle(2,4)
        perimetre = rectangle2.perimeter()
        self.assertEqual(12, perimetre)