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
    
    #print(char_dict)
   # print(len(char_list))

    return char_dict

def get_sorted_data(raw_chars_dict):
    sorted_list = []
    for key, value in raw_chars_dict.items():
        sorted_list.append({"char": key, "num": value})
    

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(dict):
    return dict["num"]


