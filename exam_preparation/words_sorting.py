def words_sorting(*args):
    def ord_of_word(word):
        return sum((ord(x) for x in word))

    word_dict = {word: ord_of_word(word) for word in args}
    total_values = sum(word_dict.values())
    if total_values % 2 == 0:
        result = sorted(word_dict.items())
    else:
        result = sorted(word_dict.items(), key=lambda p: p[1], reverse=True)

    return '\n'.join(f'{word} - {count}' for (word, count) in result)


print(words_sorting('accolade', 'cacophony'))
