# Создайте список строк:
my_list = ["hello", "my", "name", "is", "Vitalii", "world"]

# 1.	Выведите 3-е с конца слово из списка.
print(my_list[-3])

# 2.	Выведите 1-ю букву второго слова из списка.
print(my_list[1][0])

# 3.	Выведите последнюю букву последнего слова из списка.
print(my_list[-1][-1])

# 4.	Добавьте в конец списка еще одно слово.
my_list.append("word")
print(my_list)

# 5.	Вставьте в середину списка еще одно слово.
my_list.insert(int(len(my_list) / 2), "middle")
print(my_list)

# 6.	Удалите первое слово из списка.
my_list.pop(0)
print(my_list)

# 7.	Удалите слово «world» из списка, если оно есть в списке.
my_list.remove("world")
print(my_list)
