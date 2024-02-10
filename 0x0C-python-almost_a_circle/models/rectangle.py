#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Set rectangle attributes and id """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ private instance attributes
        call super, Base class and assign it id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ asign value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ asign value to the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ return X """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float) or value < 0):
            raise TypeError("x must be >=0")
        self.__x = value
        
    @property
    def y(self):
        """ return Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ asign the value of y """
        if not isinstance(value, (int, float) or value < 0):
            raise TypeError("y must be >= 0")
        self.__y = value


    def area(self):
        """ calculates the area of the rectangle """
        return (self.width * self.height)


    def display(self):
        """ prints in stdout the Rectangle
        with character #
        """

        for i in range(self.height):
            print('#' * self.width)


    def __str__(self):
        """ override the string method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
