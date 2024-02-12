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

if __name__ == "__main__":
    unittest.main()
