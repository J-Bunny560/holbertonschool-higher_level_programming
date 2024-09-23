#!/usr/bin/python3
"""fuction that return True if the objects is an instance of a class that
inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """fuction that return True if the objects is an instance of a class that
    inherited (directly or indirectly) from the specified class"""
    return isinstance(obj, a_class) and type(obj) != a_class
