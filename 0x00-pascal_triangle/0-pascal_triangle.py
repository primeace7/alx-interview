#!/usr/bin/env python3
"""
An iterative implementation of Pascal's tringle generator
"""

def pascal_triangle(n):
    """ generate and return a list of lists representing pascal's trinagle
    of size n
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
            
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

        triangle.append(row)

    return triangle
