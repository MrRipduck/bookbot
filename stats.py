def get_num_words(text):
    word_count = 0

    words = text.split()
    for count in words:
        word_count += 1
    print(f"{word_count} words found in the document")