"""test_base.py

This module contains unit tests for the models/base.py

Classes it defined:
    - TestBase: Represent test for the class Base in base.py

"""


import unittest
from base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        self.obj1 = Base();
        self.obj2 = Base(5);

    def tearDown(self):
        pass

    def test___init__(self):
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 5)
