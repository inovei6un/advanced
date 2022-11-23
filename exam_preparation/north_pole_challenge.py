n, m = input().split(', ')
rows = int(n)
cols = int(m)

current_row = 0
current_col = 0


matrix = [input().split(' ') for _ in range(rows)]

for row in matrix:
    if 'Y' in row:
        current_row = int(matrix.index(row))
        current_col = int(row.index('Y'))

matrix[current_row][current_col] = 'x'


def move_player(direction, steps, matrix, decorations_counter, gifts_counter, cookies_counter, current_row, current_col):
    for step in range(steps):
        if all_items_collected(matrix):
            break
        if direction == "left":
            current_row, current_col = current_row, current_col - 1
        elif direction == "right":
            current_row, current_col = current_row, current_col + 1
        elif direction == "down":
            current_row, current_col = current_row + 1, current_col
        elif direction == "up":
            current_row, current_col = current_row - 1, current_col
        if outside_the_field(current_row, current_col, rows, cols):
            current_row, current_col = reposition_player(current_row, current_col, steps, rows, cols)
        if matrix[current_row][current_col] == "D":
            decorations_counter += 1
        elif matrix[current_row][current_col] == "G":
            gifts_counter += 1
        elif matrix[current_row][current_col] == "C":
            cookies_counter += 1
        elif matrix[current_row][current_col] == '.':
            pass
        matrix[current_row][current_col] = 'x'
    return current_row, current_col, decorations_counter, cookies_counter, gifts_counter

decorations_counter = 0
cookies_counter = 0
gifts_counter = 0


def outside_the_field(current_row, current_col, rows, cols):
    return current_row < 0 or current_col < 0 or current_row >= int(rows) or current_col >= int(cols)


def reposition_player(current_row, current_col, steps, rows, cols):
    if current_row < 0:
        current_row = int(rows) - 1
        return current_row, current_col
    if current_col < 0:
        current_col = int(cols) - 1
        return current_row, current_col
    if current_row >= int(rows):
        return 0, current_col
    if current_col >= int(cols):
        return current_row, 0


def all_items_collected(matrix):
    matrix_string = ''
    for sublist in matrix:
        matrix_string += ', '.join(sublist)
    if "D" not in matrix_string and "G" not in matrix_string and "C" not in matrix_string:
        return True
    else:
        return False


while True:
    command = input().split('-')
    direction = command[0]
    if direction == "End":
        break
    steps = int(command[1])
    current_row, current_col, decorations_counter, cookies_counter, gifts_counter = move_player(direction, steps, matrix, decorations_counter, gifts_counter, cookies_counter, current_row, current_col)

    if all_items_collected(matrix):
        break


matrix[current_row][current_col] = 'Y'

if all_items_collected(matrix):
    print(f"Merry Christmas!")
print(f"You've collected:")
print(f" - {decorations_counter} Christmas decorations")
print(f" - {gifts_counter} Gifts")
print(f" - {cookies_counter} Cookies")

for row in matrix:
    print(' '.join(row))

'''
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End



5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3


5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End

'''