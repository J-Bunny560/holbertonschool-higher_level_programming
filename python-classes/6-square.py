#!/usr/bin/python3
"""Creates a class Square with private instance attributes size and position,
and public instance methods to calculate area and print square."""


class Square:
    """Defines a class with private instance attributes size and position,
and public instance methods to calculate area and print square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates attribute size to 0 and position to (0, 0)"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the private instance attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private instance attribute position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints square of size self.__size using #"""
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()
