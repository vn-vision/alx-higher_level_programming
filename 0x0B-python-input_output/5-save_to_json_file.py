#!/usr/bin/python3
import json

""" function that saves object to file """


def save_to_json_file(my_obj, filename):
    """ convert obj to json and store in file """

    jj = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(jj)
        return len(jj)
