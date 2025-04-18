import math
def sguare(side):
    area = side * side
    return math.ceil(area)
side=float(input("Сторона квадрата:"))
print(f"Площадь квадрата:{sguare(side)}")