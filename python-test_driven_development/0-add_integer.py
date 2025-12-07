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
        TypeError: if a or b are not integers/floats
    """

    # Validate a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Validate b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN (NaN != NaN is always True)
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    # Reject infinity manually (no imports allowed)
    if isinstance(a, float) and (a == float('inf') or a == -float('inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b == float('inf') or b == -float('inf')):
        raise OverflowError("cannot convert float infinity to integer")

    # Now safe to cast to int
    return int(a) + int(b)
