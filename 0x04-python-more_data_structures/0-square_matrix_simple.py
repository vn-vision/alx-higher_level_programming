#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nw_matrix = matrix.copy()
    ana_list = []

    for x in nw_matrix:
       ana_list.append(list( map(lambda i: i**2, x)))

    return ana_list
