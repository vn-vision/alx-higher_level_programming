#!/usr/bin/python3
""" a function that writes a string to file encoding UTF8 """


def write_file(filename="", text=""):
    """ create file if it does not exist """

    f  = with open(filename, 'w', encoding='utf-8')

    f.write(text)
