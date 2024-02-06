#!/usr/bin/python3
"""
Module with a script that adds arguments
to a Python list saved in a file
"""
import sys


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
if len(sys.arg) > 1:
    try:
        items = load(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.arg[1:])
    save(items, filename)
