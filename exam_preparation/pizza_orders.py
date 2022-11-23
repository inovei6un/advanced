pizza_orders = [int(x) for x in input().split(', ') if 11 > int(x) > 0]
employees = [int(x) for x in input().split(', ')]

total_pizzas = 0
remaining_pizzas = 0
order_is_completed = True

total_pizzas_to_be_made = sum(pizza_orders)

while True:
    if len(pizza_orders) == 0 or len(employees) == 0:
        if len(pizza_orders) > 0:
            order_is_completed = False
        break
    current_employee = employees.pop(-1)
    current_pizza_order = pizza_orders.pop(0)
    if current_pizza_order > current_employee:
        remaining_pizzas = current_pizza_order - current_employee
        total_pizzas += current_employee
        pizza_orders.insert(0, remaining_pizzas)

pizza_orders = [str(x) for x in pizza_orders]
employees = [str(x) for x in employees]

if order_is_completed:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas_to_be_made}')
    print(f'Employees: {", ".join(employees)}')
elif not order_is_completed:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(pizza_orders)}')


'''

11, 6, 8, 1 
3, 1, 9, 10, 5, 9, 1

10, 9, 8, 7, 5
5, 10, 9, 8, 7

12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1

'''