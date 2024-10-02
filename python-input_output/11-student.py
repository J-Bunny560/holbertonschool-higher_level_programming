#!/usr/bin/python3
""" a class Student that defines a student """


class Student:
    """ a class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for i in json:
            self.__dict__[i] = json[i]
