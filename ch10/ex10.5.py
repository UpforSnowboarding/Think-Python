def is_sorted(t):
    previous = t[0]
    for i in t:
        if i > previous:
            return True
        previous = i
    else:
        return False

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))

def is_sorted_method(t):
    return t == sorted(t)

print(is_sorted_method([1, 2, 2]))
print(is_sorted_method(['b', 'a']))
