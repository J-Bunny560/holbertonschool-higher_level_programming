#!/usr/bin/python3
"""Module to define a Square class with
size attribute and area calculation.

This module provides a Square class that allows
creating a square with a specific
size and calculating its area. The size attribute
is validated to ensure it is a
non-negative integer.
"""


class Square:
    """Represents a square with a size.

    Attributes:
        __size (int): The size of one side of the square.
    """

    def __init__(self, size=0):
        """Initializes a Square instance with a given size.

        Args:
            size (int): The size of one side of the square,
        must be a non-negative integer.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of one side of the square,
        must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
