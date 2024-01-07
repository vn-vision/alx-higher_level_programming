#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    argA = len(tuple_a)
    argB = len(tuple_b)

    if argA >= 2:
        x_a, x_b = tuple_a[0], tuple_a[1]
    else:
        x_a, x_b = tuple_a[0] if argA >= 1 else 0, 0

    if argB >= 2:
        y_a, y_b = tuple_b[0], tuple_b[1]
    else:
        y_a, y_b = tuple_b[0] if argB >= 1 else 0, 0

    x = x_a + y_a
    y = x_b + y_b

    return (x, y)
