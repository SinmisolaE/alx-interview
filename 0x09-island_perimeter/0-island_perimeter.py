#!/usr/bin/python3

""" Create a function def island_perimeter(grid)"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid"""
    if not grid:
        return 0
    row = len(grid)
    col = len(grid[0])
    perimeter = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                # check top side
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check bottom
                if i == (row - 1) or grid[i + 1][j] == 0:
                    perimeter += 1
                # check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # check right
                if j == (col - 1) or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
