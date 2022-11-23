row_count, col_count = [int(x) for x in input().split(', ')]

column_sum = [0] * col_count
matrix = []

for _ in range(row_count):
    matrix.append([int(x) for x in input().split(' ')])

for row_index in range(row_count):
    for column_index in range(col_count):
        column_sum[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sum]

'''

3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0

[1, 2, 3]
[1, 2, 3] 

'''