def stock_availability(inventory_list, action, *args):
    if action == "delivery":
        for el in args:
            inventory_list.append(el)
    elif action == "sell":
        if not args:
            inventory_list.pop(0)
        else:
            for el in args:
                if isinstance(el, int):
                    return inventory_list[el:]
                else:
                    sold_items = set(args)
                    return [item for item in inventory_list if item not in sold_items]
    return inventory_list


def stock_availability1(inventory_list, action, *args):
    if action == "delivery":
        return inventory_list + list(args)

    if not args or isinstance(args[0], int):
        count = args[0] if args else 1
        inventory_list = inventory_list[count:]
        return inventory_list

    sold_items = set(args)

    return [item for item in inventory_list if item not in sold_items]


#print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
#print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
#print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
#print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 4)) #problem is not here
print(stock_availability(["chocolate", "chocolate", "banana", 'chocolate', 'chocolate'], "sell", "chocolate"))
#print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))
#print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie", "banana"))



#print(stock_availability1(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
#print(stock_availability1(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
#print(stock_availability1(["chocolate", "vanilla", "banana"], "sell"))
#print(stock_availability1(["chocolate", "vanilla", "banana"], "sell", 2))
#print(stock_availability1(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
#print(stock_availability1(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))
#print(stock_availability1(["chocolate", "vanilla", "banana"], "sell", "cookie", "banana"))