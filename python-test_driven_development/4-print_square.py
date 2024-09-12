#!/usr/bin/python3
"""function that prints a square with the character #."""


def print_square(size):
    """print_Square: it prints # in form of a square
        argument
            size:(int or float) the length of the square
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for i in range(size):
        print("#" * size)
