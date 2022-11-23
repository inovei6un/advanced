def calculate_scored_points(matrix, row, col):
    scored_points = 0
    if matrix[row][col].isdigit():
        scored_points = int(matrix[row][col])
    elif matrix[row][col] == 'D':
        scored_points = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 2
    elif matrix[row][col] == 'T':
        scored_points = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 3
    elif matrix[row][col] == 'B':
        return scored_points
    return scored_points


first_player, second_player = input().split(', ')
matrix = [[char for char in input().split()] for row in range(7)]

first_player_score = 501
second_player_score = 501

first_player_turns = 0
second_player_turns = 0

turns = 1

while True:
    coordinates = eval(input())
    row = coordinates[0]
    col = coordinates[1]

    if row in range(len(matrix)) and col in range(len(matrix)):
        if turns % 2 != 0:
            first_player_turns += 1
            result = calculate_scored_points(matrix, row, col)
            if result == 0:
                first_player_score = 0
                break
            else:
                first_player_score -= result
        else:
            second_player_turns += 1
            result = calculate_scored_points(matrix, row, col)
            if result == 0:
                second_player_score = 0
                break
            else:
                second_player_score -= result
    else:  # HERE
        if turns % 2 != 0:
            first_player_turns += 1
        else:
            second_player_turns += 1

    turns += 1

    if first_player_score <= 0 or second_player_score <= 0:
        break

if first_player_score <= 0:
    print(f'{first_player} won the game with {first_player_turns} throws!')
else:
    print(f'{second_player} won the game with {second_player_turns} throws!')

'''
Ivan, Peter
12 21 18 4 20 7 11
9 D D D D D 10
15 D T T T D 3
2 D T B T D 19
17 D T T T D 6
22 D D D D D 14
5 8 23 13 16 1 24
(3, 3)
'''