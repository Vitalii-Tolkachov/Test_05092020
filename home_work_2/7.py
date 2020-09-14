# Дано три числа. Упорядочите их в порядке возрастания.
# Программа должна считывать три числа a, b, c,
# затем программа должна менять их значения в переменных так,
# чтобы стали выполнены условия a <= b <= c. Затем программа выводит тройку a, b, c.

number1 = input("enter number 1:")
number2 = input("enter number 2:")
number3 = input("enter number 3:")

if number2 < number1:
    number1, number2 = number2, number1

if number3 < number1:
    number1, number3 = number3, number1

if number3 < number2:
    number2, number3 = number3, number2

number_case = [number1, number2, number3]

print(number_case)

