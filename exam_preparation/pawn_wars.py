chess_board = []
col, row = 0, 0
col1, row1 = 0, 0

white_wins = False
black_wins = False

for _ in range(8):
    row = [x for x in input().split(' ')]
    chess_board.append(row)

for sublist in chess_board:
    if 'w' in sublist:
        row, col = chess_board.index(sublist), sublist.index('w')
    if 'b' in sublist:
        row1, col1 = chess_board.index(sublist), sublist.index('b')

white = [int(row), int(col)]
black = [int(row1), int(col1)]


turn_counter = 0

while not white_wins and not black_wins:
    turn_counter += 1
    if white[0] == 0:
        white_wins = True
        print('white wins', white)
    elif black[0] == 7:
        black_wins = True
        print('black wins', black)
    if turn_counter % 2 != 0:
        if abs(white[1] - black[1]) == 1 and abs(white[0] - black[0] == 1):
            white[0] -= 1
            white[1] -= 1
            white_wins = True
        else:
            white[0] -= 1
    else:
        if abs(white[1] - black[1]) == 1 and abs(white[0] - black[0] == 1):
            black[0] += 1
            black[1] += 1
            black_wins = True
        else:
            black[0] += 1

if white_wins:
    print('white wins', white)
else:
    print('black wins', black)

'''
- - - - - - b - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - -  
- w - - - - - -  
- - - - - - - - 
- - - - - - - - 


- - - - - - - - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - - 
- - b - - - - -  
- w - - - - - -  
- - - - - - - - 
- - - - - - - - 



- - - - - - - - 
- - b - - - - - 
- - - w - - - - 
- - - - - - - - 
- - - - - - - -  
- - - - - - - -  
- - - - - - - - 
- - - - - - - - 

'''