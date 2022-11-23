def naughty_or_nice_list(kid_list, *args, **kwargs):
    nice_kids = []
    naughty_kids = []
    for command in args:
        num, naughty_or_nice = command.split('-')
        num = int(num)
        name = None
        is_unique = False
        for kid_num, kid_name in kid_list:
            if num == kid_num and is_unique:
                is_unique = False
                break
            if num == kid_num:
                name = kid_name
                is_unique = True
        if is_unique:
            kid_list.remove((num, name))
            if naughty_or_nice == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)
    for name, naughty_or_nice in kwargs.items():
        is_unique = False
        num = None
        for kid_number, kid_name in kid_list:
            if name == kid_name and is_unique:
                is_unique = False
                break
            if name == kid_name:
                is_unique = True
                num = kid_number
        if is_unique:
            kid_list.remove((num, name))
            if naughty_or_nice == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)
    not_found = [name for num, name in kid_list]

    result = ''
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    return result.strip()


print(naughty_or_nice_list(
                    [
                        (6, "John"),
                        (4, "Karen"),
                        (2, "Tim"),
                        (1, "Merry"),
                        (6, "Frank"),
                    ],
                    "6-Nice",
                    "5-Naughty",
                    "4-Nice",
                    "3-Naughty",
                    "2-Nice",
                    "1-Naughty",
                    Frank="Nice",
                    Merry="Nice",
                    John="Naughty",
                ))

#print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty", ))

