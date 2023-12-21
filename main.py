def read_book(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def letter_count(book_text):
    letters = {}
    book_text = book_text.lower()
    for letter in book_text:
        if letter.isalpha(): 
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def book_report(book):
    book_contents = read_book(book)
    letters = letter_count(book_contents)
    characters = list(letters.keys())
    characters.sort()
    print(f"--- Begin report of {book} ---")
    print(f"{word_count(book_contents)} words found in the document")
    print("")
    for character in characters:
        print(f"The '{character}' character was found '{letters[character]}' times")
    print("--- End report ---")
    

def main():
    book = 'books/frankenstein.txt'
    book_report(book)
    
main()