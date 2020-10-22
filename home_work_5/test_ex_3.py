import unittest
from home_work_5.ex_3 import is_year_leap
from home_work_5.ex_3 import is_triangle_exist
from home_work_5.ex_3 import get_type_of_triangle

class MyTestCase(unittest.TestCase):
    def test_year_0(self):
        self.assertEqual(is_year_leap(0), True)

    def test_year_8(self):
        self.assertEqual(is_year_leap(8), True)

    def test_year_40(self):
        self.assertEqual(is_year_leap(40), True)

    def test_year_100(self):
        self.assertEqual(is_year_leap(100), False)

    def test_year_400(self):
        self.assertEqual(is_year_leap(400), True)

    def test_year_2(self):
        self.assertEqual(is_year_leap(2), False)

    def test_year_399(self):
        self.assertEqual(is_year_leap(399), False)



    def test_triangle_exist_000(self):
        self.assertEqual(is_triangle_exist(0, 0, 0), False)

    def test_triangle_exist_110(self):
        self.assertEqual(is_triangle_exist(1, 1, 0), False)

    def test_triangle_exist_111(self):
        self.assertEqual(is_triangle_exist(1, 1, 1), True)



    def test_type_of_triangle_000(self):
        self.assertEqual(get_type_of_triangle(0, 0, 0), "Not a triangle")

    def test_type_of_triangle_555(self):
        self.assertEqual(get_type_of_triangle(5, 5, 5), "Equilateral triangle")

    def test_type_of_triangle_662(self):
        self.assertEqual(get_type_of_triangle(6, 6, 2), "Isosceles triangle")

    def test_type_of_triangle_000(self):
        self.assertEqual(get_type_of_triangle(2, 3, 4), "Versatile triangle")


if __name__ == '__main__':
    unittest.main()
