"""test_base.py

This module contains unit tests for the /models/test_rectangle.py

Classes it defined:
    - TestBase: Represent test for the class Rectangle in base.py

"""


import unittest
from rectangle import Rectangle

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj1 = Rectangle(5, 4, 1, 2, 1)
        cls.obj2 = Rectangle(1, 2, 1, 2, 3)
        cls.obj3 = Rectangle(1, 2)

    def tearDown(self):
        pass

    def test___init__with_valid_input(self):
        self.assertEqual(TestBase.obj1.id, 1)
        self.assertEqual(TestBase.obj2.id, 3)
        self.assertEqual(TestBase.obj3.id, 1)

    def test___init__set_height_and_y_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.obj1.height = "hey"
            TestBase.obj1.height = None
            TestBase.obj1.y = "hey"
            TestBase.obj1.y = None

        with self.assertRaises(ValueError):
            TestBase.obj1.height = 0
            TestBase.obj1.height = -1
            TestBase.obj1.y = 0
            TestBase.obj1.y = -1

    def test___init__set_width_and_x_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.obj1.width = "hey"
            TestBase.obj1.x = "hey"
            TestBase.obj1.x = None

        with self.assertRaises(ValueError):
            TestBase.obj1.width = 0
            TestBase.obj1.width = -2
            TestBase.obj1.x = 0
            TestBase.obj1.x = -2

    def test__init__default_value(self):
        obj5 = Rectangle(5, 5)
        self.assertEqual(obj5.id, 2)

    def test_area(self):
        result = TestBase.obj1.area()
        self.assertEqual(result, 20)

    def test___str__(self):
        self.assertEqual(str(TestBase.obj1), "[Rectangle] (1) 1/2 - 5/4")

    def test_update_with_args_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.obj1.update(True, 6, 2, 1, 12)
            TestBase.obj1.update(4, 6, "hey", 1, 12)

        with self.assertRaises(ValueError):
            TestBase.obj1.update(4, 6, -3, 1, 12)
            TestBase.obj1.update(4, -2, 3, 1, 12)
            TestBase.obj1.update(4, 2, 0, 1, -1)
            TestBase.obj1.update(4, 0, 3, 1, 1)

    def test_update_with_kwargs_with_invalid_input(self):
        with self.assertRaises(TypeError):
            TestBase.obj1.update(width="hey")
            TestBase.obj1.update(height="hey")
            TestBase.obj1.update(x=None)
            TestBase.obj1.update(y=None)
            TestBase.obj1.update(x="Hey")
            TestBase.obj1.update(y="hey")

        with self.assertRaises(ValueError):
            TestBase.obj1.update(width=0)
            TestBase.obj1.update(height=0)
            TestBase.obj1.update(width=-1)
            TestBase.obj1.update(height=-5)
            TestBase.obj1.update(x=-1)
            TestBase.obj1.update(y=-2)
