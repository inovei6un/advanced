def find_symbol(matrix, symbol):
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == symbol:
                return row_index, col_index


n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)

if result:
    row_index, col_index = result
    print(f"({row_index}, {col_index})")
else:
    print(f"{symbol} does not occur in the matrix")



'''


3
ABC
DEF
X!@
!


4
asdd
xczc
qwee
qefw
4

'''