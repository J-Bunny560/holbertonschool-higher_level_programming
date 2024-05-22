#!/usr/bin/python3
"""defines class Mylist"""


class MyList(list):
    """class that inherits from list
    with public instance methos to print sorted list"""

    def print_sorted(self):
        print(sorted(self))
