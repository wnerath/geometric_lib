import unittest
from triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):
    def test_area_positive(self):
        # Тест площади треугольника с положительными основанием и высотой
        self.assertAlmostEqual(area(0, 5), 10.0)
        self.assertAlmostEqual(area(10, 2), 10.0)
        self.assertAlmostEqual(area(3.5, 6), 10.5)

    def test_area_zero_or_negative(self):
        # Тест площади треугольника с нулевым или отрицательным основанием/высотой
        with self.assertRaises(ValueError):
            area(-1, 5)
        with self.assertRaises(ValueError):
            area(4, -2)
        with self.assertRaises(ValueError):
            area(0, 5)

    def test_perimeter_positive(self):
        # Тест периметра треугольника с корректными сторонами
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(6, 8, 10), 24)
        self.assertEqual(perimeter(7.5, 7.5, 7.5), 22.5)

    def test_perimeter_zero_or_negative(self):
        # Тест периметра треугольника с нулевыми или отрицательными сторонами
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)

    def test_perimeter_invalid_triangle(self):
        # Тест периметра треугольника, нарушающего неравенство треугольника
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)  # 1 + 2 = 3, треугольник невозможен
        with self.assertRaises(ValueError):
            perimeter(5, 1, 1)  # 5 > 1 + 1

if __name__ == '__main__':
    unittest.main()
