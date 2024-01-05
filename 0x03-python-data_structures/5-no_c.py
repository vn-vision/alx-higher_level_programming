#!/usr/bin/python3

def no_c(my_string):

    new_str = ""
    ln = len(my_string)
    i = 0

    while i < ln:
        if my_string[i] != "c" and my_string[i] != "C":
            new_str += my_string[i]
        i += 1
    return new_str
