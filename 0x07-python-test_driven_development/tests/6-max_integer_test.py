#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_pos_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 6, 3, 2]), 6)

    def test_neg_int(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-6, -8, -3, -2]), -2)

    def test_comb_int(self):
        self.assertEqual(max_integer([2, -4, 6]), 6)
        self.assertEqual(max_integer([-4, 8, 2, 6]), 8)

    def test_none_list(self):
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([]), None)

    def test_pos_float(self):
        self.assertEqual(max_integer([1.2, 2.4, 5.6]), 5.6)
        self.assertEqual(max_integer([1.5, 2.2, 8.3]), 8.3)

    def test_neg_float(self):
        self.assertEqual(max_integer([-1.2, -2.4, -5.6]), -1.2)
        self.assertEqual(max_integer([-5.2, -7.4, -7.3]), -5.2)

    def test_comb_float(self):
        self.assertEqual(max_integer([2.2, -2.4, -5.6]), 2.2)
        self.assertEqual(max_integer([2.5, -6.4, -3.6]), 2.5)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_err_list(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})
        with self.assertRaises(TypeError):
            max_integer(5, 9)
        with self.assertRaises(TypeError):
            max_integer([3, 6], [4, -6])
        with self.assertRaises(TypeError):
            max_integer([7, 6], (4.2, -6))
