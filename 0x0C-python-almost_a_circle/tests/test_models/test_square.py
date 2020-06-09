#!/usr/bin/python3
"""Unittest for Square
"""
import unittest
from models.Square import Square


class TestSquare(unittest.TestCase):
    def test_pos_size(self):
        squ_1 = Square(10)
        self.assertEqual(print(squ_1.size), None)

    def test_size_neg(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_string(self):
        with self.assertRaises(TypeError):
            Square(10, "Holberton")

    def test_y_neg(self):
        with self.assertRaises(ValueError):
            Square(10, 2, -2)

    def test_x_tuple(self):
        with self.assertRaises(TypeError):
            Square(10, (1, 2), 6, 4)

    def test_x_neg(self):
        with self.assertRaises(ValueError):
            Square(10, -7, 2, 5)

    def test_y_list(self):
        with self.assertRaises(TypeError):
            Square(10, 3, [1, 2, 3], 4)

    def test_size_bool(self):
        with self.assertRaises(TypeError):
            Square(True, 8, 3, 4)

    def test_comb_height_y(self):
        with self.assertRaises(ValueError):
            Square(10, -5, (-8, 2))

    def test_comb_size_y(self):
        with self.assertRaises(TypeError):
            Square([1, 2, 3], 2, -5)

    def test_size_float(self):
        with self.assertRaises(TypeError):
            Square(2.5, 8, 3, 4)

    def test_y_dict(self):
        with self.assertRaises(TypeError):
            Square(5, 8, {"name": 2}, 4)

    def test_x_float_neg(self):
        with self.assertRaises(TypeError):
            Square(5, -3.8)

    def test_positive(self):
        squ_2 = Square(1, 2, 3, 4)
        self.assertEqual(print(squ_2), None)

    def test_str(self):
        squ_8 = Square(4, 6, 2)
        self.assertEqual(print(squ_8), "(Square) (12) 2/1 - 4/6")

    def test_str(self):
        squ_9 = Square(4, 8)
        self.assertEqual(squ_9.__str__(), "(Square) (10) 6/0 - 4/8")

    def test_str(self):
        squ_9 = Square(4)
        self.assertEqual(squ_9.__str__(), "(Square) (10) 6/0 - 4/8")

    def test_str(self):
        squ_10 = Square(4, 8)
        self.assertEqual(print(squ_10), None)

    def test_x_dict(self):
        with self.assertRaises(ValueError):
            squ_11 = Square(20, 30, 40, 50)
            squ_11.update(y=-3, x="hola")

    def test_update_menor(self):
        squ_12 = Square(4, 8)
        squ_12.update(12, 34, 2, 1)
        self.assertEqual(squ_12.__str__(), "(Square) (12) 1/0 - 34/2")

    def test_update_mayor(self):
        squ_13 = Square(4, 8, 3, 1)
        squ_13.update(12, 34)
        self.assertEqual(squ_13.__str__(), "(Square) (12) 3/1 - 34/8")

    def test_update_height(self):
        with self.assertRaises(ValueError):
            squ_13 = Square(1, 5)
            squ_13.update(0, 2, 3, 4)

    def test_update_height(self):
        with self.assertRaises(ValueError):
            squ_16 = Square(5, 6)
            squ_16.update(2, 1, -3, 4)

    def test_update_mayor(self):
        squ_14 = Square(3, 1)
        squ_14.update(12, 34, 37, 27)
        self.assertEqual(print(squ_14.width), None)

    # Dejar de ultimo por el id
    def test_without_id(self):
        squ_5 = Square(10, 2)
        self.assertEqual(squ_5.id, 3)
