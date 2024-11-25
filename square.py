def area(a):
    if a < 0:
        raise ValueError("Side length cannot be negative")  # Проверка стороны
    return a * a
    # Возвращает площадь квадрата по полученной стороне, при a = 3 вернет 9


def perimeter(a):
    if a < 0:
        raise ValueError("Side length cannot be negative")  # Проверка стороны
    return 4 * a
    # Возвращает периметр квардрата по полученной стороне, при a = 3 вернет 12
