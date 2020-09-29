# Оформляем в функции наши задания с урока и предыдущих ДЗ:
# Пишем функцию, которая попросит ввести число.
# Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.
# * Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не простым input!
def func1():
    while 1:
        number = input("enter number: ")
        try:
            number = float(number)
        except:
            print("data is not a number")
        else:
            return number


# Пишем функцию, которая попросит пользователя ввести слово
# (строка из буквенных символов без пробелов в середине, а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое слово.
def func2():
    while True:
        mess = input("enter no space word: ")
        mess = mess.strip()
        if ' ' not in mess and mess.isalpha():
            return mess


# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.
def func4(side1, side2, side3):
    if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:
        return True
    else:
        return False


# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами и если существует,
# то возвращает тип треугольника
# Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный),
# Versatile triangle (разносторонний)
# или не треугольник (Not a triangle).
def func5(a, b, c):
    if not func4(a, b, c):
        return "Not a triangle"
    else:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or a == c or b == c:
            return "Isosceles triangle"
        else:
            return "Versatile triangle"


# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2).
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# *Считайте четыре действительных числа от пользователя
# (перед запуском функции, не внутри функции)
# и выведите результат работы этой функции.
number1 = func1()
number2 = func1()
number3 = func1()
number4 = func1()
print(distance(number1, number2, number3, number4))

# print(func1())
print(func2())
print(func5(3, 3, 3))
print(func5(3, 3, 5))
print(func5(4, 6, 5))
print(func5(1, 1, 3))
