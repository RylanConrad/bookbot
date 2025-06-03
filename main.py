from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_data
import sys



def get_book_text():
    print(len(sys.argv))
    

    file_path = sys.argv[1]

    with open(file_path) as f:
        file_contents = f.read()

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return

    #print(file_contents)
    return file_contents

def print_sorted_data(sorted_data):
    for dicts in sorted_data:
        if dicts["char"].isalpha() == True:
            print(f"{dicts["char"]}: {dicts["num"]}")
    



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    else:
        text = get_book_text()  #remove hardcoded path to book file
        print(f"Found {get_num_words(text)} total words")
        sorted_data = get_sorted_data(get_char_count(text))
        print_sorted_data(sorted_data)

main()