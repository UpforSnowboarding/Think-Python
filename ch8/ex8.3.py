# use the reverse string slice to complete the is_palindrome exercise

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome('banana'))
print(is_palindrome('redivider'))

# one lined version

def is_palindrome2(word):
    return word == word[::-1]

print(is_palindrome2('banana'))
print(is_palindrome2('redivider'))
