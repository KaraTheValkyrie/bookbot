from stats import get_word_count, get_letter_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
    
def main():
    text = get_book_text("books/frankenstein.txt")
    print(get_word_count(text))
    letter_counts = get_letter_counts(text)
    print(letter_counts)
    

main()