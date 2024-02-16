#!/usr/bin/python3
"""test_rectangle.py

This module contains unit tests for the /models/test_rectangle.py

Classes it defined:
    - TestBase: Represent test for the class Rectangle in base.py

"""


import os
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj1 = Rectangle(5, 4, 1, 2, 1)
        cls.obj2 = Rectangle(1, 2, 1, 2, 3)

    def tearDown(self):
        pass

    def test___init__with_valid_input(self):
        self.assertEqual(TestBase.obj1.id, 1)
        self.assertEqual(TestBase.obj2.id, 3)

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

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 10)
        r1_dictionary = r1.to_dictionary()

        self.assertEqual(r1_dictionary, {'y': 9, 'x': 1, 'id': 10, 'height': 2, 'width': 10})

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        actual_dictionary = json.loads(json_dictionary)
        expected_dictionary = json.loads('[{"x": 2, "y": 8, "id": 6, "width": 10, "height": 7}]')

        self.assertEqual(actual_dictionary, expected_dictionary)

    def test_to_json_string_with_None_input(self):
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

    def test_to_json_string_with_empty_input(self):
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

    def test_type_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(isinstance(json_dictionary, str), True)

    def test_save_to_file(self):
        r1 = Rectangle(10, 2, 1, 9, 10)
        r2 = Rectangle(10, 7, 2, 8, 6)
        Rectangle.save_to_file([r1, r2])

        file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Rectangle.json')

        assert os.path.exists(file_path), "my_file.json does not exist"

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list)

        self.assertEqual(list_input, list_output)

    def test_create(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(str(r1), str(r2))

    def test_create_with_invalid_input(self):
        dictionary = {"x": 2, "y": 8, "id": 6, "width": "hey", "height": "hey"}

        with self.assertRaises(TypeError):
            r1 = Rectangle.create(**dictionary)

        dictionary = {"x": -2, "y": -8, "id": 6, "width": -3, "height": -4}

        with self.assertRaises(ValueError):
            r1 = Rectangle.create(**dictionary)
