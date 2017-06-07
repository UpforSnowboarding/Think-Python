with open('words.txt') as fd:
    wordlist = fd.read().split()

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

count = 0
total = len(wordlist)


for line in wordlist:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)

print(count / total * 100, '%')
