#!/usr/bin/python3
import abc
from math import pi


#  Circle and Rectangle Classes
class Circle:

    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return pi * (self.radius ** 2)


    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return 2 * (self.width + self.height)


#  shape_info Function
def shape_info(shape):

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
