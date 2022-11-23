firework_effects = [int(x) for x in input().split(', ') if int(x) > 0]
explosive_power = [int(x) for x in input().split(', ') if int(x) > 0]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:
    if not firework_effects and explosive_power:
        break
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        break
    current_firework_effect = firework_effects.pop(0)
    current_explosive_power = explosive_power.pop(-1)
    firework_sum = current_firework_effect + current_explosive_power
    if firework_sum % 15 == 0:
        crossette_firework += 1
    elif firework_sum % 5 == 0:
        willow_firework += 1
    elif firework_sum % 3 == 0:
        palm_firework += 1
    else:
        if current_firework_effect - 1 >= 1:
            current_firework_effect -= 1
            firework_effects.append(current_firework_effect)
        explosive_power.append(current_explosive_power)

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    firework_effects_strings = [str(x) for x in firework_effects]
    print(f"Firework Effects left: {', '.join(firework_effects_strings)}")
if explosive_power:
    explosive_power_strings = [str(x) for x in explosive_power]
    print(f"Explosive Power left: {', '.join(explosive_power_strings)}")

print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossette_firework}')


'''
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22


-15, -8, 0, -16, 0, -22
10, 5
'''