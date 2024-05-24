#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

        if radius < 0:
            raise ValueError("Radius cannot be negative")


    def area(self):
        return 3.14 * self.radius ** 2


    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

    except AttributeError:
        print("The provided object does not have area and perimeter methods.")
