#!/usr/bin/python3
""" Function that returns True if object is exactly
an instance of the specifies class """


def is_same_class(obj, a_class):
    """ tells the instance of the object
    using conditional statement"""

    if type(obj) is a_class:
        return True
    else:
        return False
