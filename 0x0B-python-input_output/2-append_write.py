#!/usr/bin/python3
""" function that appends a string at end """


def append_write(filename="", text=""):
    """ Add at text to the end of the file given """

    with open(filename, 'a', encodinng='utf-8') as f:
        f.append(text, end="")
