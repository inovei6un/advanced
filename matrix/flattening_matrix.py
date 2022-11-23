n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

flattened_matrix = [num for sublist in matrix for num in sublist]
print(flattened_matrix)
