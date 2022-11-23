datura_bomb = 0
cherry_bomb = 0
smoke_decoy_bomb = 0

bomb_effects = [int(x) for x in input().split(', ')]
bomb_casings = [int(x) for x in input().split(', ')]


def bomb_made(bomb_effect, bomb_casing):
    if bomb_effect + bomb_casing == 40:
        return f'datura_bomb'
    if bomb_effect + bomb_casing == 60:
        return f'cherry_bomb'
    if bomb_effect + bomb_casing == 120:
        return f'smoke_decoy_bomb'


while True:
    if len(bomb_effects) == 0 or len(bomb_casings) == 0:
        break
    if datura_bomb >= 3 and cherry_bomb >= 3 and smoke_decoy_bomb >= 3:
        break
    current_bomb_effect = bomb_effects.pop(0)
    current_bomb_casing = bomb_casings.pop(-1)
    if bomb_made(current_bomb_effect, current_bomb_casing) == 'datura_bomb':
        datura_bomb += 1
    elif bomb_made(current_bomb_effect, current_bomb_casing) == 'cherry_bomb':
        cherry_bomb += 1
    elif bomb_made(current_bomb_effect, current_bomb_casing) == 'smoke_decoy_bomb':
        smoke_decoy_bomb += 1
    else:
        current_bomb_casing -= 5
        bomb_effects.insert(0, current_bomb_effect)
        bomb_casings.append(current_bomb_casing)

if datura_bomb >= 3 and cherry_bomb >= 3 and smoke_decoy_bomb >= 3:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

bomb_effects_final = [str(x) for x in bomb_effects]
bomb_casings_final = [str(x) for x in bomb_casings]

if bomb_effects:
    print(f'Bomb Effects: {", ".join(bomb_effects_final)}')
else:
    print(f'Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {",".join(bomb_casings_final)}')
else:
    print(f"Bomb Casings: empty")

print(f'Cherry Bombs: {cherry_bomb}')
print(f'Datura Bombs: {datura_bomb}')
print(f'Smoke Decoy Bombs: {smoke_decoy_bomb}')

'''
5, 25, 25, 115
5, 15, 25, 35

30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10


'''