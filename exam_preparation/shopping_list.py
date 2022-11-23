def shopping_list(budget, **kwargs):
    result = ''
    types_of_product = 0
    if budget < 100:
        return f"You do not have enough budget."
    for key, value in kwargs.items():
        product = key
        price = float(value[0])
        amount = float(value[1])
        if price * amount <= budget:
            budget -= price*amount
            types_of_product += 1
            result += f"You bought {product} for {price*amount:.2f} leva.\n"
            if types_of_product == 5:
                break
    return result.strip()

'''
print(shopping_list(20, jeans=(19.99, 1),))

print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))


print(shopping_list(104,
cola=(1.20, 2),
candies=(0.25, 15),
bread=(1.80, 1),
pie=(10.50, 5),
tomatoes=(4.20, 1),
milk=(2.50, 2),
juice=(2, 3),
eggs=(3, 1),
))
'''
