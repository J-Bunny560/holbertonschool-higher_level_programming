#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_function1(self):
        """testing using a three digit integer 100"""
        result = max_integer([1, 2, 3, 4, 5, 6, 100])
        self.assertEqual(result, 100)
    def test_function2(self):
        """testing if list is empty"""
        self.assertIsNone(max_integer([]), None)
    def test_function3(self):
        """ testing if list contains a string"""
        self.assertRaises(TypeError, max_integer, [2, 3, 4, "daniel"])
    def test_function4(self):
        """testing with negative integer"""
        self.assertEqual(max_integer([0, 0, -1]), 0)
    def test_function5(self):
        """testing with float"""
        self.assertEqual(max_integer([2, 4, 4.5]), 4.5)
    def test_function6(self):
        """testing with nested list"""
        self.assertRaises(TypeError, max_integer, ([1, 2, 3, 4, 5, [6, 7, 10]]))