#!/usr/bin/python3
"""
Test for Base Class
"""


import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models import rectangle
import inspect
import pep8


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        """Test that models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """
        Set up the test for rectangles
        """
        self.inst = Rectangle(1, 2, 3, 4, 5)

    def test_width(self):
        """
        test rectangle height
        """
        self.assertEqual(self.inst.width, 1)

    def test_width(self):
        """
        test rectangle width
        """
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """
        text x
        """
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.inst.y, 4)

    def test_no_args(self):
        """
        test no args to init
        """
        with self.assertRaises(TypeError):
            noargs = Rectangle()

    def test_too_many_args(self):
        """
        test too many args to init
        """
        with self.assertRaises(TypeError):
            b = Rectangle(1, 1, 2, 3, 4, 5, 6, 7, 8)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_width_typeerror(self):
        """Test string for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("width", 1)

    def test_height_typeerror(self):
        """Test string for height"""
        with self.assertRaisesRegex(
                TypeError, "height must be an integer"):
            r = Rectangle(1, "height")

    def test_x_typerror(self):
        """Test string for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "x")

    def test_y_typeerror(self):
        """Test string for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "y")

    def test_display_empty(self):
        """Test display with no arguments"""

        with self.assertRaises(TypeError):
            Rectangle.display()

    def test_display_two_by_two(self):
        """Test display of rectangle with 2 width and 2 height"""

        r = Rectangle(2, 2)
        expected_square = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle.display(r)
            self.assertEqual(fake_out.getvalue(), expected_square)

    def test_display_two_by_three(self):
        """Test display of rectangle with 2 width and 3 height"""

        r = Rectangle(2, 3)
        expected_square = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle.display(r)
            self.assertEqual(fake_out.getvalue(), expected_square)

    def test_display_two_by_three_1x_2y(self):
        """Test display of rectangle with 2 width and 3 height"""

        r = Rectangle(2, 3, 1, 2)
        expected_square = "\n\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle.display(r)
            self.assertEqual(fake_out.getvalue(), expected_square)

    def test_display_two_by_three_1x_0y(self):
        """Test display of rectangle with 2 width and 3 height"""

        r = Rectangle(2, 3, 1)
        expected_square = " ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle.display(r)
            self.assertEqual(fake_out.getvalue(), expected_square)

    def test_display_two_by_three_0x_2y(self):
        """Test display of rectangle with 2 width and 3 height"""

        r = Rectangle(2, 3, 0, 2)
        expected_square = "\n\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle.display(r)
            self.assertEqual(fake_out.getvalue(), expected_square)

    def test_rectangle_str(self):
        """Test rectangle produces the correct __str__"""
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_update_no_args(self):
        """Test updating a rectangle with no arguments"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_update_id(self):
        """Test updating a rectangle with new id"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(8)
        self.assertEqual(str(r), "[Rectangle] (8) 4/5 - 2/3")

    def test_update_width(self):
        """Test updating a rectangle with new width"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(r.id, 1)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 1/3")

    def test_update_height(self):
        """Test updating a rectangle with new height"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(r.id, r.width, 8)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/8")

    def test_update_x(self):
        """Test updating a rectangle with new x"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(r.id, r.width, r.height, 8)
        self.assertEqual(str(r), "[Rectangle] (6) 8/5 - 2/3")

    def test_update_y(self):
        """Test updating a rectangle with new y"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(r.id, r.width, r.height, r.x, 8)
        self.assertEqual(str(r), "[Rectangle] (6) 4/8 - 2/3")

    # kwargs
    def test_update_kwargs_id(self):
        """Test updating a rectangle with new id"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs_width(self):
        """Test updating a rectangle with new width"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 1/3")

    def test_update_kwargs_height(self):
        """Test updating a rectangle with new height"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 1/2")

    def test_update_kwargs_x(self):
        """Test updating a rectangle with new x"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/5 - 1/2")

    def test_update_kwargs_y(self):
        """Test updating a rectangle with new y"""

        r = Rectangle(2, 3, 4, 5, 6)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        """Test create method"""

        r = Rectangle(5, 6, 7, 8, 9)
        r_dict = r.to_dictionary()
        cr = Rectangle.create(**r_dict)
        self.assertEqual(str(cr), "[Rectangle] (9) 7/8 - 5/6")

    def test_load_from_file(self):
        """Test load from file"""
        r1 = Rectangle(9, 8, 7, 6, 5)
        r2 = Rectangle(30, 40, 50, 60, 7)
        test_input = [r1, r2]
        Rectangle.save_to_file(test_input)
        test_output = Rectangle.load_from_file()
        self.assertEqual(str(test_output[0]), '[Rectangle] (5) 7/6 - 9/8')
        self.assertEqual(str(test_output[1]), '[Rectangle] (7) 50/60 - 30/40')


if __name__ == "__main__":
    unittest.main()
