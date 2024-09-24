#!/usr/bin/python3
"""task 01"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """ a class representing a shape"""
    @abstractmethod
    def area(self):
        """ returns area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """ returns perimeter of shape"""
        pass

class Circle(Shape):
        """ a class representing a circle"""
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            """ returns area of circle"""
            return 3.14 * self.radius * self.radius

        def perimeter(self):
            """ returns perimeter of circle"""
            return 2 * 3.14 * self.radius

class Rectangle(Shape):
        """ a class representing a rectangle"""
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            """ returns area of rectangle"""
            return self.width * self.height

        def perimeter(self):
            """ returns perimeter of rectangle"""
            return 2 * (self.width + self.height)

def shape_info(Shape):
    """prints area and perimeter of shape"""
    area = Shape.area()
    perimeter = Shape.perimeter()
    print("area: {}".format(area))
    print("perimeter: {}".format(perimeter))
