with open('words.txt') as fd:
    wordlist = fd.read().split()

def consec_triple_double(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False

def locate_triple_double():
    for line in wordlist:
        word = line.strip()
        if consec_triple_double(word):
            print(word)

locate_triple_double()
