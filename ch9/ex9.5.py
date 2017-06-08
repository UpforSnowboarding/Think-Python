with open('words.txt') as fd:
    wordlist = fd.read().split()

def uses_all(letters,word):
    for letter in letters:
        if letter not in word:
            return False
    return True


def using_all_letters():
    word_count = 0
    all_letters = input("Enter the required letters: ")

    for line in wordlist:
        word = line.strip()
        if uses_all(all_letters,word):
            print(word)
            word_count += 1
    return word_count

using_all_letters()
