#!/usr/bin/python3
""" function that returns a list of lists of integers"""


def pascal_triangle(n):
    """ returns a list of lists of integers"""
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        while len(triangle) != n:
            tri = triangle[-1]
            temp = [1]
            for i in range(len(tri) - 1):
                temp.append(tri[i] + tri[i + 1])
            temp.append(1)
            triangle.append(temp)
        return triangle
