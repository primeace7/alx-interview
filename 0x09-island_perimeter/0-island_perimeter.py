#!/usr/bin/python3
'''
Implement an island perimeter calculator, given a list
of lists representing the island
'''


def check_boundary(grid, row, col):
    '''
    Check how many boundary cells a single cell has
    e.g in the below grid, 1* has 2 boundaries:
    0  0  0  0
    0  1* 1  0
    0  1  0  0
    0  0  0  0
    '''
    count = 0
    if grid[row][col + 1] == 1:
        count += 1
    if grid[row][col - 1] == 1:
        count += 1
    if grid[row + 1][col] == 1:
        count += 1
    if grid[row - 1][col] == 1:
        count += 1

    return count


def island_perimeter(grid):
    '''Calculate and return the perimeter of an island
    represented by a grid of numbers
    '''
    boundaries = 0
    land = 0
    gridsize = len(grid)

    check = [type(row) is list for row in grid]
    if False in check:
        return 0
    elif 1 in grid[0] or 1 in grid[-1]:
        return 0
    elif gridsize > 100:
        return 0
    elif len(grid[0]) > 100 or len(grid[-1]) > 100:
        return 0

    for row in range(1, gridsize - 1):
        if grid[row][0] == 1 or grid[row][-1] == 1:
            return 0

        for col in range(1, len(grid[row]) - 1):
            boundary_count = check_boundary(grid, row, col)
            if grid[row][col] and boundary_count:
                boundaries += boundary_count
                land += 1
            elif grid[row][col]:
                return 0

    if land:
        return (4 * land) - boundaries
    else:
        return 0
