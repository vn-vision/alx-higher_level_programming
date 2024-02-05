#!/usr/bin/python3
""" Function returns true if the object
is an instance of, or if an instance of
a class that inherited from specified class """


def is_kind_of_class(obj, a_class):
    """ Check if the obj - 1, 'two', [1, 2, 3]
    is an instance of the a_class - int, float, list
    or a 'subclass' """

    if isinstance(obj, a_class):
        return True
    return False
