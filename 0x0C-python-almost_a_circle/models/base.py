#!/usr/bin/python3
""" class named Base """


class Base():
    """ the base of all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing the id and set it to value """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
