def shopping_cart(*args):
    shopping_dict = {'Pizza': set(), 'Dessert': set(), 'Soup': set()}
    try:
        for key, value in args:
            if key in shopping_dict:
                if key == 'Pizza':
                    if len(shopping_dict['Pizza']) == 4:
                        continue
                    elif key == 'Soup':
                        if len(shopping_dict['Soup']) == 3:
                            continue
                    elif key == "Dessert":
                        if len(shopping_dict['Dessert']) == 2:
                            continue
                shopping_dict[key].add(value)
            else:
                shopping_dict[key] = {value, }

    except ValueError:
        if len(shopping_dict['Dessert']) == 0 and len(shopping_dict['Pizza']) == 0 and len(shopping_dict['Soup']) == 0 and not shopping_dict:
            return f'No products in the cart!'
        if shopping_dict:
            result = ''
            sorted_collections_and_objects = sorted(shopping_dict.items(), key=lambda x: (-len(x[1]), x[0]))
            for tuple_ in sorted_collections_and_objects:
                type_object = tuple_[0]
                list_of_objects = tuple_[1]
                sorted_list_of_objects = sorted(list_of_objects)
                result += f"{type_object}:\n"
                for obj in sorted_list_of_objects:
                    result += f" - {obj}\n"
            return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

'''

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
'''