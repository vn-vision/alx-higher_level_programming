#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry():
    """ public instance method that raises
    an exception """

    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate if int is positive"""
        self.name = name

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.value = value


""" Class Rectangle thart inherits from baseclass """


class Rectangle(BaseGeometry):
    """ instantiate the width and height
    of a rectangle, must be positive ints
    use integer_validator"""

    def __init__(self, width, height):
        """ initialize the width and height
        after validation"""

        bc = BaseGeometry()

        bc.integer_validator("width", width)
        self.width = width
        bc.integer_validator("height", height)
        self.height = height
