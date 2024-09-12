#!/usr/bin/python3
"""function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""


def text_indentation(text):
    """args:
        text:(str) the text to be printed
        raise:
            TypeError:text must be a string is raised if the argument 
            passed to the function is not a string
    """
    new_line = (".", "?", ":")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in new_line:
            print(i, end="")
            print()
            print()
        else:
            print(i, end="")
