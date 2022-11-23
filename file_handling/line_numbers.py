from string import punctuation


def count(line):
    punctuation_symbols_set = set(punctuation)
    letters_count = 0
    symbols_count = 0
    for symbol in line:
        if symbol.isalpha():
            letters_count += 1
        elif symbol in punctuation_symbols_set:
            symbols_count += 1
    return letters_count, symbols_count


with open('./text.txt', 'r') as file, open('./output.txt', 'w') as output:
    for index, line in enumerate(file):
        letters, punctuation_symbols = count(line)
        output.write(f"Line {index + 1}: {line.strip()} ({letters})({punctuation_symbols})\n")
