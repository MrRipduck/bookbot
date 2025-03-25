def get_num_words(text):
    word_count = 0

    words = text.split()
    for count in words:
        word_count += 1
    return word_count

def symbol_count(text):
    lower_case_book = str.lower(text)
    symbols = {}
    for letter in lower_case_book:
        if letter in symbols:
            symbols[letter] += 1
        else:
            symbols[letter] = 1
    return symbols

def create_char_count_list(symbols):
    char_count_list = []
    for char, count in symbols.items():
        if char.isalpha():
            char_count_list.append({"char": char, "count": count})
    return char_count_list

def sort_on(char_dict):
    return char_dict["count"]


