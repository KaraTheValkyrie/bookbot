def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
    
def word_count(book_text):
    words = []
    words = book_text.split()
 #   return len(words)
    return(f"{len(words)} words found in the document")

def main():
    text = get_book_text("books/frankenstein.txt")
    print(word_count(text))

main()