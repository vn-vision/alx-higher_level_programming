#!/usr/bin/python3
""" function that returns dictionary description """


def class_to_json(obj):
    """ convert instance into JSON """

    jj = {}
    attributes = obj.__dict__

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            jj[key] = value

    return jj
