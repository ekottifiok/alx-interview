#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Create a function def island_perimeter(grid):
    that returns the perimeter of the island described in grid:
    """
    per = 0
    connections = 0
    length_row = len(grid)
    length_col = len(grid[0])
    for x in range(0, length_row):
        for y in range(0, length_col):
            if grid[x][y] == 1:
                per += 4
                # checking top
                if x != 0 and grid[x - 1][y] == 1:
                    connections += 1
                # checking left
                if y != 0 and grid[x][y - 1] == 1:
                    connections += 1
    return per - (connections * 2)
