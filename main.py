from stats import get_num_words
from stats import get_char_count


def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()

    #print(file_contents)
    return file_contents




def main():

    text = get_book_text("/home/rylan/bookbot/books/frankenstein.txt")
    print(f"{get_num_words(text)} words found in the document")
    get_char_count(text)

main()