#!/usr/bin/python3
"""write a function that reads a text file (UTF8)"""


def read_file(filename=""):
    """write a function that reads a text file (UTF8)
        and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
