egg = [int(x) for x in input().split(', ') if int(x) >= 0]
piece_of_paper = [int(x) for x in input().split(', ')]

egg_in_a_box = 0

while egg and piece_of_paper:
    current_egg = egg.pop(0)
    if current_egg == 13:
        first_piece = piece_of_paper.pop(0)
        last_piece = piece_of_paper.pop(-1)
        piece_of_paper.append(first_piece)
        piece_of_paper.insert(0, last_piece)
        continue
    if current_egg == 0:
        continue
    current_paper = piece_of_paper.pop(-1)
    sum_of_egg_and_paper = current_egg + current_paper
    if sum_of_egg_and_paper <= 50:
        egg_in_a_box += 1

egg_list = [str(x) for x in egg]
piece_of_paper_list = [str(x) for x in piece_of_paper]

if egg_in_a_box > 0:
    print(f"Great! You filled {egg_in_a_box} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if egg:
    print(f"Eggs left: {', '.join(egg_list)}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join(piece_of_paper_list)}")


'''
20, 13, -7, 7
10, 5, 20, 15, 7, 9


'''