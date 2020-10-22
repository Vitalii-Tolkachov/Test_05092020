import math


# Задание 2 (на создание новых классов)
# Создать классы
# 1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
class Room:

    def __init__(self, s1=0, s2=0):
        self.s1 = s1
        self.s2 = s2

    def __str__(self):
        return f"<Room object: s1 {self.s1} \ns2 {self.s2}>"

    # Методы:
    # 1.	вычисляем площадь,
    def get_square(self):
        return self.s1 * self.s2

    # 2.	вычисляем периметр.
    def get_perimeter(self):
        return (self.s1 + self.s2) * 2


# 2) Студент (свойства: имя-фамилия, специальность, год начала обучения, список оценок – при создании объекта,
# по умолчанию, пустой список).
class Student:

    def __init__(self, full_name="", profession="", start_year=0, rating=None):
        if rating is None:
            rating = []
        self.full_name = full_name
        self.profession = profession
        self.start_year = start_year
        self.rating = rating

    def __str__(self):
        return f"<Student object: full_name {self.full_name} \nprofession {self.profession}\nstart_year {self.start_year}\nrating {self.rating}>"

    # Методы:
    # 3.	Добавить новую оценку в свойство списка оценок
    def update_rating(self, new_r=0):
        self.rating.append(new_r)

    # 4.	Посчитать средний балл,
    def average_rating(self):
        tmp = 0
        for item in self.rating:
            tmp += item
        return tmp / len(self.rating)

    # 5.	Посчитать сколько лет учится уже студент.
    def get_time_study(self):
        return 2020 - self.start_year


# 3) Точка на карте (свойства: X, Y).
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Point object: x {self.x} \ny {self.y}>"

    # Методы:
    # 1.	Нужно вычислить расстояние до начала координат,
    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # 2.	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
    def get_distance_to_point(self, px=0, py=0):
        return ((self.x - px) ** 2 + (self.y - py) ** 2) ** 0.5

    # 3.	** перевод в другие системы координат
    def get_polar_system(self):
        tmp = [self.get_distance(), math.atan(self.y / self.x)]
        return tmp

# 3) Для всех классов сделайте __str__, чтоб объекты красиво выводились на экран!
#
#



r1 = Room(3, 4)

print(r1.get_perimeter())
print(r1.get_square())

s1 = Student("john", "programmer", 1990, [5, 5, 4, 4])

print(s1.average_rating())
s1.update_rating(3)
print(s1.average_rating())
print(s1.get_time_study())

p1 = Point(3, 4)

print(p1.get_polar_system())
