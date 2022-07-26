#!/usr/bin/python3
""" Unit test for max_integer file """


import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_empty_list(self):
        """check for empty list []"""
        my_list = []
        self.assertIsNone(max_integer(my_list))

    def test_no_args(self):
        """check for no arguments passed """
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """check for only one number in the list"""
        my_list = [5]
        self.assertEqual(max_integer(my_list), 5)

    def test_positive_end(self):
        """check for all positive with max at end"""
        my_list = [2, 10, 8, 36, 14, 60]
        self.assertEqual(max_integer(my_list), 60)

    def test_positive_middle(self):
        """check for all positive with max in middle"""
        my_list = [2, 10, 400, 550, 14, 500, 67]
        self.assertEqual(max_integer(my_list), 550)

    def test_positive_beginning(self):
        """check for all positive with max at beginning"""
        my_list = [600, 20, 8, 36, 24, 50]
        self.assertEqual(max_integer(my_list), 600)

    def test_one_negative(self):
        """check for list with one negative number"""
        my_list = [200, 670, 8, -36, 14, 50]
        self.assertEqual(max_integer(my_list), 670)

    def test_all_negative(self):
        """check for list with all negative numbers"""
        my_list = [-6, -50, -750, -1, -100]
        self.assertEqual(max_integer(my_list), -1)
