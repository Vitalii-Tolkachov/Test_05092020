# Задание 4 (на создание тестов c помощью unittest)
# Создайте наборы тестов на тестирование класса ITEmployee, который вы реализовали в Задании 1
# (или Employee, или Person в зависимости до куда вы дошли в выполнении Задания 1).

import unittest
from home_work_5.ex_1 import ITEmployee


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.ite = ITEmployee("John Smith", 1990, "Programmer", 2, 500)

    def test_name(self):
        self.assertEqual(self.ite.get_name(), "John")

    def test_surname(self):
        self.assertEqual(self.ite.get_surname(), "Smith")

    def test_age_in_2000(self):
        self.assertEqual(self.ite.age_in(2000), 10)

    def test_position_2(self):
        self.assertEqual(self.ite.get_position(), "Junior Programmer")

    def test_position_4(self):
        self.ite.experience = 4
        self.assertEqual(self.ite.get_position(), "Middle Programmer")

    def test_position_7(self):
        self.ite.experience = 7
        self.assertEqual(self.ite.get_position(), "Senior Programmer")

    def test_salary_default(self):
        self.assertEqual(self.ite.salary, 500)

    def test_salary_50(self):
        self.ite.bonus_salary(50)
        self.assertEqual(self.ite.salary, 550)

    def test_skill_default(self):
        self.assertEqual(self.ite.skills, [])

    def test_add_skill(self):
        self.ite.add_skill("tester")
        self.assertEqual(self.ite.skills, ["tester"])

    def test_add_skills(self):
        self.ite.add_skills(["good", "bad"])
        self.assertEqual(self.ite.skills, ["good", "bad"])


if __name__ == '__main__':
    unittest.main()
