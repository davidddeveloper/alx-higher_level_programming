#!/usr/bin/python3
"""2-matrix_divided.py

    __test__ = {"external" = tests/2-matrix_divided.txt}

    This module contains function related to dividing matrix

"""


def matrix_divided(matrix, div):
    """Divides matrix and return the result in a new matrix

    Args:
        - matrix: list of list
        - div: int/float representing the divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size

    """

    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    size = len(matrix[0])  # size of the first row
    new_matrix = []
    for row in matrix:
        new_matrix_row = []
        for number in row:
            if type(number) != int and type(number) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            if len(row) != size:
                raise TypeError(
                        "Each row of the matrix must have the same size"
                        )

            quotient = number / div
            quotient = round(quotient, 2)

            new_matrix_row.append(quotient)

        new_matrix.append(new_matrix_row)

    return new_matrix
