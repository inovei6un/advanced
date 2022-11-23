def list_manipulator(num_list, *args):
    num_list = num_list
    list_args = list(args)
    list_args.pop(0)
    list_args.pop(0)
    if args[0] == "add":
        if args[1] == "beginning":
            num_list = list_args + num_list
        elif args[1] == "end":
            num_list = num_list + list_args
    elif args[0] == "remove":
        if args[1] == "beginning":
            if len(list_args) == 1:
                for el in range(int(list_args[0])):
                    num_list.pop(0)
            elif not list_args:
                num_list.pop(0)
        elif args[1] == "end":
            if len(list_args) == 1:
                for el in range(int(list_args[0])):
                    num_list.pop()
            elif not list_args:
                num_list.pop()
    return num_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
