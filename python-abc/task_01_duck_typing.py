#!/usr/bin/env python3
"""
Defines Shape abstract class and demonstrates duck typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class Shape"""

    @abstractmethod
    def area(self):
        """Return the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter using duck typing
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
