#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
import pep8
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Test for Rectangle"""
    def test_rectangle_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pos_width(self):
        """Test width"""
        rect_1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_1.width, 1)

    def test_pos_height(self):
        """Test height"""
        rect_2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_2.height, 2)

    def test_pos_x(self):
        """test x"""
        rect_3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_3.x, 3)

    def test_pos_y(self):
        """test y"""
        rect_4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_4.y, 4)

    def test_y_neg(self):
        """Test y neg"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_y_string(self):
        """Test y string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 2, "Holberton")

    def test_x_neg(self):
        """Test x neg"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -2, 5)

    def test_x_tuple(self):
        """Test x tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2), 4)

    def test_height_neg(self):
        """Test height negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, -7, 2, 5)

    def test_height_list(self):
        """test height list"""
        with self.assertRaises(TypeError):
            Rectangle(10, [1, 2, 3], 3, 4)

    def test_width_neg(self):
        """test width"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 7, 2, 5)

    def test_width_bool(self):
        """test width bool"""
        with self.assertRaises(TypeError):
            Rectangle(True, 8, 3, 4)

    def test_comb_height_x(self):
        """test comb height"""
        with self.assertRaises(ValueError):
            Rectangle(10, -5, (-8, 2))

    def test_comb_width_y(self):
        """Test comb width"""
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], 2, 4, -5)

    def test_width_float(self):
        """Test width float"""
        with self.assertRaises(TypeError):
            Rectangle(2.5, 8, 3, 4)

    def test_x_dict(self):
        """Test x dict"""
        with self.assertRaises(TypeError):
            Rectangle(5, 8, {"name": 2}, 4)

    def test_y_float_neg(self):
        """Test y float"""
        with self.assertRaises(TypeError):
            Rectangle(5, 8, 2, -3.4)

    def test_area_1(self):
        """Test area"""
        rect_6 = Rectangle(4, 5)
        self.assertEqual(rect_6.area(), 20)

    def test_area_2(self):
        """Test area 2"""
        rect_6 = Rectangle(3, 5, 6, 7)
        self.assertEqual(rect_6.area(), 15)

    def test_str(self):
        """test str"""
        rect_8 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(print(rect_8), "[Rectangle] (12) 2/1 - 4/6")

    def test_str(self):
        """test str"""
        rect_9 = Rectangle(4, 8, 6)
        self.assertEqual(rect_9.__str__(), "[Rectangle] (10) 6/0 - 4/8")

    def test_str(self):
        """test str"""
        rect_9 = Rectangle(4, 8)
        self.assertEqual(rect_9.__str__(), "[Rectangle] (8) 0/0 - 4/8")

    def test_x_dict(self):
        """test x dict"""
        with self.assertRaises(ValueError):
            rect_11 = Rectangle(20, 30, 40, 50)
            rect_11.update(y=-3, x="hola")

    def test_update_menor(self):
        """test update menor"""
        rect_12 = Rectangle(4, 8)
        rect_12.update(12, 34, 2, 1)
        self.assertEqual(rect_12.__str__(), "[Rectangle] (12) 1/0 - 34/2")

    def test_update_mayor(self):
        """test update mayor"""
        rect_13 = Rectangle(4, 8, 3, 1)
        rect_13.update(12, 34)
        self.assertEqual(rect_13.__str__(), "[Rectangle] (12) 3/1 - 34/8")

    def test_update_height(self):
        """Test update height"""
        with self.assertRaises(ValueError):
            rect_13 = Rectangle(1, 5)
            rect_13.update(2, 2, 3, -3)

    def test_update_x(self):
        """Test update"""
        with self.assertRaises(ValueError):
            rect_16 = Rectangle(5, 6)
            rect_16.update(2, 1, -3, 4)

    def test_rect(self):
        """Test Rectangle"""
        with self.assertRaises(ValueError) as test1:
            rect17 = Rectangle(10, 2, -3, 5, 19)
        self.assertTrue("x must be >= 0" in str(test1.exception))

    def test_display(self):
        """Test display"""
        r = Rectangle(3, 2)
        display_example = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)
