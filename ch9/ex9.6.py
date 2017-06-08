
def is_abecedarian(word):
    previous = word[0]
    for i in word:
        if i < previous:
            return False
        previous = i
    return True

print(is_abecedarian('abcdefg'))

def is_abecedarian_while(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i = i + 1

    return True

print(is_abecedarian_while('abcde'))

def is_abecedarian_recursion(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recursion(word[1:])

print(is_abecedarian_recursion('banana'))
