#!/usr/bin/python3
import math
from abc import ABC, abstractmethod

# Shape Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Rectangle Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape_info Function
def shape_info(shape):
    print(f"Area: {shape.area():.2f}")  # Formatted output
    print(f"Perimeter: {shape.perimeter():.2f}")

# Testing
try:
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)
    shape_info(circle)
    shape_info(rectangle)
    # This will trigger the ValueError
    circle_negative = Circle(radius=-5)
    shape_info(circle_negative)
except ValueError as e:
    print(e) 
