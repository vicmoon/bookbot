def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    characters_list = list(text.lower())
    char_dict = {}
    for char in characters_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        
    return char_dict


def sort_characters(dictionary):
    return dictionary[1]






