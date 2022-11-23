current_player, other_player = input().split(', ')

size = 6
row, col = 0, 0
current_player_location = None, None
other_player_location = None, None
resting_rounds_current_player = 0
resting_rounds_other_player = 0

matrix = [input().split(' ') for x in range(size)]


def player_movement(row, col, matrix):
    current_player_location = matrix[row][col]
    return current_player_location


while True:
    direction_input = input()
    row, col = direction_input[1:-1].split(', ')
    row, col = int(row), int(col)
    if current_player_location == "W" and resting_rounds_current_player == 1:
        current_player_location, other_player_location = other_player_location, current_player_location
        current_player, other_player = other_player, current_player
        resting_rounds_current_player -= 1
        resting_rounds_current_player, resting_rounds_other_player = resting_rounds_other_player, resting_rounds_current_player
        continue
    current_player_location = player_movement(row, col, matrix)
    if current_player_location == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif current_player_location == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break
    elif current_player_location == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        resting_rounds_current_player += 1
    current_player_location, other_player_location = other_player_location, current_player_location
    current_player, other_player = other_player, current_player
    resting_rounds_current_player, resting_rounds_other_player = resting_rounds_other_player, resting_rounds_current_player

'''
Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)



Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)


Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
'''