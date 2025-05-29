def word_count(book):
    return(len(book.split()))
    
def char_count(book):
    characters = {}
    for char in book:
        if char.lower() in characters:
            characters[char.lower()] = characters[char.lower()] + 1
        else:
            characters[char.lower()] = 1
    return characters

def sort_chars(characters):
    character_counts = []

    for char in characters:
        char_dict = {"char": char, "num": int(characters[char])}
        character_counts.append(char_dict)

    character_counts.sort(reverse=True, key=sort_on)
    return character_counts

def sort_on(d):
    return d["num"]

 