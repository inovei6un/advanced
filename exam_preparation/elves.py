elves_energy = [int(x) for x in input().split(' ')]
materials = [int(x) for x in input().split(' ')]

total_energy = 0
total_toys = 0
turn_counter = 0

# first elf takes last box !!!

while elves_energy and materials:
    if elves_energy and elves_energy[0] < 5:
        elves_energy.pop(0)
        continue
    if len(elves_energy) == 0 or len(materials) == 0:
        break

    current_elf = elves_energy.pop(0)
    materials_box = materials.pop()
    turn_counter += 1

    toys_to_create = 1
    energy_to_spend = materials_box
    cookies = 1

    if turn_counter % 3 == 0:
        toys_to_create = 2
        energy_to_spend *= 2
    if turn_counter % 5 == 0:
        toys_to_create = 0
        cookies = 0
    if energy_to_spend <= current_elf:
        total_toys += toys_to_create
        total_energy += energy_to_spend
        elves_energy.append(current_elf - energy_to_spend + cookies)
    else:
        materials.append(materials_box)
        elves_energy.append(current_elf * 2)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")
if elves_energy:
    print(f"Elves left: {', '.join(map(str, elves_energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
'''
10 16 13 25
12 11 8

10 14 22 4 5
11 16 17 11 1 8

5 6 7
2 1 5 7 5 3

'''