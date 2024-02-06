#!/usr/bin/python3
import json

""" create obj from json file """


def load_from_json_file(filename):
    """ read from file and convert to obj"""

    with open(filename, 'r', encoding='utf-8') as f:
        jj = f.read()

        nj = json.loads(jj)
        return nj
