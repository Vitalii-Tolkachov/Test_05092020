# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
#  (Football Coach)
my_string = "We! are not what we should be!\nWe are not what we need to be.\nBut at least we are not what we used to be\n (Football Coach)"

# Посчитайте сколько слов в тексте

print(len(my_string.split()))
# Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)

my_string2 = my_string.split()

for item in my_string2:
    my_string2[my_string2.index(item)] = item.strip(",.!()\n")

print(my_string2)

# Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
my_list = sorted(my_string2)
for item in my_list:
    print(item, end=" ")

# Усложнённое * (можно сначала его не делать):
# Посчитать, сколько раз встречается каждое слово.
# (Подсказка: создавать словарь, где ключи — это слова из текста,
# а в значениях подсчитываем количество «встречаний» этого слова)
# Слова с большой буквы и с маленькой это все равно одно и тоже слово 😊

my_dict = dict()
for item in my_list:
    my_list[my_list.index(item)] = item.upper()
    if my_dict.get(item, 0) == 0:
        my_dict[item] = 1
    else:
        my_dict[item] += 1

print("\n", my_dict)
