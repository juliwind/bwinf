quote_path = "stoerung0.txt"

with open('Alice_im_Wunderland.txt') as f:
    text = []
    for line in f:
        for word in line.split():
            text.append(word)

with open(quote_path) as f:
    quote = []
    for line in f:
        for word in line.split():
            quote.append(word)


def solveQuote(start_idx):
    possible_quotes = []
    remaining_quote = quote
    start_word = quote[start_idx]

    first_matches = []
    idx = 0
    for word in text:
        if start_word == word:
            first_matches.append(idx)
            cur_quote = ""
            for j in range(len(quote)):
                cur_quote += text[j + idx - start_idx] + " "
            possible_quotes.append(cur_quote)

        idx += 1

    remaining_quote = remaining_quote[start_idx + 1:len(remaining_quote)]
    idx = 0
    while (("_" in remaining_quote) == True) and (idx < 50):
        idx_2 = 0
        for i in remaining_quote:
            print(i, i != "_")
            if i != "_":
                searched_word = remaining_quote[idx]
                new_possibles = []
                for i in range(len(possible_quotes)):
                    temp_quote = possible_quotes[i]
                    sliced_quote = temp_quote.split()
                    if (sliced_quote[idx] == searched_word):
                        new_possibles.append(sliced_quote)
            idx_2 += 1
        idx += 1
        possible_quotes = new_possibles
    # for x in range(len(possible_quotes)):
        # print(possible_quotes[x])


idx = 0
for i in quote:

    if i != "_":
        solveQuote(idx)
        break
    idx += 1
