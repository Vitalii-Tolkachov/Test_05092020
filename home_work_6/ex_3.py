# Задание 3
# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
# Рядом со словом укажите сколько раз оно встречалось в тексте
with open('many_words.txt', 'r', encoding="utf-8") as f:
    with open('sort_words.txt', 'w', encoding="utf-8") as wf:
        a = str(f.read()).split()
        b = [x.strip(".,-!?") for x in a]
        b.sort()
        a = []
        for item in b:
            if item not in a:
                print(item, b.count(item), file=wf)
                a.append(item)
