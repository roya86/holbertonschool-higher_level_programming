#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats, casted to integers.

    Args:
        a: first number (int or float)
        b: second number (int or float)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
