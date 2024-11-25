import unittest
from rectangle import area, perimeter

class TestRectangleFunctions(unittest.TestCase):
    def test_area_positive(self):
        # Тест площади прямоугольника с положительными сторонами
        self.assertEqual(area(1, 2), 2)
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(5, 6), 30)

    def test_area_zero(self):
        # Тест площади прямоугольника с одной из сторон равной 0
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(7, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_negative(self):
        # Тест площади прямоугольника с отрицательными сторонами
        with self.assertRaises(ValueError):
            area(-1, 2)
        with self.assertRaises(ValueError):
            area(3, -4)
        with self.assertRaises(ValueError):
            area(-5, -6)

    def test_perimeter_positive(self):
        # Тест периметра прямоугольника с положительными сторонами
        self.assertEqual(perimeter(1, 2), 6)
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(5, 6), 22)

    def test_perimeter_zero(self):
        # Тест периметра прямоугольника с одной из сторон равной 0
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(7, 0), 14)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_negative(self):
        # Тест периметра прямоугольника с отрицательными сторонами
        with self.assertRaises(ValueError):
            perimeter(-1, 2)
        with self.assertRaises(ValueError):
            perimeter(3, -4)
        with self.assertRaises(ValueError):
            perimeter(-5, -6)

if __name__ == '__main__':
    unittest.main()
