size = 6
rover_row, rover_col = 0, 0

matrix = [input().split(' ') for x in range(size)]

for sublist in matrix:
    if "E" in sublist:
        rover_row = matrix.index(sublist)
        rover_col = sublist.index("E")
        rover_position = rover_row, rover_col
directions = input().split(', ')


def move_rover(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "down":
        return row + 1, col
    if direction == "up":
        return row - 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def reposition_rover(row, col, size):
    if row < 0:
        return size - 1, col
    if row >= size:
        return 0, col
    if col < 0:
        return row, size - 1
    if col >= size:
        return row, 0


water = 0
metal = 0
concrete = 0
rover_got_broken = False

for direction in directions:
    rover_row, rover_col = move_rover(direction, rover_row, rover_col)

    if is_outside(rover_row, rover_col, size):
        rover_row, rover_col = reposition_rover(rover_row, rover_col, size)

    current_position = matrix[rover_row][rover_col]

    if current_position == 'W':
        water += 1
        print(f'Water deposit found at ({rover_row}, {rover_col})')
    elif current_position == 'M':
        metal += 1
        print(f'Metal deposit found at ({rover_row}, {rover_col})')
    elif current_position == 'C':
        concrete += 1
        print(f'Concrete deposit found at ({rover_row}, {rover_col})')
    elif current_position == 'R':
        rover_got_broken = True
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water >= 1 and metal >= 1 and concrete >= 1:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')


'''
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left


R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right


R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left

'''
