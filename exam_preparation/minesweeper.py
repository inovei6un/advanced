import re

size = int(input())

matrix = []

for _ in range(size):
    rows = [None for x in range(size)]
    matrix.append(rows)

mines = int(input())


def is_inside(size, row, col):
    return 0 <= row < size and 0 <= col < size


def count_neighbor_bombs(matrix, row, col):
    count = 0
    if is_inside(len(matrix), row - 1, col) and matrix[row - 1][col] == "*":
        count += 1
    if is_inside(len(matrix), row + 1, col) and matrix[row + 1][col] == "*":
        count += 1
    if is_inside(len(matrix), row, col - 1) and matrix[row][col - 1] == "*":
        count += 1
    if is_inside(len(matrix), row, col + 1) and matrix[row][col + 1] == "*":
        count += 1
    if is_inside(len(matrix), row - 1, col - 1) and matrix[row - 1][col - 1] == "*":
        count += 1
    if is_inside(len(matrix), row + 1, col - 1) and matrix[row + 1][col - 1] == "*":
        count += 1
    if is_inside(len(matrix), row - 1, col + 1) and matrix[row - 1][col + 1] == "*":
        count += 1
    if is_inside(len(matrix), row + 1, col + 1) and matrix[row + 1][col + 1] == "*":
        count += 1
    return count


for _ in range(mines):
    mine_row, mine_col = [int(x) for x in re.findall('\\d+', input())]
    matrix[mine_row][mine_col] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "*":
            continue
        cell_value = count_neighbor_bombs(matrix, row, col)
        matrix[row][col] = cell_value

for row in matrix:
    print(*row, sep=' ')

'''
4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)

5
3
(1, 1)
(2, 4)
(4, 1)

'''