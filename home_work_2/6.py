# Даны три числа a, b, c.
# Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.

side1 = int(input("enter 1 side of triangle: "))
side2 = int(input("enter 2 side of triangle: "))
side3 = int(input("enter 3 side of triangle: "))

if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
    print("YES")

else:
    print("NO")