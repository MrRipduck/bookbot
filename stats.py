def get_num_words(text):
    word_count = 0

    words = text.split()
    for count in words:
        word_count += 1
    print(f"{word_count} words found in the document")

def symbol_count(text):
    lower_case_book = str.lower(text)
    symbols = {}
    for letter in lower_case_book:
        if letter in symbols:
            symbols[letter] += 1
        else:
            symbols[letter] = 1
    print(symbols)

def sorting_letters(dict):
    
    
