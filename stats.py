def get_num_words(book):
    words = []
    words = book.split()
    #print(len(words))
    word_count = len(words)

    return word_count

def get_char_count(book):
    book = book.lower()
    char_list = list(book)
    char_dict = {}
    #print(char_list)
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    print(char_dict)

    print(len(char_list))
