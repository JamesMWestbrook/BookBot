def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)

    word_count = len(file_contents.split())
    print(f"Word count: {word_count}")

    #count_phrase("That", file_contents)

    print(count_characters(file_contents))


def count_phrase(phrase, book):
    lower_phrase = phrase.lower()
    lower_book = book.lower()

    count = lower_book.count(lower_phrase)
    print(f"'{lower_phrase}' was said {count} times")

def count_characters(text):
    characters = {}
    for c in text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters
    

main()