# Задание 1 (на создание классов)
# Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
# 1) Person (два свойства:
# 1. теперь full_name пусть будет свойством, а не функцией
# (одно поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»),
# а свойств name и surname нету,
# 2. год рождения).

class Person:

    def __init__(self, full_name="", birth=0):
        # * (дополнительное) Можете в конструкторе проверить,
        # что в год рождения меньше или равно 2020 (текущий год – для продвинутых),
        # но больше или равно 1900. Если нет, вызывайте исключение
        assert 1900 <= birth <= 2020
        # * (дополнительное) Можете в конструкторе проверить,
        # что в full_name передаётся строка, состоящая из двух слов, если нет, вызывайте исключение 😊
        assert len(full_name.split()) == 2
        self.birth = birth
        self.full_name = full_name

# Реализовать методы, которые:
# 1.	выделяет только имя из full_name
    def get_name(self):
        return self.full_name.split()[0]

# 2.	выделяет только фамилию из full_name;
    def get_surname(self):
        return self.full_name.split()[1]
# 3.	вычисляет сколько лет было/есть/исполнится в году,
# который передаётся параметром (obj.age_in(year));
# если не передавать параметр, по умолчанию, сколько лет в этом году;
    def age_in(self, year=2020):
        return(year - self.birth)

    def __str__(self):
        return f"<Person object: {self.full_name} \nBirth {self.birth}>"


# 2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
# * (дополнительное) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊

class Employee(Person):

    def __init__(self, full_name="", birth=0, position="", experience=0, salary=0):
        super().__init__(full_name, birth)
        self.experience = experience
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"<Employee object: {self.full_name} \nBirth {self.birth} \n{self.get_position()} \nSalary {self.salary}>"

    # Реализовать новые методы:
    # 1.	возвращает должность с приставкой, которая зависит от опыта работы:
    # Junior — менее 3 лет,
    # Middle — от 3 до 6 лет,
    # Senior — больше 6 лет.
    # Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>.
    # Если, например, у вас объект имел должность “programmer” с опытом 2 года,
    # метод должен вернуть “Junior programmer”
    def get_position(self):
        if 0 <= self.experience < 3:
            return f"Junior {self.position}"
        elif 3 <= self.experience < 6:
            return f"Middle {self.position}"
        elif self.experience > 6:
            return f"Senior {self.position}"
        else:
            return "Position error"



# 2.	метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.
    def bonus_salary(self, bonus=0):
        self.salary += bonus

"""
# 3) ITEmployee (наследуемся от Employee)
"""
"""    тренировочный класс
        наследуется от класса Employee
"""
class ITEmployee(Employee):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def __str__(self):
        return f"<ITEmployee object: {self.full_name} \nBirth {self.birth} \n{self.get_position()} \nSalary {self.salary} \nSkills {self.skills}>"
    """
    # 1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill (см. презентацию)
    """
    """ Метод который добавляет новый навык экземпляру класса """
    def add_skill(self, new_skill):
        self.skills.append(new_skill)
    """
    # 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
    """
    """ Метод который добавляет несколько новых навыков экземпляру класса """
    def add_skills(self, new_skills):
        self.skills += new_skills



# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill, или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill
# 4) Для всех классов сделайте __str__, чтоб объекты красиво выводились на экран!


# 5) Создайте строки документации к классу и ко всем его методам!






p1 = Person("John Smith", 1990)
e1 = Employee("Jane Smith", 1990, "Programmer", 2, 500)
i1 = ITEmployee("Jack Smith", 1990, "Programmer", 2, 500)
e1.bonus_salary(33)
print(e1.full_name)
print(e1.birth)
print(e1.position)
print(e1.experience)
print(e1.salary)

print(i1.skills)
i1.add_skill("skill1")
print(i1.skills)
i1.add_skills(["skill2", "skill3"])
print(i1.skills)

print(e1.get_position())

print(p1)
print(e1)
print(i1)

print(i1.get_name())


