import sys
from stats import word_count
from stats import char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() 
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_string = get_book_text(filepath)
    w_count = word_count(book_string)
    c_count = char_count(book_string)
    sorted_c_list = sort_chars(c_count)    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {w_count} total words")
    print("--------- Character Count -------")

    for d in sorted_c_list:
        if d["char"].isalpha():
            char = d["char"]
            count = d["num"]
            print(f"{char}: {count}")

    print("============= END ===============")
          
main()