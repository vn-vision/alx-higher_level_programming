#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    matrix_divide divides all elements of a matrix
    Args:
        matrix: the matrix
        div: the number to divide with
    """

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    # find the length of each row
    row_len = len(matrix[0])

    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif row_len == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")

    # get each row of the matrix
    for row in matrix:
        new_row = []

        # get each element in row
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix
