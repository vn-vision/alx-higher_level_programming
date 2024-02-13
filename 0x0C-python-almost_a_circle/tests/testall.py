#!/usr/bin/python3
""" this is a testcase for the Base, Rectangle and Square"""
import unittest
import os.path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class AirbnbprepTest(unittest.TestCase):
    """ This task was in preparation for the Airbnb
    this is a testcase for the rectangle, base. square class
    """

    # starting base class
    def test_base_auto_id(self):
        """ test the base id """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_base_auto_id_increment(self):
        """ id increment """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_base_custom_id(self):
        """ custom """
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_rectangle_valid_arguments(self):
        """ rectangle valid arguments """
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_negative_width(self):
        """ rectangle with -ve width """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        """ rectangle with -ve height """
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
    def test_rectangle_zero_width(self):
        """ rectangle with 0 width"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_with_position(self):
        """ positional arguments """
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.x, 3)

    def test_toJson(self):
        """ test for serialization """
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id":1}]), '[{"id": 1}]')

    def test_saveFile(self):
        """ checks whether a file is created """
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))
        os.remove("Base.json")

        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_loadFile(self):
        """ this checks whether you can load a file """
        with open("Base.json", "w", encoding='utf-8') as f:
            f.write('[]')
        self.assertEqual(Base.load_from_file(), [])
        os.remove("Base.json")

        with open("Rectangle.json", "w", encoding='utf-8') as f:
            f.write('[{"width":2, "height":3, "x":0, "y":0, "id":1}]')

        rectangle = Rectangle.load_from_file()
        self.assertEqual(len(rectangle), 1)
        self.assertIsInstance(rectangle[0], Rectangle)
        self.assertEqual(rectangle[0].id, 1)
        self.assertEqual(rectangle[0].width, 2)
        self.assertEqual(rectangle[0].height, 3)
        self.assertEqual(rectangle[0].x, 0)
        self.assertEqual(rectangle[0].y, 0)
        os.remove("Rectangle.json")

        with open("Square.json", "w", encoding='utf-8') as f:
            f.write('[{"size":4, "x":0, "y":0, "id":1}]')

        square = Square.load_from_file()
        self.assertEqual(len(square), 1)
        self.assertIsInstance(square[0], Square)
        self.assertEqual(square[0].id, 1)
        self.assertEqual(square[0].x, 0)
        self.assertEqual(square[0].y, 0)
        self.assertEqual(square[0].size, 4)
        os.remove("Square.json")

    def test_square_valid_argument(self):
        """ valid arguments for square """
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_square_with_position(self):
        """ positional argument"""
        square = Square(1, 2)
        self.assertEqual(square.x, 2)

    def test_square_negative_size(self):
        """ -ve values for square """
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_zero_size(self):
        """ when it is zero """
        with self.assertRaises(ValueError):
            Square(0)

if __name__ == "__main__":
    unittest.main()
