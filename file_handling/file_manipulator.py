from os.path import exists
from os import remove

while True:
    command = input()
    if command == "End":
        break
    command_params = command.split('-')
    file_name = command_params[1]

    if command_params[0] == "Create":
        with open(f'./{file_name}', 'w') as file:
            pass
    elif command_params[0] == "Add":
        content = command_params[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '\n')
    elif command_params[0] == "Replace":
        if not exists(f'./{file_name}'):
            print("An error occurred")
            continue
        old_string = command_params[2]
        new_string = command_params[3]
        with open(f'./{file_name}', 'r+') as file:
            file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(file_content)
    elif command_params[0] == "Delete":
        if not exists(f'./{file_name}'):
            print("An error occurred")
            continue
        else:
            remove(f"./{file_name}")

