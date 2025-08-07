from stats import count_words
from stats import count_characters
from sys import *
import os

FILE_TO_READ = "books/frankenstein.txt"

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def generate_book_report(book):
    report = f"============ BOOKBOT ============\nAnalyzing book found at {FILE_TO_READ}...\n----------- Word Count ----------\nFound {count_words(book)} total words\n--------- Character Count -------"
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
        FILE_TO_READ = argv[1]
        print(FILE_TO_READ)
        contents = get_book_text(FILE_TO_READ)
        print(generate_book_report(contents))
    except FileNotFoundError:
        print("That file does not exist.")
    except Exception as e:
        print(f"Unknown error: {e}")
main()