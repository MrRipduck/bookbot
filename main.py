def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
def main():
    word_count = 0
    book_text = get_book_text("books/frankenstein.txt")
    
    words = book_text.split()
    for count in words:
        word_count += 1
    print(f"{word_count} words found in the document")
main()





