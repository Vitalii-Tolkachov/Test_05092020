
# Задание 3 (на создание тестов c помощью unittest)
# Создайте наборы тестов на написанные функции из прошлого домашнего задания:
# •	Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
# •	Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.
def is_triangle_exist(side1, side2, side3):
    if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
        return True
    else:
        return False
# •	Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами и если существует,
# то возвращает тип треугольника
# Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный),
# Versatile triangle (разносторонний)
# или не треугольник (Not a triangle).
def get_type_of_triangle(a, b, c):
    if not is_triangle_exist(a, b, c):
        return "Not a triangle"
    else:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or a == c or b == c:
            return "Isosceles triangle"
        else:
            return "Versatile triangle"

def only_alpha(w = ""):
    tmp = ""
    if len(w):
        for item in w:
            if item.isalpha():
                tmp += item
    return tmp

