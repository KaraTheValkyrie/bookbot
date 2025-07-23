def get_word_count(book_text):
    words = []
    words = book_text.split()
 #   return len(words)
    return(f"{len(words)} words found in the document")

def get_letter_counts(text):
    text = text.lower()
    letter_counts = {}
    for char in text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return(letter_counts)