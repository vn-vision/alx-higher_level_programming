#!/usr/bin/python3
""" function that saves object to file """
import json


def save_to_json_file(my_obj, filename):
    """ convert obj to json and store in file """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
