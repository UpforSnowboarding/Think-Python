# rushed version and only does lower case

def rotate_word(s,n):
    new_word = ''
    word = s.lower()
    for i in word:
        j = ord(i) + n
        new_word += chr(j)
    return new_word

print(rotate_word('hello',5))

# Proper version

# Create a Caesar Cipher script
# It uses a key between 1 - 26 to encrypt and decrypt the plain text message

def encrypt_letter(char,n):

    # first set the values of upper and lower cases values

    if char.isupper():
        begin = ord('A')
    elif char.islower():
        begin = ord('a')
    else:
        return char

    letter = ord(char) - begin
    enc_letter = (letter + n) % 26 + begin # the modulo % 26 instils the base case, ensures the evaluation doesn't exceed the upper
    #bound of the key (no. of chars in the alphabet i.e. 26)
    return chr(enc_letter)

print(encrypt_letter('B', 5))

def encrypt_string(s,n):
    result = ''

    for i in s:
        result += encrypt_letter(i,n)

    return result

print(encrypt_string('hello', 10))
