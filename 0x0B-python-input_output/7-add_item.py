#!/usr/bin/python3
import sys

""" add all arguments to python list """


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if len(sys.argv) > 1:
    save(sys.argv[1:], "add_item.json")
print(load("add_item.json"))
