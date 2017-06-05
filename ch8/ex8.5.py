# rushed version and only does lower case

def rotate_word(s,n):
    new_word = ''
    word = s.lower()
    for i in word:
        j = ord(i) + n
        new_word += chr(j)
    return new_word

print(rotate_word('hello',5))
