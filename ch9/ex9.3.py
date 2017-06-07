with open('words.txt') as fd:
    wordlist = fd.read().split()

def avoids(word,forbiddenletters):
    for letter in word:
        if letter in forbiddenletters:
            return False
    return word

forbidden = 'a','e','w','b','z','c','t'
for line in wordlist:
    if avoids(line,forbidden):
        print(line)
