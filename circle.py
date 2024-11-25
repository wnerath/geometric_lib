import math
# Импортирует библиотеку math чтобы использовать функцию math.pi для числа пи

def area(r):
    if r < 0:
        raise ValueError("Radius cannot be negative") # Проверка радиуса
    return math.pi * r * r
   
    # Возвращает площадь окружности по полученному радиусу
    
def perimeter(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")  # Проверка радиуса
    return 2 * math.pi * r

    # Возвращает периметр окружности по полученному радиусу

