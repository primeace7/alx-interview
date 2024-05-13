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
    if col != len(grid[row]) - 1 and grid[row][col + 1] == 1:
        count += 1
    if col != 0 and grid[row][col - 1] == 1:
        count += 1
    if row != len(grid) - 1 and grid[row + 1][col] == 1:
        count += 1
    if row != 0 and grid[row - 1][col] == 1:
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
    elif gridsize > 100:
        return 0
    elif len(grid[0]) > 100 or len(grid[-1]) > 100:
        return 0

    for row in range(0, gridsize):
        for col in range(0, len(grid[row])):
            boundary_count = check_boundary(grid, row, col)
            if grid[row][col] and boundary_count:
                boundaries += boundary_count
                land += 1
            elif grid[row][col]:
                land += 1

    if land:
        return (4 * land) - boundaries
    else:
        return 0
