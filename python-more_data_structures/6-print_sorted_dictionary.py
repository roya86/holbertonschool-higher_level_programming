#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print dictionary ordered by keys (alphabetically)."""
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
