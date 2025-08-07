from stats import count_words
from stats import count_characters

FILE_TO_READ = "books/frankenstein.txt"

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text(FILE_TO_READ)
    print("============ BOOKBOT ============")

main()