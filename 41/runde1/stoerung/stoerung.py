quote_path = "stoerung0.txt"

with open('Alice_im_Wunderland.txt', encoding="utf8") as f:
    text = []
    written_text = ""
    for line in f:
        for word in line.split():
            word = word.lower()
            chars = list(word)
            new_chars = []
            for i in chars:
                if (ord(i) > 96 and ord(i) < 123) or i == "ü" or i == "ä" or i == "ö" or i == "ß":
                    new_chars.append(i)
            word = ""
            for i in new_chars:
                word += i
            text.append(word)
    written_text = written_text.lower()

with open(quote_path, encoding="utf8") as f:
    quote = []
    for line in f:
        for word in line.split():
            quote.append(word)


def solveQuote():
    knownWords = getKnownWords()
    possible_quotes = []
    j = 0

    for i in text:
        if i == knownWords[0][0]:
            for k in knownWords[1:]:
                isRight = True
                if (text[j + k[1] - knownWords[0][1]] != k[0]):
                    isRight = False
            if(isRight == True):
                temp_quote = buildQuote(j)
                possible_quotes.append(temp_quote)
            isRight = False
        j += 1
    return possible_quotes


def getKnownWords():
    temp = []
    j = 0
    for i in quote:
        if i != "_":
            temp.append([i, j])
        j += 1
    return temp


def buildQuote(text_idx):
    temp_quote = []
    j = 0
    for i in quote:
        if i != "_":
            break
        j += 1
    start_idx = text_idx - j
    for k in range(len(quote)):
        temp_quote.append(text[start_idx+k])
    return temp_quote


all_quotes = solveQuote()

broke_quote_word = ""
for i in quote:
    broke_quote_word += i
    broke_quote_word += " "
print("Stoerung: ", broke_quote_word)

unique_quotes = []
for sublist in all_quotes:
    if sublist not in unique_quotes:
        unique_quotes.append(sublist)
all_quotes = unique_quotes

for i in all_quotes:
    quote_word = ""
    for j in i:
        quote_word += j
        quote_word += " "
    print("Zitat: ", quote_word)
