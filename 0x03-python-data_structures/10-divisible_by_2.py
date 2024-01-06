#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    ln = len(my_list)
    i = 0
    new_list = []

    while i < ln:
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

        i += 1
    return new_list
