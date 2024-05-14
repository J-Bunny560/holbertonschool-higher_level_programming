#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by orderes keys."""
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
