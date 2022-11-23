from collections import deque
market_queue = deque()


while True:
    command = input()
    if command == "End":
        print(f"{len(market_queue)} people remaining.")
        break
    elif command == "Paid":
        while market_queue:
            print(market_queue.popleft())
    else:
        market_queue.append(command)
