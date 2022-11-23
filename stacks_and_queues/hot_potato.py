from collections import deque
kid_deck = deque(input().split(' '))
toss_count = int(input())
counter = 0

while len(kid_deck) > 1:
    counter += 1
    kid = kid_deck.popleft()

    if counter < toss_count:
        kid_deck.append(kid)
    else:
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {kid_deck[0]}")
