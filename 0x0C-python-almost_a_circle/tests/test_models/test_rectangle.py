#!/usr/bin/python3
""" tests for rectangle module """
from unittest import TestCase
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout

class TestRectangle(TestCase):
    """ class TestRectangle  """
    def test_id_set(self):
        """ id is set """
        r =  Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width(self):
        """ testing for width """
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.id, 12)

    def test_height(self):
        """ testing for height """
        r =  Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.id, 12)

    def test_x(self):
        """ testing for x """
        r = Rectangle(5, 8, 4, 9)
        self.assertEqual(r.x, 4)

    def text_y(self):
        """ testing for y"""
        r = Rectangle(3, 7, 8, 9)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.id, 3)

    def test_no_args(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg(self):
        """Test that height is a mandatory arg"""
        with self.assertRaises(TypeError):
            r = Rectangle(7)

    def test_type_error_width(self):
        """Test type != int for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("world", 5)

    def test_type_error_height(self):
        """Test type != int for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(5, "6")

    def test_type_error_x(self):
        """Test type != int for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 7, "babe")

    def test_type_error_y(self):
        """Test type != int for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(5, 6, 8, "7")

    def test_ValueError_width(self):
        """Test value <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-6, 6)

    def test_ValueError_height(self):
        """Test value <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -9)

    def test_ValueError_x(self):
        """Test value < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(8, 7, -7)

    def test_ValueError_y(self):
        """Test value <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(2, 4, 6, -8)

    def test_area(self):
        """ Test for area of a rectangle"""
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)

    def test_area_one_args(self):
        """ Test for area of a rectangle with one argument"""
        with self.assertRaises(TypeError):
            r = Rectangle(2)

    def test_display_no_xy(self):
        """Test display without x and y"""
        r = Rectangle(2, 2, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 2)


    def test_display_one_args(self):
        """Test display one  args"""
        with self.assertRaises(TypeError):
            r = Rectangle(4)
            r.display()

    def test_str(self):
        """Test the __str__ method with positive value id"""
        r = Rectangle(10, 10, 0, 0, -2)
        self.assertEqual(str(r), "[Rectangle] (-2) 0/0 - 10/10")

    def test_str_complete(self):
        """ Test the __str__ method with all arguments """
        r = Rectangle(10, 10, 5, 4, 8)
        self.assertEqual(str(r), "[Rectangle] (8) 5/4 - 10/10")

    def test_display_x(self):
        """Testing the display method with x"""
        with io.StringIO() as buf, redirect_stdout(buf):
            r = Rectangle(2, 3, 4)
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 2 + "\n") * 3)

    def test_display_xy(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r = Rectangle(5, 6, 7, 8, 9)
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)
