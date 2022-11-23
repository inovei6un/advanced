from collections import deque
quantity_of_water = int(input())
dispenser_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        dispenser_queue.append(command)

while True:
    command = input().split(' ')
    if command[0] == "End":
        break
    elif command[0] == "refill":
        quantity_of_water += int(command[1])
    else:
        liters_needed = int(command[0])
        if liters_needed <= quantity_of_water:
            quantity_of_water -= liters_needed
            print(f'{dispenser_queue.popleft()} got water')
        else:
            print(f"{dispenser_queue.popleft()} must wait")

print(f"{quantity_of_water} liters left")
