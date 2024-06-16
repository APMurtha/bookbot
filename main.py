def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"---Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n") 
    num_letters = count_each_letter(text)
    num_letters.sort(reverse=True, key=sort_on)
    for letter in num_letters:
        char = letter["char"]
        count = letter["num"]
        print(f"The letter \"{char}\" character was found {count} times ")
        print("--- End report ---")

def get_word_count(file):
    words = file.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_each_letter(text):
    letter_count = {}
    letter_dict = []
    for char in text.lower():
        if char in letter_count:
            letter_count[char] += 1
        elif char.isalpha():
            letter_count[char] = 1
    for char, count in letter_count.items():
        new_dict = {"char": char, "num": count}
        letter_dict.append(new_dict)
    return letter_dict

def sort_on(dict):
    return dict["num"]


main()
