def has_duplicates(l):

    t = list(l)
    t.sort()
    
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False

print(has_duplicates('cba'))
print(has_duplicates('abba'))
