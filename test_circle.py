import unittest
import math
from circle import area, perimeter  # Импортируем функции из файла

class TestCircleFunctions(unittest.TestCase):
    def test_area_positive(self):
        # Тест площади окружности с положительным радиусом
        self.assertAlmostEqual(area(1), math.pi, places=5)
        self.assertAlmostEqual(area(2), 4 * math.pi, places=5)
        self.assertAlmostEqual(area(0.5), 0.25 * math.pi, places=5)

    def test_area_zero(self):
        # Тест площади окружности с радиусом 0
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        # Тест площади окружности с отрицательным радиусом (должен быть обработан)
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_positive(self):
        # Тест периметра окружности с положительным радиусом
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=5)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi, places=5)
        self.assertAlmostEqual(perimeter(0.5), math.pi, places=5)

    def test_perimeter_zero(self):
        # Тест периметра окружности с радиусом 0
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        # Тест периметра окружности с отрицательным радиусом (должен быть обработан)
        with self.assertRaises(ValueError):
            perimeter(-1)

if __name__ == '__main__':
    unittest.main()

