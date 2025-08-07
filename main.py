from stats import count_words
from stats import count_characters
from sys import *
import os

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def generate_book_report(book, path):
    report = f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {count_words(book)} total words\n--------- Character Count -------"
    characters_in_book = count_characters(book)
    sorted_by_usage = sorted(characters_in_book.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for character in sorted_by_usage:
        report += f"\n{character[0]}: {character[1]}"
    report += "\n============= END ==============="
    return report

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    try:
        file_to_read = argv[1]
        print(file_to_read)
        contents = get_book_text(file_to_read)
        print(generate_book_report(contents, file_to_read))
    except FileNotFoundError:
        print("That file does not exist.")
    except Exception as e:
        print(f"Unknown error: {e}")
main()