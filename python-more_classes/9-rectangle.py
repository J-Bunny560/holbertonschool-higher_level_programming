#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """ a class that defines the a rectangle
        properties: getter and setter methods for width and height
        methods: __init__ method -for creating a class
                area method - for calculating the area of the rectangle
                perimeter method -for calculating the perimeter of rectangle
                __str__ methods - that returns the string representation of
                Rectangle instance(s)
                _repr__ method - returns the formal strig representation of
                an object that can be evaluated
                _del_ method - performs clean up operation before an object
                is deleted
    """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += str(self.print_symbol) * self.width + "\n"
        return result.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        result = (self.width * 2) + (self.height * 2)
        return result

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 > area2:
            return area1
        else:
            return area2

    @classmethod
    def square(cls, size=0):
        new_object = cls(size, size)
        return new_object
