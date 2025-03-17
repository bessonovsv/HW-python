import math


def sguare(side):
    return math.ceil(side * side)


side = float(input("Сторона квадрата: "))
print(f"Площадь квадрата: {sguare(side)}")
