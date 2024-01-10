#!/usr/bin/python3

def search_replace(my_list, search, replace):
    nw_list = my_list.copy()
    ana_list = []

    for i in nw_list:
        if i == search:
            i = replace
        ana_list.append(i)

    return ana_list
