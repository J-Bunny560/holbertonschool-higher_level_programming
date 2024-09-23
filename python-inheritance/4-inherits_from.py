#!/usr/bin/python3
"""fuction that return True if the objects is an instance of a class that
inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """fuction that return True if the objects is an instance of a class that
    inherited (directly or indirectly) from the specified class"""
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
