#!/usr/bin/python3
"""
Module for matrix_divided function.
Divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix: list of lists of ints/floats
        div: number (int or float)

    Returns:
        new matrix with elements rounded to 2 decimals

    Raises:
        TypeError: if matrix is invalid or div is not a number
        ZeroDivisionError: if div is zero
    """

    # Validate matrix type
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate matrix elements + uniform row size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix
    return [[round(value / div, 2) for value in row] for row in matrix]
