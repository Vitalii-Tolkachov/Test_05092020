# Входные данные
# Пользователь вводит строку.

text = input("enter a sting: ")

# Выходные данные
# Воспользуйтесь одним print(), но при этом выводите с новой строки:
# Сначала выведите третий символ этой строки. //text[2]
# Во второй строке выведите предпоследний символ этой строки. //text[-2]
# В третьей строке выведите первые пять символов этой строки. //text[:5]
# В четвертой строке выведите всю строку, кроме последних двух символов. //text[:-2]
# В пятой строке выведите все символы с четными индексами //text[::2]
# (считая, что индексация начинается с 0, поэтому символы выводятся, начиная с первого символа). //text[1::2]
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.  //text[-1::-1]
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего. //text[-1::-2]
# В девятой строке выведите все символы строки через один в обратном порядке, начиная с предпоследнего. //text[-2::-2]
# В десятой строке выведите все символы в обратном порядке без первого и последнего элемента. //text[-2:0:-1]
# Ну, и напоследок выведите длину данной строки.
# PS: Выловите исключения, если введённая строка слишком короткая. Какого типа исключение надо выловить?
a = True
while a:
    try:
        print(text[2], text[-2], text[:5], text[:-2], text[::2], text[1::2], text[::-1], text[::-2], text[-2::-2], text[-2:0:-1], len(text), sep="\n")
        a = False
    except IndexError:
        text = input("enter a sting: ")
