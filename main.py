import sys
from stats import word_count, char_count

def main(filepath):
    # open and read contents
    with open(filepath) as f:
        file_contents = f.read()

    # get the word count
    words = word_count(file_contents)
    print(f"{words} words found in the document")

    # get the character count
    characters = char_count(file_contents)
    # convert dictionary to list of tuples, sort descending based on values
    sorted_chars = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    # print each result
    for char, count in sorted_chars:
        print(f"{char}: {count}")

if __name__ == "__main__":
    #check for arg
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    main(filepath)