#!/usr/bin/python3
"""defines function to see if object is an instance of a class
or a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """returns True if object is an instance of the class
    or class that inherited from"""
    return (isinstance(obj, a_class))
