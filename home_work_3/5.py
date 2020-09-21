# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом (любым),
# то должна выполняться конкатенация, т. е. соединение, строк.
# В остальных случаях введённые числа суммируются.

number1 = input("enter 1 number: ")
number2 = input("enter 2 number: ")

try:
    number_tmp = float(number1)
    number2 = float(number2)
except:
    print(str(number1) + str(number2))
else:
    print(number_tmp + number2)
