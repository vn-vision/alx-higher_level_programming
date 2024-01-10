#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(i for i in my_list)
    result = 0

    for x in new_set:
        result += x

    return result
