#!/usr/bin/python3
""" class Square that inherits from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square inherits from rectangle
    square is a rectangle with equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        """ call super class and assign the necessary arguments
        width = height: size
        x, y cordinates and IS
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String format for square define """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the value of the square sides"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns attributes in the args
        args is the list of arguments 
        1st: id
        2nd: size
        3rd: x
        4th: y
        """

        if args:
            attr = ['id', 'size', 'x', 'y']
            for attr, value in zip(attr, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ turns the square attributes to dictionary """
        sdict = {'id':self.id,
                 'x':self.x,
                 'size':self.size,
                 'y':self.y}
        return sdict
