#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This module adds two integers.
    It takes two arguments, a and b, and returns their sum.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
