#!/usr/bin/python3
""" create obj from json file """
import json


def load_from_json_file(filename):
    """ read from file and convert to obj"""

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        return json.loads(data)
