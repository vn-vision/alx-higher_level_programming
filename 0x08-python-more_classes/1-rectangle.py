#!/usr/bin/python3
""" Class Rectangle that defines rectangle
based on 0-rectangle.py
"""


class Rectangle:
    """ the Class rectangle takes attributes
    width: the length of "width"
    height: its height
    """

    def __init__(self, width=0, height=0):
        """ Create new rectangle
        width, height
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ return the width """

        return self.__width

    @width.setter
    def width(self, value):
        """ manipulate the width of the rectangle """

        if value < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__width = value

    @property
    def height(self):
        """ return set height """

        return self.__height

    @height.setter
    def height(self, value):
        """ Manipulate height
        change the value
        """

        if value == 0:
            raise ValueError("height must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")

        self.__height = value
