import unittest
from square import area, perimeter

class TestSquareFunctions(unittest.TestCase):
    def test_area_positive(self):
        # Тест площади квадрата с положительной стороной
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3), 9)

    def test_area_zero(self):
        # Тест площади квадрата со стороной 0
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        # Тест площади квадрата с отрицательной стороной
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_positive(self):
        # Тест периметра квадрата с положительной стороной
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3), 12)

    def test_perimeter_zero(self):
        # Тест периметра квадрата со стороной 0
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        # Тест периметра квадрата с отрицательной стороной
        with self.assertRaises(ValueError):
            perimeter(-1)

if __name__ == '__main__':
    unittest.main()
