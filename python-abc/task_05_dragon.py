#!/usr/bin/python3

class SwimMixin:
    """
    A mixin class that provides a swim method for creatures that can swim.
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    A mixin class that provides a fly method for creatures that can fly.
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon. Dragons can swim, fly, and roar.
    """
    def roar(self):
        print("The dragon roars!")
