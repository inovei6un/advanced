rows = int(input())

even_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    even_matrix.append([x for x in row if x % 2 == 0])
print(even_matrix)


'''

2
1, 2, 3
4, 5, 6

'''