def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Side lengths cannot be negative")  # Проверка сторон
    return a * b
    # Возвращает площадь прямоугольника по полученным двум сторонам 
def perimeter(a, b):
    if a < 0 or b < 0:
        raise ValueError("Side lengths cannot be negative")  # Проверка сторон
    return a*2 + b*2
    # Возвращает периметр прямоугольника по полученным двум сторонам 
