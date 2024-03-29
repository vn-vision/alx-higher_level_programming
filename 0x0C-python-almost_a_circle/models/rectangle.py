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
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ return Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ asign the value of y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must >= 0")
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle """
        return (self.width * self.height)

    def display(self):
        """ prints in stdout the Rectangle
        with character #
        """
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + '#' * self.width)

    def __str__(self):
        """ override the string method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        1st arg: id
        2nd: width
        3rd: height
        4th: x
        5th: y
        no-keyword argument, order is important
        """
        attr = ['id', 'width', 'height', 'x', 'y']

        for attr in kwargs:
            setattr(self, attr, kwargs[attr])

        for attr, value in zip(attr, args):
            setattr(self, attr, value)

    def to_dictionary(self):
        """ convert rectangle attributes to dictionary """
        rdict = {'x': self.x,
                 'y': self.y,
                 'id': self.id,
                 'height': self.height,
                 'width': self.width}
        return (rdict)
