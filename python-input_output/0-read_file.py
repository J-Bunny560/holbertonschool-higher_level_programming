#!/usr/bin/python3
"""defines functions to read a txt file and prints to stdout"""


def read_file(filename=""):
    """reads text file and prints to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
