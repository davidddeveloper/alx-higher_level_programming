"""test_base.py

This module contains unit tests for the models/base.py

Classes it defined:
    - TestBase: Represent test for the class Base in base.py

"""


import unittest
import sys
sys.path.append("/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models")
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
