with open('words.txt') as fd:
    wordlist = fd.read().split()

def avoids(word,forbiddenletters):
    for letter in word:
        if letter in forbiddenletters:
            return False
    return True

forbidden = 'aewbzct'
for line in wordlist:
    if avoids(line,forbidden):
        print(line)

# second section where the users input the forbidden characters

forbidden = input('Please enter the letters you want to exclude: ')

for line in wordlist:
    if avoids(line,forbidden):
        print(line)
