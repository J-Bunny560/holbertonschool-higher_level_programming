#!/usr/bin/python3
""" defines class CustomObject"""

import pickle


class CustomObject:
    """a custom python class that represents an object with a:
    name, age, and student status."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Prints the name, age, and student status of the object """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student: {self.is_student}")

    def serialize(self, filename):
        """ Serialize data and save it to a file """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """ Load data from a file and deserialize it """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error: {e}")
