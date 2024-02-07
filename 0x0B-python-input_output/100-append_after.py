#!/usr/bin/python3
""" a function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ adds after the specified string
    the find() returns the index of the first
    letter of the string it is searching for
    """

    with open(filename, 'r', encoding='utf-8') as f:
        file = f.readlines()

        found = 0
        with open(filename, 'w', encoding='utf-8') as f:
            for line in file:
                f.write(line)
                if search_string in line:
                    f.write(new_string)
                    found = 1
        if not found:
            print("Search string not found")
