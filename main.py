def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_char_report(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def print_char_report(chars_dict):
    # Filter out non-alphabetic characters and create a list of dictionaries
    alpha_chars = [{"char": char, "num": count} for char, count in chars_dict.items() if char.isalpha()]
    
    # Sort the list of dictionaries
    alpha_chars.sort(reverse=True, key=sort_on)
    
    # Print the report
    for item in alpha_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")

main()