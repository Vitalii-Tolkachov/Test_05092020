#Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает)
# 0 (если все числа различны).

number1 = input("1 number is:")
number2 = input("2 number is:")
number3 = input("3 number is:")

if number1 == number2 and number1 == number3:
    print("3")

elif number1 == number2 or number1 == number3 or number2 == number3:
    print("2")

else:
    print("0")
