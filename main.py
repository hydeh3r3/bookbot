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