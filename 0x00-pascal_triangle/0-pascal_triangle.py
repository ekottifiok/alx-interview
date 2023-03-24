#!/usr/bin/python3
"""Pascal triangle implementation"""

def pascal_triangle(n: int) -> list[list]:
    """
    Pascal triangle
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(triangle[-1])-1):
            temp.insert(-1, triangle[-1][j] + triangle[-1][j+1])
        triangle.append(temp)

    return triangle
