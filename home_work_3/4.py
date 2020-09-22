# У вас есть список чисел.
# Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

while bool(numbers):
    print(numbers.pop(0))


# ** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?
word = "hello hello"

while bool(word):
    print(word[0])
    word = word[1:]

# Напишите цикл, который выводит на экран и удаляет элементы списка
# от самого маленького до самого большого, пока он не останется пустым.
numbers = [23, 77, 12, 4, 45, 90]

# while bool(numbers):
#     tmp = numbers[0]
#     for item in numbers:
#         if item < tmp:
#             tmp = item
#     print(numbers.pop(numbers.index(tmp)))

while numbers:
    print(min(numbers))
    numbers.remove(min(numbers))

# ** Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

numbers = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]

cnt = [0, 0]
tmp = numbers[0]

for item in numbers:
    if item == 0:
        print(max(cnt))
        break
    if item == tmp:
        cnt[0] += 1
    else:
        if cnt[0] > cnt[1]:
            cnt[1] = cnt[0]
        tmp = item
        cnt[0] = 1

