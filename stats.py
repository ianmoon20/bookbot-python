def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dict = {}
    for char in text:
        character = char.lower()
        if character in character_dict.keys():
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict