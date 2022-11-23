size = int(input())
matrix = []

for row in range(size):
    rows = [x for x in input()]
    matrix.append(rows)

snake_row = 0
snake_col = 0
food_count = 0
is_snake_outside = False

for sublist in matrix:
    if "S" in sublist:
        snake_row = matrix.index(sublist)
        snake_col = sublist.index("S")


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def move_snake(direction, row, col):
    if direction == "left":
        if not is_outside(row, col - 1, size):
            return row, col - 1
    if direction == "right":
        if not is_outside(row, col + 1, size):
            return row, col + 1
    if direction == "down":
        if not is_outside(row + 1, col, size):
            return row + 1, col
    if direction == "up":
        if not is_outside(row - 1, col, size):
            return row - 1, col


while food_count < 10:
    directions = input()
    matrix[snake_row][snake_col] = '.'
    try:
        snake_row, snake_col = move_snake(directions, snake_row, snake_col)
    except TypeError:
        is_snake_outside = True
        break
    if matrix[snake_row][snake_col] == 'B':
        matrix[snake_row][snake_col] = '.'
        for sublist in matrix:
            if "B" in sublist:
                snake_row = matrix.index(sublist)
                snake_col = sublist.index("B")
                matrix[snake_row][snake_col] = "S"
                continue
    elif matrix[snake_row][snake_col] == '*':
        food_count += 1
    elif matrix[snake_row][snake_col] == '-':
        pass
    matrix[snake_row][snake_col] = 'S'


if is_snake_outside:
    print(f"Game over!")
elif food_count >= 10:
    print(f"You won! You fed the snake.")
print(f"Food eaten: {food_count}")
for row in matrix:
    print(''.join(row))

'''

6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left

7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down



'''