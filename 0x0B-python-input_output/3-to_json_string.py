#!/usr/bin/python3
import json

""" function that returns the JSON reprentation """


def to_json_string(my_obj):
    jj = json.dumps(my_obj)
    return jj
