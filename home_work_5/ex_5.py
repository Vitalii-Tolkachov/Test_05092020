from home_work_5.ex_3 import only_alpha

# Задание 5 (на генераторы списков и словарей – тема на самостоятельное изучение)
# 1)	Создайте список 2 в степени N, где N от 0 до 20.
my_list = [2**x for x in range(0, 21)]

# 2)	У вас есть список целых чисел. Создайте новый список остатков от деления на 3 чисел из исходного списка.
my_list2 = [x % 3 for x in my_list]

# 3)	У вас есть список, в котором могут быть разные типы данных. Создайте новый список только чисел из этого списка.
my_list3 = [1, 2, 3, 4, 5, "ggg", "tyu", "abcd57ef.gh", True, 6, 7, 8, -3, 8.6]
my_list4 = [x for x in my_list3 if type(x) == int or type(x) == float]


# 4)	У вас есть список, в котором могут быть разные типы данных. Создайте новый список только строк,
# при этом удалите усе небуквенные символы из них.
# Воспользуйтесь функцией из предыдущего задания (импортируйте её из другого своего файла)
my_list5 = [only_alpha(x) for x in my_list3 if type(x) == str]

# 5)	У вас есть словарь – характеристик человека. Ключи, например, “name”, “surname”, “age”, “position”, “address”, “skills”.
# - Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.
# - Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного словаря было строкой.
# Значения нового словаря должны быть переведены в нижний регистр и удалены всё небуквенные символы из них.
my_dict = {"name": "John", "surname": "Smith", "age": 20, "position": "pr0grammer", "@ddress": "k1ev", "skills": "tester"}
my_dict2 = {k: type(my_dict[k]) for k in my_dict}
my_dict3 = {k: only_alpha(my_dict[k]).lower() for k in my_dict if type(my_dict[k]) == str}


print(my_list)
print(my_list2)
print(my_list4)
print(my_list5)
print(my_dict2)
print(my_dict3)
