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

def word_count(file_contents):
    # count words from contents
    return len(file_contents.split())