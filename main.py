from stats import get_num_words, symbol_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
book_text = get_book_text("books/frankenstein.txt")        

get_num_words(book_text)

symbol_count(book_text)



