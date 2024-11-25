def area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Base and height must be positive")  # Проверка на положительные значения
    return a * h / 2
    # Возвращает площадь треугольника во полученным стороне и высоте 
def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")  # Проверка на положительные значения
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triangle inequality violated")  # Проверка неравенства треугольника
    return a + b + c
    # Возвращает периметр треугольника по полученным трем сторонам 
