import sys
from stats import get_num_words

def char_count(file_contents):
    character_count = {}
    # make all the text lowercase
    lower_contents = file_contents.lower()
    for char in lower_contents:
        #only alphanumeric
        if char.isalpha():
            # check if key exists, if not create it w/ value of 0, +1 if existing
            character_count[char] = character_count.get(char, 0) + 1
    return character_count

def main(filepath):
    # open and read contents
    with open(filepath) as f:
        file_contents = f.read()

    # get the word count
    words = word_count(file_contents)
    print(f"Word count: {words}\n")

    # get the character count
    characters = char_count(file_contents)
    # convert dictionary to list of tuples, sort descending based on values
    sorted_chars = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    # print each result
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

if __name__ == "__main__":
    #check for arg
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <filepath>")
        sys.exit(1)
    filepath = sys.argv[1]
    main(filepath)
