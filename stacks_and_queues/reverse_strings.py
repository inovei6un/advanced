input_string = input()
string_stack = []
reversed_string = ""


for char in input_string:
    string_stack.append(char)

while string_stack:
    reversed_string += string_stack.pop()

print(reversed_string)