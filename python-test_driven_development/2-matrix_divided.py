#!/usr/bin/python3
"""Divide the digits in a matrix."""


def matrix_divided(matrix, div):
    """Devides matrix by a digit.

    Args:
        matrix (list): Lists of digits.
        div (int/float): Denominator.
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
        "of integers/floats")
    if type(div) is not float and type(div) is not int \
    or div != div :
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
            "of integers/floats")
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for digit in row:
            if type(digit) is not float and type(digit) is not int:
                raise TypeError("matrix must be a matrix (list of lists) "
                "of integers/floats")
    return [[round(digit / div, 2) for digit in row] for row in matrix]
