#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Test for Base"""
    def test_base_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_none(self):
        """Test none"""
        base_1 = Base()
        self.assertEqual(base_1.id, 1)
        base_10 = Base()
        self.assertEqual(base_10.id, 2)

    def test_integer(self):
        """Test integer"""
        base_2 = Base(20)
        self.assertEqual(base_2.id, 20)

    def test_float(self):
        """Test float"""
        base_3 = Base(4.3)
        self.assertEqual(base_3.id, 4.3)

    def test_string(self):
        """Test string"""
        base_4 = Base("Hola")
        self.assertEqual(base_4.id, "Hola")

    def test_dict(self):
        """Test dict"""
        base_5 = Base({"Name", "Jhon"})
        self.assertEqual(base_5.id, {"Name", "Jhon"})

    def test_tuple(self):
        """Test tuple"""
        base_6 = Base((1, 2))
        self.assertEqual(base_6.id, (1, 2))

    def test_list(self):
        """Test list"""
        base_7 = Base([1, 2, 3])
        self.assertEqual(base_7.id, [1, 2, 3])
