punctuation_list = ["-", ",", ".", "!", "?"]

with open('./text.txt', 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            exchange = ' '.join(line.strip().split()[::-1])
            for symbol in punctuation_list:
                exchange = exchange.replace(symbol, '@')
            print(exchange)
