#!/usr/bin/python3
""" function reads a text file in encoding=utf8 """


def read_file(filename=""):
    """ use with to ensure closing is handled """

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
