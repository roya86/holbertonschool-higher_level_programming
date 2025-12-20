#!/usr/bin/env python3
"""
Defines a CountedIterator that counts iterated items
"""


class CountedIterator:
    """Iterator that counts how many items were iterated"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)   # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        return self.count
