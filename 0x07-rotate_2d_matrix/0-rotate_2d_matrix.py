#!/usr/bin/python3
'''A 2D matrix 90 degrees clockwise rotator implementation
'''


def getside(matrix, direction, depth):
    '''Fetch a side from a 2D matrix, assuming it is a
    collection of squares
    Example: [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    In the above matrix, 1, 2, 3 is a side, as is 3, 6, 9.
    '''
    size = len(matrix)
    if direction == 0:
        return matrix[depth][depth: size - depth]
    elif direction == 2:
        return matrix[-1 - depth][depth: size - depth]

    result = []

    if direction == 3:
        for i in range(size - depth - 1, depth - 1, -1):
            result.append(matrix[i][depth])
    elif direction == 1:
        for i in range(size - depth - 1, depth - 1, -1):
            result.append(matrix[i][-depth - 1])

    return result


def setside(matrix, side, direction, depth):
    '''Edut a side of a 2D matrix in-place, assuming it is a
    collection of squares
    Example: [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    In the above matrix, 1, 2, 3 is a side, as is 3, 6, 9.
    '''
    size = len(matrix)

    if direction == 0:
        matrix[depth][depth: size - depth] = side
    elif direction == 2:
        matrix[-1 - depth][depth: size - depth] = side
    elif direction == 3:
        for i, j in zip(side, range(depth, size - depth)):
            matrix[j][depth] = i
    elif direction == 1:
        for i, j in zip(side, range(depth, size - depth)):
            matrix[j][-1 - depth] = i


def rotate_2d_matrix(matrix):
    '''Rotate a 2D matrix in place, assuming the input
    matrix will not be empty
    '''
    cycles = len(matrix) // 2
    for i in range(cycles):
        temp = getside(matrix, 0, i)

        for j in range(3):
            from_side = getside(matrix, 3 - j, i)
            if j == 1:
                setside(matrix, from_side, 3, i)
            else:
                setside(matrix, from_side, j, i)

        setside(matrix, temp, 1, i)
