def start_spring(**kwargs):
    types_list = []
    flowers_list = []
    birds_list = []
    trees_list = []
    insects_list = []
    my_dict = {}

    values = kwargs.items()

    for tpl in values:
        if tpl[1] not in types_list:
            types_list.append(tpl[1])

    for obj, obj_type in values:
        if obj_type == "flower":
            flowers_list.append(obj)
        elif obj_type == "bird":
            birds_list.append(obj)
        elif obj_type == "tree":
            trees_list.append(obj)
        elif obj_type == "insect":
            insects_list.append(obj)

    for el in types_list:
        if el == "flower":
            my_dict['flower'] = flowers_list
        if el == "bird":
            my_dict['bird'] = birds_list
        if el == "tree":
            my_dict['tree'] = trees_list
        if el == "insect":
            my_dict['insect'] = insects_list

    current_key = ''

    for key in my_dict:
        my_dict[key] = (sorted(my_dict[key]))

    for key in my_dict:
        if len(current_key) == len(my_dict[key]) and current_key != key and current_key != '':
            sorted_dict = {k: v for k, v in sorted(my_dict.items(), reverse=True, key=lambda x: x[1])}
            my_dict = sorted_dict
        else:
            current_key = my_dict[key]

    result = ''

    for key in my_dict:
        result += f'\n{key}:\n-'
        value = my_dict[key]
        final_value = '\n-'.join(value)
        result += f'{final_value}'

    return result.strip()




example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))



example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

