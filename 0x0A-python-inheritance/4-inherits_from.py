#!/usr/bin/python3
""" Return True if the object is an instance
of a class that inherited directly or indirectly """


def inherits_from(obj, a_class):
    """ Conditional return depending
    on the obj, a_class output
    True, then return True else False"""

    cur_class = type(obj)

    if issubclass(cur_class, a_class) and cur_class != a_class:
        return True
    return False
