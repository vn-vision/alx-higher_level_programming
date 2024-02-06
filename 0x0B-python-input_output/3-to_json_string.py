#!/usr/bin/python3
""" function that returns the JSON reprentation """
import json

def to_json_string(my_obj):
    """ returns the json format """

    jj = json.dumps(my_obj)
    return jj
