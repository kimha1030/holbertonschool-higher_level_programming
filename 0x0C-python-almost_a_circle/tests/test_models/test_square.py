#!/usr/bin/python3
"""Unittest for Square
"""
import unittest
import pep8
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Test for Square"""
    def test_square_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_size_neg(self):
        """Test size"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_string(self):
        """Test x string"""
        with self.assertRaises(TypeError):
            Square(10, "Holberton")

    def test_y_neg(self):
        """Test y neg"""
        with self.assertRaises(ValueError):
            Square(10, 2, -2)

    def test_x_tuple(self):
        """Test tuple"""
        with self.assertRaises(TypeError):
            Square(10, (1, 2), 6, 4)

    def test_x_neg(self):
        """Test x neg"""
        with self.assertRaises(ValueError):
            Square(10, -7, 2, 5)

    def test_y_list(self):
        """Test y list"""
        with self.assertRaises(TypeError):
            Square(10, 3, [1, 2, 3], 4)

    def test_size_bool(self):
        """Test size bool"""
        with self.assertRaises(TypeError):
            Square(True, 8, 3, 4)

    def test_comb_height_y(self):
        """Test height y"""
        with self.assertRaises(ValueError):
            Square(10, -5, (-8, 2))

    def test_comb_size_y(self):
        """Test size y"""
        with self.assertRaises(TypeError):
            Square([1, 2, 3], 2, -5)

    def test_size_float(self):
        """Test size float"""
        with self.assertRaises(TypeError):
            Square(2.5, 8, 3, 4)

    def test_y_dict(self):
        """Test y dict"""
        with self.assertRaises(TypeError):
            Square(5, 8, {"name": 2}, 4)

    def test_x_float_neg(self):
        """Test x float"""
        with self.assertRaises(TypeError):
            Square(5, -3.8)

    def test_str1(self):
        """Test str"""
        squ_8 = Square(4, 6, 2)
        self.assertEqual(squ_8.__str__(), "[Square] (18) 6/2 - 4")

    def test_str2(self):
        """Test str"""
        squ_9 = Square(4, 8)
        self.assertEqual(squ_9.__str__(), "[Square] (19) 8/0 - 4")

    def test_str3(self):
        """Test str"""
        squ_9 = Square(4)
        self.assertEqual(squ_9.__str__(), "[Square] (20) 0/0 - 4")

    def test_x_dict(self):
        """Test x dict"""
        with self.assertRaises(ValueError):
            squ_11 = Square(20, 30, 40, 50)
            squ_11.update(y=-3, x="hola")

    def test_update_menor(self):
        """Test update"""
        squ_12 = Square(4, 8)
        squ_12.update(12, 34, 2, 1)
        self.assertEqual(squ_12.__str__(), "[Square] (12) 1/0 - 34")

    def test_update_height(self):
        """Test update"""
        with self.assertRaises(ValueError):
            squ_13 = Square(1, 5)
            squ_13.update(2, -2, 3, 4)

    def test_update_x(self):
        """Test update"""
        with self.assertRaises(ValueError):
            squ_16 = Square(5, 6)
            squ_16.update(2, 1, -3, 4)

    def test_square(self):
        """Test square"""
        with self.assertRaises(ValueError) as test1:
            Square(10, 2, -3, 5)
        self.assertTrue("y must be >= 0" in str(test1.exception))

    def test_display(self):
        """Test display"""
        r = Square(2, 2, 3)
        display_example = "\n\n\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)
