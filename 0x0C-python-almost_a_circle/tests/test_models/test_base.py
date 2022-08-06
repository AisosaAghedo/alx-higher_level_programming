#!/usr/bin/python3
""" Tests for base module """
from unittest import TestCase
from models.base import Base


class TestBase(TestCase):
    """Tests for  Base class"""
    def test_None(self):
        """Tests id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_set(self):
        """Tests id as not None"""
        b2 = Base(78)
        self.assertEqual(b2.id, 78)

    def test_None_after_set(self):
        """Tests id as None after not None"""
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_too_many_args(self):
        """test more than one args"""
        with self.assertRaises(TypeError):
            b4 = Base(1, 1)

