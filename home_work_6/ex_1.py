import requests
# Задание 1 (Обязательное всем, кроме части со звёздочкой!!!!)
# Тестовое приложение с REST API: http://pulse-rest-testing.herokuapp.com/
base_url = "http://pulse-rest-testing.herokuapp.com/"
book_dict= {"title": "Zhizn s brevnom","author": "Papa Karlo"}
# Создаём один скрипт:

# Создаём книгу POST /books/, вы запоминаете его id.
r = requests.post(base_url + "books", data=book_dict)
body = r.json()
print(body)
book_id = body['id']
book_title = body['title']
print(book_id)
# Проверяете, что она создалась и доступна по ссылке GET/books/[id]
r2 = requests.get(base_url + f"books/{book_id}")
if r2.status_code == 200:
    print("book acсess ok")
# Проверяете, что она есть в списке книг по запросу GET /books/
r2 = requests.get(base_url + "books")
body = r2.json()
for item in body:
    if item['id'] == book_id:
        print("book created")

# Изменяете данные этой книги методом PUT /books/[id]/
book_dict= {"title": "Zhizn s brevnom2","author": "Papa Karlo"}
r2 = requests.put(base_url + f"books/{book_id}", data=book_dict)
print(r2.status_code)
print(r2.json())

# Проверяете, что она изменилась и доступна по ссылке /books/[id]
body2 = r2.json()
r2 = requests.get(base_url + f"books/{book_id}")
if r2.status_code == 200 and body2['title'] == book_dict['title']:
    print("book changed ")
# Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
r2 = requests.get(base_url + "books")
body = r2.json()
for item in body:
    if item['title'] == body2['title']:
        print("book exist with new data")
# Удаляете эту книгу методом DELETE /books/[id].
r3 = requests.delete(base_url + f"books/{book_id}")
r2 = requests.get(base_url + "books")
print(r2.status_code)
print(r2.json())
# Все проверки делать программно, а не глазами, т.е. проверить,
# что в теле response данные такие же как в вашем исходном словаре путём сравнения значений в словарях!!!!!
# Второй скрипт:
# тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с книгой, которая уже должна существовать.
# Создайте книгу заранее в этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то другой может удалить.
# Третий скрипт:
# Поэкспериментируйте создавать книги и роли с неправильными данными. Посмотрите тело и статус код ответов.
# Попробуйте создать роль с ссылкой на книгу, которой нет. Посмотрите тело и статус код response.
# ** Попробуйте воспользоваться http.client вместо requests. Ощутите разницу
role_dict= {"id": "1000", "name": "karlo","type": "man", "level": 5, "book": 1}
r4 = requests.get(base_url + "roles")
body = r4.json()
print(body)
r5 = requests.post(base_url + "roles", data=role_dict)
print(r5.status_code)