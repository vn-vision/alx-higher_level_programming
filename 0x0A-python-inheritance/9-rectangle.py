#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry():
    """ public instance method that raises
    an exception """

    def area(self):
        """ raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function to validate +ve int """
        self.name = name

        if not isinstance(value, int):
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
        bc.integer_validator("height", height)

        self.width = width
        self.height = height

    def area(self):
        """ RETURN AREA"""
        return (self.width * self.height)

    def __str__(self):
        """ return the print and string representations """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.width) + "/" + str(self.height)
        return string
