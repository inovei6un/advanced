import re
final_score = 0
size = 6
throws = 3

matrix = [input().split(' ') for x in range(size)]


def is_in_range(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_score(matrix, row, col, size):
    total_score = 0
    if not is_in_range(row, col, size):
        total_score = 0
        return total_score
    if matrix[row][col] == "B":
        matrix[row][col] = 0
        if matrix[0][col] != 'B':
            total_score += int(matrix[0][col])
        if matrix[1][col] != 'B':
            total_score += int(matrix[1][col])
        if matrix[2][col] != 'B':
            total_score += int(matrix[2][col])
        if matrix[3][col] != 'B':
            total_score += int(matrix[3][col])
        if matrix[4][col] != 'B':
            total_score += int(matrix[4][col])
        if matrix[5][col] != 'B':
            total_score += int(matrix[5][col])
    return total_score


for throw in range(throws):
    row, col = [int(x) for x in re.findall('\\d+', input())]
    if not is_in_range(row, col, size):
        continue
    final_score += get_score(matrix, row, col, size)

if final_score < 100:
    print(f"Sorry! You need {100 - final_score} points more to win a prize.")
elif 100 <= final_score <= 199:
    print(f"Good job! You scored {final_score} points, and you've won Football.")
elif 200 <= final_score <= 299:
    print(f"Good job! You scored {final_score} points, and you've won Teddy Bear.")
elif 300 <= final_score:
    print(f"Good job! You scored {final_score} points, and you've won Lego Construction Set.")

'''
10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)


B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)


'''