#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid

Island perimeter computing module.
"""


def island_perimeter(grid):
    """ Computes the perimeter of an island with no lakes."""
    perimeter = 0
    if type(grid) is not list:
        return 0
    num = len(grid)
    for idx, row in enumerate(grid):
        m = len(row)
        for j, square in enumerate(row):
            if square == 0:
                continue
            edges = (
                idx == 0 or (len(grid[idx - 1]) > j and grid[idx - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                idx == num - 1 or (len(grid[idx + 1]) > j
                                   and grid[idx + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
