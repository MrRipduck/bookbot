from stats import get_num_words, symbol_count, create_char_count_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
book_text = get_book_text("books/frankenstein.txt")

word_count = get_num_words(book_text)
symbols = symbol_count(book_text)
char_count_list = create_char_count_list(symbols)

char_count_list.sort(key=lambda x: x["count"], reverse=True)

print("----------- Word Count -----------")
print(f"Found {word_count} total words")
print("===================================")
print("--------- Character Count --------")
for char_data in char_count_list:
    print(f"{char_data['char']}: {char_data['count']}")
print("============= END ===============")




