# Создайте словарь характеристик продукта с ключами
#       «title» (значение типа данных str),
#       «price» (значение численного типа данных),
#       «ingredients» (значение – список строк).
my_dict = {'title': "book", 'price': 300, "ingredients": ["pepper", "salt", "tomato"]}
print(my_dict)

# 1.	Добавьте еще одну пару ключ-значение - «description»: какой-то текст
my_dict["description"] = "some text"
print(my_dict)

# 2.	Увеличьте цену на 100.
my_dict["price"] += 100
print(my_dict)

# 3.	Добавьте в список ингредиентов еще один ингредиент.
my_dict["ingredients"].append("cucumber")
print(my_dict)

# 4.	Выделите на экран количество ингредиентов продукта.
print(len(my_dict["ingredients"]))

# 5.	Удалите из словаря значение с ключом «description»
temp = my_dict.pop("description")
print(my_dict)
