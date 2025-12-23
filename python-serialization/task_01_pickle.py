#!/usr/bin/env python3
"""
Custom object serialization and deserialization using pickle
"""

import pickle


class CustomObject:
    """CustomObject class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.
        Returns None on failure.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.
        Returns an instance of CustomObject or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None
