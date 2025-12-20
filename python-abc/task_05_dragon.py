#!/usr/bin/env python3
"""
Demonstrates mixins with SwimMixin, FlyMixin, and Dragon
"""


class SwimMixin:
    """Mixin that adds swimming ability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class using mixins"""

    def roar(self):
        print("The dragon roars!")
