def get_word_count(book_text):
    words = []
    words = book_text.split()
 #   return len(words)
    return(f"Found {len(words)} total words")

def get_letter_counts(text):
    text = text.lower()
    letter_counts = {}

    for char in text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    return(letter_counts)

def sort_key(dictionary):
    return dictionary["num"]

def organize_letter_counts(dictionary):
    letter_list = []
    
    for key, item in dictionary.items():
        if key.isalpha():
            new_dict = {"char": key, "num": item}
            letter_list.append(new_dict)

    letter_list.sort(reverse=True, key=sort_key)
    return(letter_list)

