# 1.	Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)

my_string = "123"
print(my_string.isdigit())
my_string = "abc"
print(my_string.isdigit())

# 2.	Посчитайте сколько у вас пробелов в строке.
my_string = "12  45  hh  rr df q"
print(my_string.count(" "))

# 3.	Посчитайте сколько у вас символов точки '.' в строке.
my_string = "12..45...hh.rr .df ..q"
print(my_string.count("."))

# 4.	Создайте строку "Homework". Преобразуйте её в строку длиной 100 символов,
#       посередине которой исходное слово, а с обоих сторон строка заполнена пробелами.
#       Выведите её на экран. Убедитесь, что у вас 100 символов (посчитайте длину).
my_string = "Homework"
my_string = my_string.center(100, " ")
print(my_string)
print(len(my_string))

# 5.	Сделайте первые буквы слов строки большими (upper case).
my_string = "hello my name is vitalii"
print(my_string.title())
# 6.	Определите заканчивается ли ваша строка подстрокой “ing”.
my_string = "aaasssddd"
print(my_string.endswith("ing"))
my_string = "aaasssddding"
print(my_string.endswith("ing"))

# 7.	Определите индекс первого вхождения символа “a” в вашей строке.
my_string = "park"
print(my_string.index("a"))

# 8.	Разбейте строку на список подстрок по символу пробела.
my_string = "hello my name is vitalii"
my_list = my_string.split(" ")
print(my_list)

# 9.	Пусть у вас строка имеет пробельные символы.
#       Найдите метод, который удаляет пробельные символы вначале и в конце, но не посередине.
my_string = "   hello my name is vitalii   "
print(my_string.strip(" "))
