from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
    
def main():
    text = get_book_text("books/frankenstein.txt")
    print(get_word_count(text))

main()