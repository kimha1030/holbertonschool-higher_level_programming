#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_none(self):
        base_1 = Base()
        self.assertEqual(base_1.id, 1)
        base_10 = Base()
        self.assertEqual(base_10.id, 2)

    def test_integer(self):
        base_2 = Base(20)
        self.assertEqual(base_2.id, 20)

    def test_float(self):
        base_3 = Base(4.3)
        self.assertEqual(base_3.id, 4.3)

    def test_string(self):
        base_4 = Base("Hola")
        self.assertEqual(base_4.id, "Hola")

    def test_dict(self):
        base_5 = Base({"Name", "Jhon"})
        self.assertEqual(base_5.id, {"Name", "Jhon"})

    def test_tuple(self):
        base_6 = Base((1, 2))
        self.assertEqual(base_6.id, (1, 2))

    def test_list(self):
        base_7 = Base([1, 2, 3])
        self.assertEqual(base_7.id, [1, 2, 3])
