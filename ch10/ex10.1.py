def nested_sum(n):
    total = 0
    for i in n:
        total += sum(i)
    return total

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
