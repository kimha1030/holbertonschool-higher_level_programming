#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_pos_width(self):
        rect_1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_1.width, 1)

    def test_pos_height(self):
        rect_2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_2.height, 2)

    def test_pos_x(self):
        rect_3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_3.x, 3)

    def test_pos_y(self):
        rect_4 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_4.y, 4)

    def test_y_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 2, "Holberton")

    def test_x_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -2, 5)

    def test_x_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2), 4)

    def test_height_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -7, 2, 5)

    def test_height_list(self):
        with self.assertRaises(TypeError):
            Rectangle(10, [1, 2, 3], 3, 4)

    def test_width_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 7, 2, 5)

    def test_width_bool(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 8, 3, 4)

    def test_comb_height_x(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -5, (-8, 2))

    def test_comb_width_y(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], 2, 4, -5)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            Rectangle(2.5, 8, 3, 4)

    def test_x_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 8, {"name": 2}, 4)

    def test_y_float_neg(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 8, 2, -3.4)

    def test_area_1(self):
        rect_6 = Rectangle(4, 5)
        self.assertEqual(rect_6.area(), 20)

    def test_area_2(self):
        rect_6 = Rectangle(3, 5, 6, 7)
        self.assertEqual(rect_6.area(), 15)

    def test_display(self):
        rect_7 = Rectangle(3, 5)
        self.assertEqual(rect_7.display(), None)

    def test_display(self):
        rect_10 = Rectangle(3, 5, 2, 1)
        self.assertEqual(rect_10.display(), None)

    def test_str(self):
        rect_8 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(print(rect_8), "[Rectangle] (12) 2/1 - 4/6")

    def test_str(self):
        rect_9 = Rectangle(4, 8, 6)
        self.assertEqual(rect_9.__str__(), "[Rectangle] (10) 6/0 - 4/8")

    def test_str(self):
        rect_9 = Rectangle(4, 8)
        self.assertEqual(rect_9.__str__(), "[Rectangle] (10) 6/0 - 4/8")

    def test_str(self):
        rect_10 = Rectangle(4, 8)
        self.assertEqual(print(rect_10), None)

    def test_x_dict(self):
        with self.assertRaises(ValueError):
            rect_11 = Rectangle(20, 30, 40, 50)
            rect_11.update(y=-3, x="hola")

    def test_update_menor(self):
        rect_12 = Rectangle(4, 8)
        rect_12.update(12, 34, 2, 1)
        self.assertEqual(rect_12.__str__(), "[Rectangle] (12) 1/0 - 34/2")

    def test_update_mayor(self):
        rect_13 = Rectangle(4, 8, 3, 1)
        rect_13.update(12, 34)
        self.assertEqual(rect_13.__str__(), "[Rectangle] (12) 3/1 - 34/8")

    def test_update_height(self):
        with self.assertRaises(ValueError):
            rect_13 = Rectangle(1, 5)
            rect_13.update(0, 2, 3, 4)

    def test_update_height(self):
        with self.assertRaises(ValueError):
            rect_16 = Rectangle(5, 6)
            rect_16.update(2, 1, -3, 4)

    def test_update_mayor(self):
        rect_14 = Rectangle(3, 1)
        rect_14.update(12, 34, 37, 27)
        self.assertEqual(print(rect_14.width), None)

    # Dejar de ultimo por el id
    def test_without_id(self):
        rect_13 = Rectangle(10, 2)
        self.assertEqual(rect_13.id, 12)
