#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    i = 0
    while i < strlen:
        char = ord(str[i])
        if char < 97 or char > 122:
            print("{}".format(chr(char)), end="" if i < strlen - 1 else "\n")
        else char >= 97 and char <= 122:
            char = char - 32
            print("{}".format(char), end="" if i < strlen - 1 else "\n")
        i = i + 1
