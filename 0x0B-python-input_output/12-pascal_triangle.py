#!/usr/bin/python3
""" A Module that defines Pascal's Triangle """


def pascal_triangle(n):
    """ A function that defines Pascal's Triangle """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            if i > 0:
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
