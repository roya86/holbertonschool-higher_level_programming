#!/usr/bin/python3
"""
Module for say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a name in the format:
    My name is <first name> <last name>

    Args:
        first_name: string
        last_name: string

    Raises:
        TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
