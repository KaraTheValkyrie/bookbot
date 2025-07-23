from stats import get_word_count, get_letter_counts, organize_letter_counts, sort_key
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
    
def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")

    input = sys.argv[1]
    print(f"Analyzing book found at {input}...")
    print("----------- Word Count ----------")
    
    text = get_book_text(input)
    print(get_word_count(text))
    
    print("--------- Character Count -------")
        
    letter_counts = get_letter_counts(text)
    sorted_letters = organize_letter_counts(letter_counts)
    
    for item in sorted_letters:
        
        print(f"{item["char"]}: {item["num"]}")
    
try:
    main()
except Exception as e:
    print(e)
    sys.exit(1)

