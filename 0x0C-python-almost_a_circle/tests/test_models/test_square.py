#!/usr/bin/python3
"""test_square.py

This module contains unit tests for the /models/test_rectangle.py

Classes it defined:
    - TestBase: Represent test for the class Rectangle in base.py

"""


import unittest
from square import Square

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(5, 5, 6, 5)

    def test_with_valid_input(self):
        self.assertEqual(TestBase.s1.id, 4)

    def test___init___with_invalid_input(self):
        with self.assertRaises(TypeError):
            s2 = Square("hey", 3, 5, 8)
            s2 = Square(5, 3, "hey", 8)
            s2 = Square(5, 3, 5, "hey")
            s2 = Square(4, "hey", 20, 8)

        with self.assertRaises(ValueError):
            s2 = Square(5, 3, 5, -1)
            s2 = Square(5, 3,-25, 1)
            s2 = Square(-5, 3, 5, 1)
            s2 = Square(-5, 3, 5, 1)

    def test____init__set_height_and_y_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.s1.height = "hey"
            TestBase.s1.height = None
            TestBase.s1.y = "hey"
            TestBase.s1.y = None

        with self.assertRaises(ValueError):
            TestBase.s1.height = 0
            TestBase.s1.height = -1
            TestBase.s1.y = 0
            TestBase.s1.y = -1

    def test___init__set_width_and_x_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.s1.width = "hey"
            TestBase.s1.x = "hey"
            TestBase.s1.x = None

        with self.assertRaises(ValueError):
            TestBase.s1.width = 0
            TestBase.s1.width = -2
            TestBase.s1.x = 0
            TestBase.s1.x = -2

    def test_area(self):
        result = TestBase.s1.area()
        self.assertEqual(result, 25)

    def test___str__(self):
        self.assertEqual(str(TestBase.s1), "[Square] (5) 5/6 - 5")

    def test_update_with_args_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.s1.update(True, 6, 2, 1, 12)
            TestBase.s1.update(4, 6, "hey", 1, 12)

        with self.assertRaises(ValueError):
            TestBase.s1.update(4, 6, -3, 1, 12)
            TestBase.s1.update(4, -2, 3, 1, 12)
            TestBase.s1.update(4, 2, 0, 1, -1)
            TestBase.s1.update(4, 0, 3, 1, 1)

    def test_update_with_kwargs_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.s1.update(width="hey")
            TestBase.s1.update(height="hey")
            TestBase.s1.update(x=None)
            TestBase.s1.update(y=None)
            TestBase.s1.update(x="Hey")
            TestBase.s1.update(y="hey")

        with self.assertRaises(ValueError):
            TestBase.s1.update(width=0)
            TestBase.s1.update(height=0)
            TestBase.s1.update(width=-1)
            TestBase.s1.update(height=-5)
            TestBase.s1.update(x=-1)
            TestBase.s1.update(y=-2)

    def test_to_dictionary(self):
        s3 = Square(10, 2, 1)
        s3_dictionary = s3.to_dictionary()
        self.assertEqual(s3_dictionary, {'id': 5, 'x': 2, 'size': 10, 'y': 1})
