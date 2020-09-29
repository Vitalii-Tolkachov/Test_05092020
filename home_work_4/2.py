# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов (неопределенное количество).
# Учитываем, что может быть повторяющиеся значения аргументов.

def my_func(*args):
    if args == ():
        print("negative")
        return
    my_l = list(args)
    my_l.sort()
    tmp = my_l[0]
    for item in my_l:
        if item > tmp:
            print(item)
            return
    print("negative")
    return


my_func(8, 8, 7, 6, 5, 4, 3, 2, 1, 1)
my_func(-1, -2, -3, -4)
my_func()
my_func(2, 2)
my_func(2, 2, 2, 2, 2, 2)

