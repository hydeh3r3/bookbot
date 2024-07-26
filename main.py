def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
main()

def count_words():
    with open("books/frankenstein.txt") as f:
        words = f.read().split()
        return len(words)

print(count_words())

def count_characters():
    char_counts = {}
    with open("books/frankenstein.txt") as f:
        for char in f.read().lower():
            if char.isalpha():
                char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

print(count_characters())