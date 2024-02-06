#!/usr/bin/python3
""" Add attribute to object """


def add_attribute(obj, name, value):
    """ the function adds the name(value)
    in to the object obj if it is possible
    use the hasattr() to check for the target attribute
    use setattr() to set the attribute: name -> value
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
        return obj
    else:
        raise TypeError("can't add new attribute")
