def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_length = get_num_words(text)
    
    char_dict = get_count_letter(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
    #print(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_length} words found in the document")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_letter(text):
    letter_counter = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            letter_counter[char] = letter_counter.get(char, 0) + 1
    return letter_counter
    
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True , key=sort_on)
    return sorted_list
    
main()