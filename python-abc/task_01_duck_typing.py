#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    An abstract base class representing a geometric shape.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod    
    def perimeter(self):
        pass

class Circle(Shape):
    """
    A class representing a circle, inheriting from the Shape abstract base class.
    """
    def __init__(self, radius):
        """
        Initializes a new instance of Circle.

        Args:
            radius (float): The radius of the circle.
        """

        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * abs(self.radius)
    
class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from the Shape abstract base class.
    """ 
    def __init__(self, width, height):
        """
        Initializes a new instance of Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.height * self.width
    
    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.height + self.width)
    
def shape_info(Shape):
    """
    Prints the area and perimeter of a given shape.

    This function uses duck typing: it expects the `Shape` object to have `area` and `perimeter` methods, but it doesn't care what type of object `Shape` is.

    Args:
        Shape (object): The shape object. Must have `area` and `perimeter` methods.
    """
    area = Shape.area()
    perimeter = Shape.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
