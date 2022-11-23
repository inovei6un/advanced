n = int(input())

matrix = []
diagonal_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)

'''

3
11 2 4
4 5 6
10 8 -12

3 
1 2 3
4 5 6
7 8 9




'''