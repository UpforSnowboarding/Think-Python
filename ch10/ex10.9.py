import time

def make_word():
    with open('words.txt') as fd:
        l1 = []
        for line in fd:
            word = line.strip()
            l1.append(word)
        return l1

def make_word2():
    with open('words.txt') as fd:
        l1 = []
        for line in fd:
            word = line.strip()
            l1 += [word]
        return l1


start_time = time.time()
t = make_word()
elasped_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elasped_time, 'seconds')

start_time = time.time()
t = make_word2()
elasped_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elasped_time, 'seconds')

