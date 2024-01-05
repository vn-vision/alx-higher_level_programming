#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    ln = len(my_list)
    cp_list = my_list.copy()

    if idx < 0 or idx >= ln:
        return my_list
    else:
        cp_list[idx] = element
        return cp_list
