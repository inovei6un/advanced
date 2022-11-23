input_string = input()
stack_list = []

for index in range(len(input_string)):
    if input_string[index] == "(":
        stack_list.append(index)
    elif input_string[index] == ')':
        start_index = stack_list.pop()
        end_index = index + 1
        print(input_string[start_index:end_index])
