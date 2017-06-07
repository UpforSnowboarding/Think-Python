with open('words.txt') as fd:
    wordlist = fd.read().split()

def uses_only(word,acceptedletters):
    for letter in word:
        if letter not in acceptedletters:
            return False
    return True

accepted = 'abcdefg'
for line in wordlist:
    word = line.strip()
    if uses_only(word,accepted):
        print(word)
