# 1.	Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 367 и 127.
print((367 ** 2 + 127 ** 2) ** 0.5)

# 2.	Дано двузначное число. Найдите число десятков в нем.
my_number = 57
print(my_number // 10)

# 3.	Дано трёхзначное число. Найдите сумму его цифр.
my_number = 567
my_number = str(my_number)
print(int(my_number[0]) + int(my_number[1]) + int(my_number[2]))

# 4.	Дано целое число n. Выведите следующее за ним чётное число.
my_number = 17
if my_number % 2 == 0:
    print(my_number + 2)
else:
    print(my_number + 1)

# 5.	Дано положительное действительное число X. Выведите его дробную часть.
my_number = 2.567
print(my_number - int(my_number))

# 6.	Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
my_number = 345.678
my_number = str(my_number)
print(my_number[my_number.index(".") + 1])
