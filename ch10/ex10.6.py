def is_anagram(i,j):
    return sorted(i) == sorted(j)


print(is_anagram('stop', 'pots'))
print(is_anagram('different', 'letters'))
print(is_anagram([1, 2, 2], [2, 1, 2]))
