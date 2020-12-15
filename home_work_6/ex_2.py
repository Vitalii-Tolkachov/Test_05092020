# Задание 2

def generate_some_text(cnt=1, txt="la", mode=0):
    t = ""
    while cnt:
        t += txt
        cnt -= 1
    if mode == 0:
        print(t)
    else:
        f = open('text.txt', 'w')

        print(t, "test text", file=f)
        f.close()
    return t
# Задания из класса про работу с файлами на слайдах 4, 8, 10, 11:
# 1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл
# (кто сделал с помощью методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)

f = open('text.txt', 'w')
print(generate_some_text(cnt=5, mode=1), file=f)
f.close()

handle = open("ex_1.py", "r", encoding="utf-8")
handle2 = open("text2.txt", "w")
for line in handle:
    print(line.rstrip("\n") + "!")
    print(line.rstrip("\n") + "!", file=handle2)
handle.close()
handle2.close()

f = open('no_numbers_file.txt', 'r', encoding="utf-8")
try:
    num = int(f.read())
except ValueError:
     print("convert error")
else:
     print("I did it")
finally:
    f.close()

f = open('numbers_file.txt', 'r', encoding="utf-8")
try:
    num = int(f.read())
except ValueError:
    print("convert error")
else:
    print("I did it")
finally:
    f.close()
# 2. А теперь воспользуйтесь менеджером контекста для файлов (with … as).

with open('numbers_file.txt', 'r', encoding="utf-8") as f:
    num = int(f.read())
    print("I did it")
