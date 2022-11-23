from math import floor

size = int(input())

gathered_coins = 0
player_row, player_col = 0, 0
positions_list = []
game_lost = False

matrix = [input().split(' ') for _ in range(size)]


def move_player(directions, row, col):
    if directions == "left":
        return row, col - 1
    if directions == "right":
        return row, col + 1
    if directions == "down":
        return row + 1, col
    if directions == "up":
        return row - 1, col


def outside_field(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def reposition_to_other_side(row, col, size):
    if row < 0:
        row = size - 1
        return row, col
    if col < 0:
        col = size - 1
        return row, col
    if row >= size:
        return 0, col
    if col >= size:
        return row, 0


for row in matrix:
    if 'P' in row:
        player_row = matrix.index(row)
        player_col = row.index('P')
        player_position = player_row, player_col
        positions_list.append(list(player_position))

while gathered_coins < 100:
    directions = input()

    player_row, player_col = move_player(directions, player_row, player_col)

    if outside_field(player_row, player_col, size):
        player_row, player_col = reposition_to_other_side(player_row, player_col, size)

    positions_list.append([player_row, player_col])

    current_position = matrix[player_row][player_col]
    if current_position == "X":
        game_lost = True
        break  #player loses game coins reduced to 50% and rounded down to the next lowest integer
    elif current_position == "P":
        continue
    else:
        gathered_coins += int(current_position)
        matrix[player_row][player_col] = 0

if game_lost:
    gathered_coins = floor(50/100 * gathered_coins)
    print(f"Game over! You've collected {gathered_coins} coins.")
    print(f'Your path:')
    for path in positions_list:
        print(path)
else:
    print(f"You won! You've collected {gathered_coins} coins.")
    print(f'Your path:')
    for path in positions_list:
        print(path)


'''
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right

8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left
'''