#!/usr/bin/python3
""" a class Student that defines a student """


class Student:
    """ a class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """ a class Student that defines a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a class Student that defines a student """
        if attrs is None:
            return self.__dict__
