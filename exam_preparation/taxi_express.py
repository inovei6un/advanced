customer_list = [x for x in input().split(', ')]
taxi_list = [x for x in input().split(', ')]

total_time = 0

while customer_list and taxi_list:
    current_customer = int(customer_list.pop(0))
    current_taxi = int(taxi_list.pop(-1))
    if current_customer > current_taxi:
        customer_list.insert(0, str(current_customer))
    else:
        total_time += current_customer

if not customer_list:
    print(f'All customers were driven to their destinations')
    print(f"Total time: {total_time} minutes")
elif not taxi_list:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(customer_list)}")



'''
4, 6, 8, 5, 1
1, 9, 15, 10, 6

10, 5, 8, 9
2, 4, 5, 8

2, 8, 4, 3, 11, 7
10, 15, 4, 6, 3, 10, 2, 1
'''