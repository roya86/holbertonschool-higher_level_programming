#!/usr/bin/env python3
"""
Defines an abstract Animal class and its subclasses Dog and Cat
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal"""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal"""
        pass


class Dog(Animal):
    """Dog class inherits from Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inherits from Animal"""

    def sound(self):
        return "Meow"
